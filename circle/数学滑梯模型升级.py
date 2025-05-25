from manim import *

class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[0, 4, 0.5],
            y_range=[0, 3, 0.5],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1"},
            x_length=8,
            y_length=6
        )
        
        axis_labels = axes.get_axis_labels(Tex("x"), Tex("y"))
        self.add(grid, axes, axis_labels)
        
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        self.add(origin_dot, origin_label)

        # 动画部分
        a_y = ValueTracker(1)

        def get_b_x():
            y = a_y.get_value()
            return np.sqrt(2**2 - y**2)

        # 动态计算点D和C的坐标
        def get_d_point():
            y = a_y.get_value()
            x_b = get_b_x()
            d_x = y/2
            d_y = y + x_b/2
            return axes.c2p(d_x, d_y)
        
        def get_c_point():
            y = a_y.get_value()
            x_b = get_b_x()
            c_x = x_b + y/2
            c_y = x_b/2
            return axes.c2p(c_x, c_y)

        # 创建动态元素
        point_a = always_redraw(lambda: Dot(axes.c2p(0, a_y.get_value()), color=RED))
        point_b = always_redraw(lambda: Dot(axes.c2p(get_b_x(), 0), color=BLUE))
        point_d = always_redraw(lambda: Dot(get_d_point(), color=YELLOW))
        point_c = always_redraw(lambda: Dot(get_c_point(), color=ORANGE))

        # 创建动态连线
        line_ab = always_redraw(lambda: Line(point_a, point_b, color=GREEN, stroke_width=4))
        line_ad = always_redraw(lambda: Line(point_a, point_d, color=PURPLE, stroke_width=4))
        line_dc = always_redraw(lambda: Line(point_d, point_c, color=PURPLE, stroke_width=4))
        line_cb = always_redraw(lambda: Line(point_c, point_b, color=PURPLE, stroke_width=4))
        line_od = always_redraw(lambda: Line(start=origin_dot.get_center(),end=point_d.get_center(),color=PINK,stroke_width=4))

        # 添加标签
        label_a = always_redraw(lambda: Tex("A", color=RED).next_to(point_a, LEFT))
        label_b = always_redraw(lambda: Tex("B", color=BLUE).next_to(point_b, DOWN))
        label_d = always_redraw(lambda: Tex("D", color=YELLOW).next_to(point_d, LEFT))
        label_c = always_redraw(lambda: Tex("C", color=ORANGE).next_to(point_c, RIGHT))

        # 添加长度标注
        length_label_ab = always_redraw(lambda: DecimalNumber(2, color=GREEN).next_to(line_ab.get_center(), UP, buff=0.1))
        length_label_ad = always_redraw(lambda: DecimalNumber(1, color=PURPLE).next_to(line_ad.get_center(), LEFT, buff=0.1))
        
        # 组合所有元素
        self.add(
            point_a, point_b, point_d, point_c,
            line_ab, line_ad, line_dc, line_cb,
            label_a, label_b, label_d, label_c,
            length_label_ab, length_label_ad,
            line_od
        )

        # 运行动画
        for _ in range(3):
            self.play(a_y.animate.set_value(2), run_time=3, rate_func=smooth)
            self.play(a_y.animate.set_value(1), run_time=3, rate_func=smooth)
        self.wait()

# manim -pqh 数学滑梯模型升级.py ParabolaPlot -r 1920,1080
