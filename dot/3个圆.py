from manim import *
import numpy as np

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex


class CircleArea(Scene):
    def construct(self):
        # 标题
        title = Text("三个相切圆的中间空隙面积", font_size=40,color=BLUE)
        self.camera.background_color = "#0F0F1A"
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, buff=1.5))

        # 设置圆的半径
        radius = 2
        
        # 计算圆心位置（形成等边三角形）
        top_center = UP * np.sqrt(3) * radius
        left_center = LEFT * radius
        right_center = RIGHT * radius

        # 创建三个圆
        circle_top = Circle(radius=radius, color=BLUE, fill_opacity=0.3).move_to(top_center)
        circle_left = Circle(radius=radius, color=GREEN, fill_opacity=0.3).move_to(left_center)
        circle_right = Circle(radius=radius, color=YELLOW, fill_opacity=0.3).move_to(right_center)

        # 绘制三个圆
        circles = VGroup(circle_top, circle_left, circle_right)
        self.play(Create(circles), run_time=2)
        self.wait(1)

        # 添加圆心和连接线（形成等边三角形）
        centers = VGroup(
            Dot(top_center, color=RED),
            Dot(left_center, color=RED),
            Dot(right_center, color=RED)
        )
        self.play(Create(centers))
        triangle = Polygon(
            top_center,
            left_center,
            right_center,
            color=WHITE,
            stroke_width=2
        )
        self.play(Create(triangle), run_time=2)
        self.wait(1)

        # 标记三角形边长
        side_label = MathTex(r"\text{边长} = 4", font_size=40)
        side_label.next_to(triangle, DOWN)
        self.play(Write(side_label))
        self.wait(1)

        # 计算切点位置（圆心连线的中点）
        top_left_tangent = (top_center + left_center) / 2
        top_right_tangent = (top_center + right_center) / 2
        bottom_tangent = (left_center + right_center) / 2

        # 创建曲边三角形（由三段圆弧组成）
        arc_top = Arc(
            radius=radius,
            start_angle=240 * DEGREES,
            angle=60 * DEGREES,
            arc_center=top_center,
            color=PURPLE,
            stroke_width=0
        )
        
        arc_right = Arc(
            radius=radius,
            start_angle=120 * DEGREES,
            angle=60 * DEGREES,
            arc_center=right_center,
            color=PURPLE,
            stroke_width=0
        )
        
        arc_left = Arc(
            radius=radius,
            start_angle=0,
            angle=60 * DEGREES,
            arc_center=left_center,
            color=PURPLE,
            stroke_width=0
        )
        
        # 组合成曲边三角形
        curved_triangle = VMobject()
        curved_triangle.set_points_smoothly([
            *arc_top.get_points(),
            *arc_right.get_points(),
            *arc_left.get_points(),
            arc_top.get_start()
        ])
        curved_triangle.set_fill(RED, opacity=0.5)
        curved_triangle.set_stroke(width=0)
        
        # 绘制曲边三角形并添加标注
        self.play(FadeIn(curved_triangle))
        self.wait(1)
        
        # 添加弧线标注
        arc_label_top = MathTex(r"60^\circ", font_size=30).move_to(
            top_center + DOWN * 0.3 + RIGHT * 0.5
        )
        arc_label_right = MathTex(r"60^\circ", font_size=30).move_to(
            right_center + LEFT * 0.6 + UP * 0.3
        )
        arc_label_left = MathTex(r"60^\circ", font_size=30).move_to(
            left_center + RIGHT * 0.6 + UP * 0.3
        )
        
        self.play(
            Write(arc_label_top),
            Write(arc_label_right),
            Write(arc_label_left)
        )
        self.wait(1)

        # 添加提示文本
        hint_text = VGroup(
        Text("求阴影部分的面积（", font_size=30, color=YELLOW),
        Text("红色部分", font_size=30, color=RED),
        Text("）", font_size=30, color=YELLOW)
        ).arrange(RIGHT, buff=0.1)
        hint_text.next_to(circles, DOWN, buff=1)
        self.play(Write(hint_text))
        self.wait(0.5)

        # 添加3秒倒计时
        countdown_title = Text("计算开始倒计时", font_size=35, color=YELLOW)
        countdown_title.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(countdown_title))
        self.wait(0.5)

        # 创建倒计时数字
        countdown_3 = Text("3", font_size=100, color=WHITE)
        countdown_2 = Text("2", font_size=100, color=WHITE)
        countdown_1 = Text("1", font_size=100, color=WHITE)
        countdown_start = Text("开始!", font_size=100, color=YELLOW)

        countdown_group = VGroup(countdown_3, countdown_2, countdown_1, countdown_start)
        countdown_group.move_to(ORIGIN)

        # 倒计时动画
        self.play(FadeIn(countdown_3))
        self.wait(0.8)
        self.play(
            countdown_3.animate.scale(1.5),
            run_time=0.1
        )
        self.play(
            countdown_3.animate.scale(0.5),
            run_time=0.1
        )
        self.play(ReplacementTransform(countdown_3, countdown_2))
        self.wait(0.8)
        self.play(
            countdown_2.animate.scale(1.5),
            run_time=0.1
        )
        self.play(
            countdown_2.animate.scale(0.5),
            run_time=0.1
        )
        self.play(ReplacementTransform(countdown_2, countdown_1))
        self.wait(0.8)
        self.play(
            countdown_1.animate.scale(1.5),
            run_time=0.1
        )
        self.play(
            countdown_1.animate.scale(0.5),
            run_time=0.1
        )
        self.play(ReplacementTransform(countdown_1, countdown_start))
        self.wait(0.5)
        self.play(
            countdown_start.animate.scale(1.5),
            run_time=0.2
        )
        self.play(
            FadeOut(countdown_start, scale=0.5),
            FadeOut(countdown_title),
            run_time=0.5
        )
        self.wait(0.5)

        # 显示计算公式
        formula_title = Text("阴影面积计算公式:", font_size=35, color=YELLOW)
        formula_title.to_edge(UP).shift(DOWN * 1.5)
        
        formula = MathTex(
            r"\text{面积} = \text{三角形面积} - 3 \times \text{扇形面积}",
            font_size=40
        )
        
        formula_detail = MathTex(
            r"= \frac{\sqrt{3}}{4} a^2 - 3 \times \frac{60^\circ}{360^\circ} \pi r^2",
            font_size=40
        )
        
        formula_result = MathTex(
            r"= \frac{\sqrt{3}}{4} \times 4^2 - \frac{1}{2} \pi \times 2^2",
            font_size=40
        )
        
        final_result = MathTex(
            r"= 4\sqrt{3} - 2\pi \approx 1.511",
            font_size=40,
            color=YELLOW
        )
        
        formula_group = VGroup(formula, formula_detail, formula_result, final_result)
        formula_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        formula_group.next_to(formula_title, DOWN, buff=0.5)
        
        self.play(Write(formula_title))
        self.wait(0.5)
        self.play(Write(formula))
        self.wait(1)
        self.play(Write(formula_detail))
        self.wait(1.5)
        self.play(Write(formula_result))
        self.wait(1.5)
        self.play(Write(final_result))
        self.wait(3)
        
        # 高亮最终结果
        box = SurroundingRectangle(final_result, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(3)
        
# manim -pqh --format=png 3个圆.py CircleArea -r 1920,1080