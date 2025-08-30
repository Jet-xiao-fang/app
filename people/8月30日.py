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
            x_range=[-4, 2, 1],
            y_range=[-5, 3, 1],  # 扩展y轴范围以显示完整图像
            x_length=6,
            y_length=8,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(
            Tex("x").set_color(WHITE),
            Tex("y").set_color(WHITE)
        )
        title=Tex(r"求$\triangle APC$面积的最大值？",color=YELLOW,font_size = 50).next_to(axes,UP,buff=1)
        self.add(title)
        # 添加抛物线函数 y = -x^2 - 2x + 3
        def parabola(x):
            return x**2 + 2*x - 3
            
        graph = axes.plot(
            parabola, 
            color=GREEN, 
            stroke_width=4,
            x_range=[-3.5, 1.5]  # 限制x范围以确保曲线在y值域内
        )
        graph_label = axes.get_graph_label(
            graph, 
            label=Tex('$y=x^{2}+2x-3$'), 
            direction=DL,
            x_val = -2,
            buff = 0.1,
            dot = False
        ).set_color(YELLOW).scale(0.7)
        # 计算交点
        # 与y轴交点 (x=0)
        A_dot = Dot(axes.c2p(-3,0), color=RED)
        A_label = Tex("A(-3,0)").next_to(A_dot, DL,buff=0.1).scale(0.5)
        
        B_dot = Dot(axes.c2p(1, 0), color=RED)
        B_label = Tex("B(1,0)").next_to(B_dot, DR, buff=0.1).scale(0.5)
        
        C_dot = Dot(axes.c2p(0, -3), color=RED)
        C_label = Tex("C(0,-3)").next_to(C_dot, RIGHT, buff=0.1).scale(0.5)
        
        
        self.add(graph_label,axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,C_dot,C_label)
        
        # 动点P
        p_tracker = ValueTracker(-2.8)  # 控制P点位置的追踪器
        def get_p_point():
            x = p_tracker.get_value()
            y = parabola(x)
            return axes.c2p(x, y)
        
        P_dot = always_redraw(lambda: Dot(get_p_point(), color=ORANGE).scale(1.2))
        P_label = always_redraw(lambda: Tex("P", font_size=30).next_to(P_dot, DOWN, buff=0.1))
        
        # 三角形PAB（橘黄色）
        triangle = always_redraw(lambda: Polygon(
            A_dot.get_center(),
            C_dot.get_center(),
            get_p_point(),
            color=YELLOW,
            fill_color=ORANGE,
            fill_opacity=0.5,
            stroke_width=1
        ))
        # 显示动点P和三角形
        self.play(Create(P_dot), Write(P_label), Create(triangle),run_time=2)
        self.wait(0.5)
        # 动画展示P点移动和三角形变化
        for i in range(2):
            self.play(
                p_tracker.animate.set_value(-0.2),
                run_time=3,
                rate_func=rate_functions.smooth
            )
            self.play(
                p_tracker.animate.set_value(-2.8),
                run_time=3,
                rate_func=rate_functions.smooth
            )
        
        self.wait(3)
        
#   manim -pqh --format=png 8月30日.py CirclePropertiesDemo -r 1920,1080