from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CirclePropertiesDemo(Scene):
    def construct(self):
        
        # 创建等比例坐标系
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-2, 5, 1],  # 扩展y轴范围以显示完整图像
            x_length=6,
            y_length=7,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        title=Tex(r"求出点$P$的坐标？",color=YELLOW).next_to(axes,UP,buff=1.5)
        self.add(title)
        
        def parabola(x):
            return -x**2 + 2*x + 3
            
        graph = axes.plot(
            parabola, 
            color=GREEN, 
            stroke_width=4,
            x_range=[-1.5, 3.5]  # 限制x范围以确保曲线在y值域内
        )
        graph_label = axes.get_graph_label(
            graph, 
            label=Tex('$y=-x^{2}+2x+3$'), 
            direction=UR,
            x_val = 1,
            buff = 0.1,
            dot = False
        ).set_color(PINK).scale(0.8)
        
        self.add(graph_label)
        
        # 计算交点
        # 与y轴交点 (x=0)
        A_dot = Dot(axes.c2p(3,0), color=RED)
        A_label = Tex("A(3,0)").next_to(A_dot, DOWN, buff=0.1).scale(0.6)
        
        B_dot = Dot(axes.c2p(-1, 0), color=RED)
        B_label = Tex("B(-1,0)").next_to(B_dot, DOWN, buff=0.1).scale(0.6)
        
        C_dot = Dot(axes.c2p(0, 3), color=RED)
        C_label = Tex("C(0,3)").next_to(C_dot, LEFT, buff=0.1).scale(0.5)
        
        M_dot = Dot(axes.c2p(1, 4), color=RED)
        M_label = Tex("M(1,4)").next_to(M_dot, UP, buff=0.1).scale(0.5)
        
        
        self.add(axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,C_dot,C_label,M_dot,M_label)
        
        
        P_dot = Dot(axes.c2p(0, 0), color=YELLOW)
        P_label = always_redraw(lambda: Tex("P", font_size=28, color=YELLOW).next_to(P_dot, LEFT, buff=0.1))
        self.add(P_dot,P_label)
        
        
        triangle = always_redraw(lambda: Polygon(
            P_dot.get_center(),
            M_dot.get_center(),
            A_dot.get_center(),
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.5
        ))
        self.play(Create(triangle),run_time=0.8)
         # 让点沿着x轴从 -3 移动到 3
        self.play(
            P_dot.animate.move_to(axes.c2p(0, 3)),
            run_time=6,  # 动画时长为3秒
            rate_func=linear  # 匀速运动
        )
        self.play(
            P_dot.animate.move_to(axes.c2p(0, 0)),
            run_time=6,  # 动画时长为3秒
            rate_func=linear  # 匀速运动
        )
        self.wait(3)
        
#   manim -p 8月24日.py CirclePropertiesDemo