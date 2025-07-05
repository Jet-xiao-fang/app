from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class MathSymbolsScene(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        
        rectangle = Rectangle(width=6, height=4, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.5).scale(0.8)
        titile = Tex("求$DE^{2}+CE^{2}$的最大值？",color=YELLOW).next_to(rectangle,UP,buff = 1.5)
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)  # 左上 (D)
        ]
        self.add(titile)
        labels = ["A", "B", "C", "D"]
        dots = []
        texts = []
        for idx, (corner, label) in enumerate(zip(corners, labels)):
            dot = Dot(corner, color=RED)
            if idx == 0:  # A (左下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DL, buff=0.1)
            elif idx == 1:  # B (右下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DR, buff=0.1)
            elif idx == 2:  # C (右上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UR, buff=0.1)
            elif idx == 3:  # D (左上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UL, buff=0.1)

            dots.append(dot)
            texts.append(text)
        length_label = Text("6", color=YELLOW, font_size=20)
        length_label.next_to(rectangle, DOWN, buff=0.2)

        width_label = Text("4", color=YELLOW, font_size=20)
        width_label.next_to(rectangle, RIGHT, buff=0.2)

        self.add(length_label, width_label)

        self.add(rectangle, *dots, *texts)

        circle = Circle(
            radius=2,  # 半径
            color=BLUE,  # 边框颜色
            fill_opacity=0.5,  # 填充透明度
            fill_color=GREEN  # 填充颜色
        ).scale(0.8)

        circle.move_to(rectangle.get_corner(DL))

        angle = ValueTracker(0)

        point_E = always_redraw(lambda: Dot(
            color=RED,
            radius=0.08
        ).move_to(circle.point_from_proportion(angle.get_value() % 1)))

        label_E = always_redraw(lambda: Text("E", color=WHITE).scale(0.5).next_to(
            point_E, UR, buff=0.15))

        trail = TracedPath(point_E.get_center, stroke_color=YELLOW, stroke_width=2, dissipating_time=0.2)

        line_DE = always_redraw(lambda: Line(
            rectangle.get_corner(UL),
            point_E.get_center(),
            color=YELLOW,
            stroke_width=2
        ))
        line_CE = always_redraw(lambda: Line(
            rectangle.get_corner(UR),
            point_E.get_center(),
            color=YELLOW,
            stroke_width=2
        ))

        self.add(circle, point_E, label_E)
        
        self.play(Write(line_DE), Write(line_CE), Write(trail),run_time=2)

        self.play(
            angle.animate.set_value(2),
            run_time=8,
            rate_func=linear
        )

        self.wait(5)

# manim -pqh 正方形与圆.py MathSymbolsScene -r 1920,1080 
