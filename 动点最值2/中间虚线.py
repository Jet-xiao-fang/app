from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CirclePropertiesDemo(Scene):
    def construct(self):
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
        title=Tex(r"求$PA+PC$的最小值？",color=YELLOW).next_to(axes,UP,buff=1.5)
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
        
        # 添加对称轴虚线 (x=1)
        symmetry_line = DashedLine(
            start=axes.c2p(1, axes.y_range[0]),  # 从x=1,y最小值开始
            end=axes.c2p(1, axes.y_range[1]),    # 到x=1,y最大值结束
            color=BLUE,
            stroke_width=2.5
        )
        symmetry_label = MathTex("x=1").next_to(symmetry_line, RIGHT, buff=0.1).set_color(BLUE).scale(0.5)
        
        self.play(Write(symmetry_line),Write(symmetry_label),run_time=1)
        
        P_dot = Dot(axes.c2p(1, -1), color=YELLOW)
        P_label = always_redraw(lambda: Tex("P", font_size=28, color=YELLOW).next_to(P_dot, LEFT, buff=0.1))
        self.add(P_dot,P_label)
        
        line_ap=always_redraw(lambda: Line(A_dot.get_center(),P_dot.get_center(),stroke_width=3,color=ORANGE))
        line_cp=always_redraw(lambda: Line(C_dot.get_center(),P_dot.get_center(),stroke_width=3,color=ORANGE))
        
        self.play(Write(line_ap),Write(line_cp),run_time=2)
        self.play(
            P_dot.animate.move_to(axes.c2p(1, 4)),
            run_time=6,  # 动画时长为3秒
            rate_func=linear  # 匀速运动
        )
        self.play(
            P_dot.animate.move_to(axes.c2p(1, -1)),
            run_time=6,  # 动画时长为3秒
            rate_func=linear  # 匀速运动
        )
        
        self.wait(2)
        
#   manim -p 中间虚线.py CirclePropertiesDemo