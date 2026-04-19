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
            x_range=[-2, 4, 1],
            y_range=[-2, 5, 1],  # 扩展y轴范围以显示完整图像
            x_length=6,
            y_length=7,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        title=Tex(r"当$DE:AE=1:2$时，求点D？",color=YELLOW).next_to(axes,UP,buff=1.5)
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
        A_dot = Dot(axes.c2p(-1,0), color=RED)
        A_label = Tex("A").next_to(A_dot, DOWN, buff=0.1).scale(0.6)
        
        B_dot = Dot(axes.c2p(3, 0), color=RED)
        B_label = Tex("B").next_to(B_dot, DOWN, buff=0.1).scale(0.6)
        
        C_dot = Dot(axes.c2p(0, 3), color=RED)
        C_label = Tex("C").next_to(C_dot, RIGHT, buff=0.1).scale(0.5)
        
        self.add(axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,C_dot,C_label)
        
       
        
        line_bc = Line(B_dot.get_center(),C_dot.get_center(),color=YELLOW,stroke_width=4)
        self.play(Create(line_bc))
        
        vt = ValueTracker(0.5) 
        D = always_redraw(lambda: Dot(
            axes.c2p(vt.get_value(), parabola(vt.get_value())),
            color=RED
        ))
        D_label = always_redraw(lambda: Tex("D").next_to(D, UP, buff=0.15))
        line_ad = always_redraw(lambda: Line(A_dot.get_center(),D.get_center(),color=PINK,stroke_width=4))
        
        # 计算AD与BC的交点E
        def get_intersection_point():
            # 获取AD和BC的坐标
            A_coords = axes.p2c(A_dot.get_center())
            D_coords = axes.p2c(D.get_center())
            B_coords = axes.p2c(B_dot.get_center())
            C_coords = axes.p2c(C_dot.get_center())
            
            # 计算AD直线方程: y = k1*x + b1
            k1 = (D_coords[1] - A_coords[1]) / (D_coords[0] - A_coords[0])
            b1 = A_coords[1] - k1 * A_coords[0]
            
            # 计算BC直线方程: y = k2*x + b2
            k2 = (C_coords[1] - B_coords[1]) / (C_coords[0] - B_coords[0])
            b2 = B_coords[1] - k2 * B_coords[0]
            
            # 求交点坐标
            if k1 == k2:  # 平行线无交点
                return axes.c2p(0, 0)
            else:
                x = (b2 - b1) / (k1 - k2)
                y = k1 * x + b1
                return axes.c2p(x, y)
        
        # 动态更新的交点E
        E = always_redraw(lambda: Dot(
            get_intersection_point(),
            color=BLUE
        ))
        E_label = always_redraw(lambda: Tex("E").next_to(E, UP, buff=0.15).scale(0.6))
        
        # 添加所有动态元素
        self.add(D, D_label, line_ad, E, E_label)
        
        # 动画：让D在抛物线上移动
        self.play(
            vt.animate.set_value(2.8),
            run_time=5,
            rate_func=linear
        )
        self.play(
            vt.animate.set_value(0.5),
            run_time=5,
            rate_func=linear
        )
        self.play(
            vt.animate.set_value(2),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)
        
        
#   manim -p 线段比例.py CirclePropertiesDemo