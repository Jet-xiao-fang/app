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
            x_range=[-2, 8, 1],
            y_range=[-4, 6, 1],  # 扩展y轴范围以显示完整图像
            x_length=10,
            y_length=10,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        title=Tex(r"$PC+\frac{1}{2}PA$的最小值？",color=YELLOW).next_to(axes,UP,buff=1)
        self.add(title)
        
        def parabola(x):
            return x**2 - 6*x + 5
            
        graph = axes.plot(
            parabola, 
            color=GREEN, 
            stroke_width=4,
            x_range=[0, 6]  # 限制x范围以确保曲线在y值域内
        )
        graph_label = axes.get_graph_label(
            graph, 
            label=Tex('$y=x^{2}-6x+5$'), 
            direction=UL,
            x_val = 6,
            buff = 0.5,
            dot = False
        ).set_color(BLUE).scale(0.8)
        
        self.add(graph_label)
        
        # 计算交点
        # 与y轴交点 (x=0)
        A_dot = Dot(axes.c2p(1,0), color=RED)
        A_label = Tex("A").next_to(A_dot, UP, buff=0.1).scale(0.6)
        
        B_dot = Dot(axes.c2p(5, 0), color=RED)
        B_label = Tex("B").next_to(B_dot, UP, buff=0.1).scale(0.6)
        
        C_dot = Dot(axes.c2p(0, 5), color=RED)
        C_label = Tex("C").next_to(C_dot, RIGHT, buff=0.1).scale(0.5)
        
        
        self.add(axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,C_dot,C_label)
        
        # 圆
        circle = Circle(
            radius=2,
            color=BLUE,
            stroke_width = 3
        ).move_to(axes.c2p(5,0))
        self.play(Create(circle))
        # 动点P
        p_tracker = Dot(circle.point_at_angle(0), color=RED)
        
        P_label = always_redraw(lambda: Tex("P", font_size=30).next_to(p_tracker, UP, buff=0.1))
        
        line_pc = always_redraw(lambda: Line(p_tracker.get_center(),C_dot.get_center(),color=YELLOW,stroke_width=4))
        line_pa = always_redraw(lambda: Line(p_tracker.get_center(),A_dot.get_center(),color=YELLOW,stroke_width=4))
        # 显示动点P和三角形
        # 显示动点P和三角形
        self.play(Create(p_tracker), Write(P_label),Create(line_pc),Create(line_pa))
        self.wait(0.5)
        self.play(
            MoveAlongPath(p_tracker, circle),
            run_time=6,
            rate_func=linear,
        )
        self.play(
            MoveAlongPath(p_tracker, circle),
            run_time=6,
            rate_func=linear,
        )
        
        self.wait(1)
        
#   manim -pqh 曲线与圆.py CirclePropertiesDemo