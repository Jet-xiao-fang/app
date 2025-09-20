from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CirclePropertiesDemo(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 创建等比例坐标系
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-2, 7, 1],  # 扩展y轴范围以显示完整图像
            x_length=7,
            y_length=9,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        title=Tex(r"求$s1-s2$的最大值？",color=YELLOW).next_to(axes,UP,buff=1.5)
        self.add(title)
        
        def parabola(x):
            return -x**2 + 3*x + 4
            
        graph = axes.plot(
            parabola, 
            color=GREEN, 
            stroke_width=4,
            x_range=[-1.2, 4.2]  # 限制x范围以确保曲线在y值域内
        )
        graph_label = axes.get_graph_label(
            graph, 
            label=Tex('$y=-x^{2}+3x+4$'), 
            direction=UR,
            x_val = 1.5,
            buff = 0.1,
            dot = False
        ).set_color(PINK).scale(0.8)
        
        self.add(graph_label)
        
        # 计算交点
        # 与y轴交点 (x=0)
        A_dot = Dot(axes.c2p(-1,0), color=RED)
        A_label = Tex("A").next_to(A_dot, DOWN, buff=0.1).scale(0.6)
        
        B_dot = Dot(axes.c2p(4, 0), color=RED)
        B_label = Tex("B").next_to(B_dot, DOWN, buff=0.1).scale(0.6)
        
        C_dot = Dot(axes.c2p(0, 4), color=RED)
        C_label = Tex("C").next_to(C_dot, RIGHT, buff=0.1).scale(0.5)
        
        self.add(axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,C_dot,C_label)
        
        
         # 创建BC线段
        line_CB = Line(C_dot.get_center(), B_dot.get_center(), stroke_width=3, color=YELLOW)
        self.add(line_CB)
        
        # 创建 ValueTracker 控制 x 值
        x_tracker = ValueTracker(1)  # 初始 x = 0.2
        
        # 点 M 的位置绑定到 tracker
        M = always_redraw(
            lambda: Dot(color=RED).move_to(
                axes.c2p(x_tracker.get_value(), parabola(x_tracker.get_value()))
            )
        )
        M_label = always_redraw(
            lambda: Tex("M").next_to(M, UP, buff=0.1).scale(0.6)
        )
        
        # 直线AM
        line_AM = always_redraw(
            lambda: Line(
                A_dot.get_center(),
                M.get_center(),
                color=BLUE,
                stroke_width=3
            )
        )
        
        # 计算AM与y轴的交点D (x=0)
        def get_D_point():
            M_x = x_tracker.get_value()
            M_y = parabola(M_x)
            A_x, A_y = -1, 0
            
            # 计算直线AM的斜率和截距
            if M_x != A_x:
                k = (M_y - A_y) / (M_x - A_x)
                b = A_y - k * A_x
                
                # 与y轴交点 (x=0)
                D_y = b  # 因为 y = k*0 + b = b
                return axes.c2p(0, D_y)
            else:
                return axes.c2p(0, A_y)
        
        D_dot = always_redraw(
            lambda: Dot(color=PURPLE).move_to(get_D_point())
        )
        D_label = always_redraw(
            lambda: Tex("D").next_to(D_dot, LEFT, buff=0.1).scale(0.6)
        )
        
        # 计算AM与BC的交点E
        def get_E_point():
            M_x = x_tracker.get_value()
            M_y = parabola(M_x)
            A_x, A_y = -1, 0
            
            # 直线AM的参数
            if M_x != A_x:
                k_AM = (M_y - A_y) / (M_x - A_x)
                b_AM = A_y - k_AM * A_x
            else:
                k_AM = float('inf')
                b_AM = float('inf')
            
            # 直线BC的参数 (两点式)
            C_x, C_y = 0, 4
            B_x, B_y = 4, 0
            k_BC = (B_y - C_y) / (B_x - C_x)
            b_BC = C_y - k_BC * C_x
            
            # 计算交点E
            if k_AM != k_BC:
                E_x = (b_BC - b_AM) / (k_AM - k_BC)
                E_y = k_AM * E_x + b_AM
                return axes.c2p(E_x, E_y)
            else:
                return axes.c2p(float('inf'), float('inf'))
        
        E_dot = always_redraw(
            lambda: Dot(color=ORANGE).move_to(get_E_point())
        )
        E_label = always_redraw(
            lambda: Tex("E").next_to(E_dot, UP, buff=0.1).scale(0.6)
        )
        
        # 三角形MBE
        triangle_MBE = always_redraw(
            lambda: Polygon(
                M.get_center(),
                B_dot.get_center(),
                E_dot.get_center(),
                color=BLUE,
                fill_opacity=0.3,
                stroke_width=2
            )
        )
        
        # 三角形CDE
        triangle_CDE = always_redraw(
            lambda: Polygon(
                C_dot.get_center(),
                D_dot.get_center(),
                E_dot.get_center(),
                color=GREEN,
                fill_opacity=0.3,
                stroke_width=2
            )
        )
        
        # 面积标签
        s1_label = always_redraw(
            lambda: Tex(r"$S_1$", color=BLUE).move_to(triangle_MBE.get_center()).scale(0.6)
        )
        
        s2_label = always_redraw(
            lambda: Tex(r"$S_2$", color=GREEN).move_to(triangle_CDE.get_center()).scale(0.6)
        )
        
        # 添加所有动态元素
        self.add(
            M, M_label,
            line_AM,
            D_dot, D_label,
            E_dot, E_label,
            triangle_MBE, triangle_CDE,
            s1_label, s2_label
        )
        
        # 动画演示M移动
        self.play(x_tracker.animate.set_value(3.8), run_time=6, rate_func=linear)
        # 再移动回去
        self.play(x_tracker.animate.set_value(1), run_time=4, rate_func=linear)
        
        self.play(x_tracker.animate.set_value(2.5), run_time=2, rate_func=linear)
        
        self.wait(3)
        
#   manim -pqh  2个三角形面积差.py CirclePropertiesDemo