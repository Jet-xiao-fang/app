from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class MathSymbolsScene(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        rectangle = Rectangle(width=8, height=6, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.5).scale(0.7)
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)  # 左上 (D)
        ]
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
        length_label = Text("8", color=YELLOW, font_size=28)
        length_label.next_to(rectangle, DOWN, buff=0.2)

        width_label = Text("6", color=YELLOW, font_size=28)
        width_label.next_to(rectangle, LEFT, buff=0.2)

        self.add(length_label, width_label)

        self.add(rectangle, *dots, *texts)
        # 添加点E（矩形中心）
        center = rectangle.get_center()
        point_E = Dot(center, color=GREEN)
        label_E = Text("E", color=WHITE, font_size=24).next_to(point_E, DOWN, buff=0.1)
        self.add(point_E, label_E)
        
        circle = Circle(
            radius=2,  # 半径
            color=RED
        ).scale(0.7)

        circle.move_to(rectangle.get_corner(UR))

        point_P = Dot(
            color=GREEN,
            radius=0.08
        ).move_to(circle.point_at_angle(245 * DEGREES))

        label_P = always_redraw(lambda: Text("P", color=WHITE).scale(0.5).next_to(
            point_P, UR, buff=0.15))

        trail = TracedPath(point_P.get_center, stroke_color=YELLOW, stroke_width=2, dissipating_time=0.2)

        line_DP = always_redraw(lambda: Line(
            rectangle.get_corner(UL),
            point_P.get_center(),
            color=ORANGE,
            stroke_width=3
        ))
        line_CP = always_redraw(lambda: Line(
            rectangle.get_corner(UR),
            point_P.get_center(),
            color=GREEN,
            stroke_width=3
        ))
        triangle_DEP = always_redraw(lambda: Polygon(
            rectangle.get_corner(UL),  # D点
            center,                    # E点
            point_P.get_center(),      # P点
            color=ORANGE,
            stroke_width=3,
            fill_opacity=0.5
        ))
        self.add(circle, point_P, label_P,triangle_DEP)
        
        self.play(Write(line_DP), Write(line_CP), Write(trail),run_time=1)

        self.play(
            Rotating(
                point_P,
                radians=2 * PI,  # 旋转360度（一圈）
                about_point=circle.get_center(),  # 围绕圆心旋转
                run_time=6,
                rate_func=linear
            )
        )
        self.play(
            Rotating(
                point_P,
                radians=2 * PI,  # 再旋转一圈
                about_point=circle.get_center(),
                run_time=6,
                rate_func=linear
            )
        )
        
        self.wait(3)

# manim -pqh 8月29日.py MathSymbolsScene
