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
            y_range=[-5, 2, 1],  # 扩展y轴范围以显示完整图像
            x_length=6,
            y_length=7,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        title=Tex(r"求线段$PQ$的最大值？",color=YELLOW).next_to(axes,UP,buff=1.5)
        self.add(title)
        
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
            x_val = -1,
            buff = 0.1,
            dot = False
        ).set_color(PINK).scale(0.8)
        
        self.add(graph_label)
        
        # 计算交点
        # 与y轴交点 (x=0)
        A_dot = Dot(axes.c2p(-3,0), color=RED)
        A_label = Tex("A").next_to(A_dot, DOWN, buff=0.1).scale(0.6)
        
        B_dot = Dot(axes.c2p(1, 0), color=RED)
        B_label = Tex("B").next_to(B_dot, DOWN, buff=0.1).scale(0.6)
        
        C_dot = Dot(axes.c2p(0, -3), color=RED)
        C_label = Tex("C").next_to(C_dot, RIGHT, buff=0.1).scale(0.5)
        
        
        self.add(axes,axis_labels,graph,A_dot,A_label,B_dot,B_label,C_dot,C_label)
        
        line_ac = Line(A_dot.get_center(),C_dot.get_center(),color=YELLOW,stroke_width=3)
        
        self.play(Create(line_ac))
        
         # 创建移动的竖线
        vertical_line = always_redraw(lambda: DashedLine(
            start=axes.c2p(-1.5, -5),
            end=axes.c2p(-1.5, 2),
            color=BLUE,
            stroke_width=2
        ))
        
        # 创建P点（在线段AC上）
        P_dot = always_redraw(lambda: Dot(
            line_ac.point_from_proportion(
                (-1.5 - (-3)) / (0 - (-3))  # 计算比例
            ),
            color=ORANGE
        ))
        P_label = always_redraw(lambda: Tex("P").next_to(P_dot, UR, buff=0.1).scale(0.6))
        
        # 创建Q点（在抛物线上）
        Q_dot = always_redraw(lambda: Dot(
            axes.c2p(-1.5, parabola(-1.5)),
            color=PURPLE
        ))
        Q_label = always_redraw(lambda: Tex("Q").next_to(Q_dot, DL, buff=0.1).scale(0.6))
        
        # 创建PQ线段
        PQ_line = always_redraw(lambda: Line(
            P_dot.get_center(),
            Q_dot.get_center(),
            color=WHITE,
            stroke_width=3
        ))
        
        # 添加所有动态元素
        self.add(vertical_line, P_dot, P_label, Q_dot, Q_label, PQ_line)
        
        # 使用追踪器控制竖线位置
        tracker = ValueTracker(-3)
        vertical_line.add_updater(lambda m: m.become(DashedLine(
            start=axes.c2p(tracker.get_value(), -5),
            end=axes.c2p(tracker.get_value(), 2),
            color=BLUE,
            stroke_width=2
        )))
        P_dot.add_updater(lambda m: m.move_to(line_ac.point_from_proportion(
            (tracker.get_value() - (-3)) / (0 - (-3))
        )))
        Q_dot.add_updater(lambda m: m.move_to(axes.c2p(
            tracker.get_value(),
            parabola(tracker.get_value())
        )))
        
        # 动画：竖线从x=-3移动到x=0
        self.play(
            tracker.animate.set_value(0),
            run_time=8,
            rate_func=linear
        )
        self.play(
            tracker.animate.set_value(-1.5),
            run_time=4,
            rate_func=linear
        )
    
        self.wait(3)
        
#   manim -p 线段最值.py CirclePropertiesDemo