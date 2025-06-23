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
        title = Tex("三个相切圆的中间空隙面积", font_size=40)
        self.camera.background_color = "#0F0F1A"
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, buff=3))
        
        # 创建三个圆（上面一个，下面两个）
        circle_top = Circle(radius=1, color=BLUE, fill_opacity=0.3).shift(UP * np.sqrt(3))
        circle_left = Circle(radius=1, color=GREEN, fill_opacity=0.3).shift(LEFT)
        circle_right = Circle(radius=1, color=YELLOW, fill_opacity=0.3).shift(RIGHT)
        
        # 绘制三个圆
        circles = VGroup(circle_top, circle_left, circle_right)
        self.play(Create(circles), run_time=2)
        self.wait(1)
        
        # 添加圆心和连接线（形成等边三角形）
        centers = VGroup(
            Dot(circle_top.get_center(), color=RED),
            Dot(circle_left.get_center(), color=RED),
            Dot(circle_right.get_center(), color=RED)
        )
        self.play(Create(centers))
        
        triangle = Polygon(
            circle_top.get_center(),
            circle_left.get_center(),
            circle_right.get_center(),
            color=WHITE,
            stroke_width=2
        )
        self.play(Create(triangle), run_time=2)
        self.wait(1)
        
        # 标记三角形边长
        side_label = Tex("边长 = 2", font_size=30)
        side_label.next_to(triangle, DOWN)
        self.play(Write(side_label))
        self.wait(1)
        
        # 添加3秒倒计时
        countdown_title = Text("计算开始倒计时", font_size=35, color=YELLOW)
        countdown_title.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(countdown_title))
        self.wait(0.5)
        
        # 创建倒计时数字
        countdown_3 = Tex("3", font_size=100, color=WHITE)
        countdown_2 = Tex("2", font_size=100, color=WHITE)
        countdown_1 = Tex("1", font_size=100, color=WHITE)
        countdown_start = Tex("开始!", font_size=100, color="WHITE")
        
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
        
        # 显示面积公式推导
        formula_title = Tex("面积计算:", font_size=35)
        formula_title.to_edge(LEFT).shift(DOWN*2)
        
        # 等边三角形面积
        triangle_area = MathTex(
            r"S_{\triangle} = \frac{\sqrt{3}}{4} \times \text{边长}^2 = \frac{\sqrt{3}}{4} \times 2^2 = \sqrt{3}",
            font_size=35
        )
        triangle_area.next_to(formula_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # 三个扇形面积
        sector_area = MathTex(
            r"3 \times S_{\text{扇形}} = 3 \times \frac{60^\circ}{360^\circ} \pi r^2 = 3 \times \frac{1}{6} \pi \times 1^2 = \frac{\pi}{2}",
            font_size=35
        )
        sector_area.next_to(triangle_area, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # 最终公式
        final_formula = MathTex(
            r"S_{\text{空隙}} = S_{\triangle} - 3S_{\text{扇形}} = \sqrt{3} - \frac{\pi}{2}",
            font_size=35
        )
        final_formula.next_to(sector_area, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # 数值结果
        result = MathTex(
            r"S_{\text{空隙}} \approx 1.732 - 1.571 \approx 0.161",
            font_size=35,
            color=YELLOW
        )
        result.next_to(final_formula, DOWN, aligned_edge=LEFT, buff=0.3)
        
        formulas = VGroup(
            formula_title,
            triangle_area,
            sector_area,
            final_formula,
            result
        ).shift(DOWN*0.5)
        
        self.play(FadeIn(formula_title))
        self.wait(0.5)
        self.play(FadeIn(triangle_area))
        self.wait(1.5)
        self.play(FadeIn(sector_area))
        self.wait(1.5)
        self.play(FadeIn(final_formula))
        self.wait(1.5)
        self.play(FadeIn(result))
        self.wait(3)
        
        # 清理画面
        self.play(
            FadeOut(title),
            FadeOut(side_label),
            FadeOut(formulas),
            FadeOut(triangle),
            FadeOut(centers),
            circles.animate.set_fill(opacity=0.1).set_stroke(width=1),
        )
        
        # 显示最终答案
        final_answer = MathTex(
            r"\text{中间空隙面积} = \sqrt{3} - \frac{\pi}{2} \approx 0.161",
            font_size=40,
            color="#FFAA00"
        )
        box = SurroundingRectangle(final_answer, color=BLUE, buff=0.5, corner_radius=0.2)
        box.set_fill(BLACK, opacity=0.5)
        
        self.play(
            DrawBorderThenFill(box),
            Write(final_answer),
            run_time=2
        )
        self.wait(3)