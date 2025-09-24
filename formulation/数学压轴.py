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
        C_label = Tex("C").next_to(C_dot, LEFT, buff=0.1).scale(0.5)
        
        E_dot = Dot(axes.c2p(0, 2), color=RED)
        E_label = Tex("E").next_to(E_dot, LEFT, buff=0.1).scale(0.5)
        
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.6)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        
        self.add(axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,
                 C_dot,C_label,E_dot,E_label,origin_dot,origin_label)
        
       
        
        line_bc = Line(B_dot.get_center(),C_dot.get_center(),color=YELLOW,stroke_width=4)
        line_ae = Line(A_dot.get_center(),E_dot.get_center(),color=YELLOW,stroke_width=4)
         # 创建从E到O的线段
        line_eo = Line(E_dot.get_center(), origin_dot.get_center(), color=BLUE, stroke_width=2)
        # 创建带填充的角度（A-E-O角）
        angle_aeo = Angle(
            Line(E_dot,A_dot),
            Line(E_dot,origin_dot),
            radius=0.5,
            color=BLUE,
            other_angle=False,  # 只绘制较小的角度
            fill_opacity=0.8,   # 设置填充不透明度
            fill_color=BLUE     # 设置填充颜色
        )
        self.play(Create(line_bc),Create(line_ae),Create(line_eo),Create(angle_aeo))
        vt = ValueTracker(0.5) 
        P = always_redraw(lambda: Dot(
            axes.c2p(vt.get_value(), parabola(vt.get_value())),
            color=RED
        ))
        P_label = always_redraw(lambda: Tex("P").next_to(P, UP, buff=0.15))
        
        line_cp = always_redraw(lambda: Line(C_dot.get_center(),P.get_center(),color=PINK,stroke_width=4))
        angle_bcp = always_redraw(lambda: Angle(
            Line(C_dot,B_dot),
            Line(C_dot,P)
        ))
        # 添加所有动态元素
        self.add(P, P_label, line_cp,angle_bcp)
        
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
        
        
#   manim -pqh 数学压轴.py CirclePropertiesDemo