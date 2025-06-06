from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        tex = Tex(r"求: $\triangle ABP$ 的最小值?", color=BLUE).to_edge(UP)
        self.play(Write(tex))
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-2, 6, 1],
            x_length=16,
            y_length=8,
            
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-8, 8, 0.5],
            y_range=[-2, 6, 0.5],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1"},
            x_length=16,
            y_length=8
            
        )
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))  # 使用MathTex
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        
        # 抛物线绘制
        parabola = axes.plot(
            lambda x: x**2 / 4,
            color=GREEN,
            stroke_width=4
        )
        # parabola_label = MathTex(r"y = \dfrac{1}{4}x^2", color=GREEN).scale(0.8)
         # parabola_label.next_to(parabola.point_from_proportion(0.7), DOWN, buff=0.2)
        # 替换原有parabola_label定义
        parabola_label = axes.get_graph_label(
            graph=parabola,
            label=MathTex(r"y = \dfrac{1}{4}x^2", color=GREEN).scale(0.8),
            x_val=-3,  # 指定x=3处的标签位置
            direction=LEFT,
            buff=0.4,
            dot=False  # 不显示定位点
        )
        # 添加到场景
        self.add(grid, axes, axis_labels, origin_dot, origin_label,parabola,parabola_label)
        # 正确写法（Axes坐标系转换）
        A_coords = (0, 1)  # 数学坐标系中的坐标
        A_point = Dot(axes.c2p(*A_coords), color=RED)  # 转换到场景坐标系
        Label_A = Tex("A").next_to(A_point, LEFT, buff=0.1)
        B_coords = (1, 4)  # 数学坐标系中的坐标
        B_point = Dot(axes.c2p(*B_coords), color=RED)  # 转换到场景坐标系
        Label_B = Tex("B").next_to(B_point, RIGHT, buff=0.1)
        #绘制线段AB
        Line_AB = Line(
            start= A_point.get_center(),
            end= B_point.get_center()

        )
        self.add(A_point,Label_A,B_point,Label_B,Line_AB)
        # 创建动点P（网页3、5的实现方法）
        vt = ValueTracker(1)  # 初始值对应x=1
        P = always_redraw(lambda: Dot(
            axes.c2p(vt.get_value(), (vt.get_value()**2)/4),
            color=YELLOW
        ))
        P_label = always_redraw(lambda: Tex("P").next_to(P, UP, buff=0.15))
        AP = always_redraw(lambda: DashedLine(
            A_point.get_center(), 
            P.get_center(),
            color=RED_C,
            stroke_width=2.5
        ))
        BP = always_redraw(lambda: DashedLine(
            B_point.get_center(),
            P.get_center(),
            color=BLUE_C,
            stroke_width=2.5
        ))
        self.play(
            Create(P),
            Write(P_label),
            Create(AP),
            Create(BP),
            run_time = 2
        )
         # 轨迹跟踪（网页6的抛物线绘制扩展）
        trace = TracedPath(P.get_center, dissipating_time=1, stroke_color=YELLOW)
        self.add(trace)  # 添加轨迹追踪
        # 动画控制（网页5的运动控制优化）
        self.play(
            vt.animate.set_value(4),  # x从1运动到4
            rate_func=linear,
            run_time=6
        )
        self.play(
            vt.animate.set_value(1),  # x从1运动到4
            rate_func=linear,
            run_time=6
        )
        self.wait(2)


# manim -pqh 正方形.py ParabolaPlot -r 1920,1080