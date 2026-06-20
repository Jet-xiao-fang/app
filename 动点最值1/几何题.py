from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class Draw3DSphere(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        rectangle = Rectangle(width=4, height=4, color=BLUE).scale(1.2)
        rectangle.set_fill(color=BLUE, opacity=0.3).scale(0.8)
        corners = [
            rectangle.get_corner(UL),  # 左上 (A)
            rectangle.get_corner(DL),  # 左下 (B)
            rectangle.get_corner(DR),  # 右下 (C)
            rectangle.get_corner(UR),  # 右上 (D)
        ]
        # 1. 创建标题
        title = Tex("求$CF+EF$的最小值？", 
                    font_size=48,
                    color=WHITE
                    ).next_to(rectangle,UP,buff=1.5)
        self.add(title)
        labels = ["A", "B", "C", "D"]
        dots = []
        texts = []
        for idx, (corner, label) in enumerate(zip(corners, labels)):
            dot = Dot(corner, color=RED)
            if idx == 0:  # A (左下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UL, buff=0.1)
            elif idx == 1:  # B (右下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DL, buff=0.1)
            elif idx == 2:  # C (右上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DR, buff=0.1)
            elif idx == 3:  # D (左上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UR, buff=0.1)

            dots.append(dot)
            texts.append(text)
        # 添加对角线BD
        diagonal_bd = Line(corners[1], corners[3], color=GREEN)
        # 找到点E在BC上的位置，BE = 1
        # B、C的坐标分别为corners[1]和corners[2]，E位于BC上
        b_to_c = corners[2] - corners[1]
        e_position = corners[1] + (b_to_c / 4)  # BE = 1 (4是边BC的长度)
        point_e = Dot(e_position, color=RED)
        text_e = Text("E", color=WHITE, font_size=24).next_to(point_e, DOWN, buff=0.1)
        length_label = Text("4", color=YELLOW, font_size=30)
        length_label.next_to(rectangle, DOWN, buff=0.2)

        width_label = Text("4", color=YELLOW, font_size=30)
        width_label.next_to(rectangle, RIGHT, buff=0.2)

        self.add(length_label, width_label)

        self.add(rectangle, *dots, *texts, diagonal_bd, point_e, text_e)
        # t = ValueTracker(0.1)

        # dot_f = always_redraw(
        #     lambda: Dot(
        #         color=RED,
        #         radius=0.05
        #     ).move_to(diagonal_bd.point_from_proportion(t.get_value()))
        # )
        dot_f = Dot(corners[1], color=YELLOW, radius=0.05)  # 初始位置在B点
        text_f = always_redraw(lambda: Text("F").scale(0.5).next_to(dot_f, UR, buff=0.1))

        # 添加线条 CF 和 EF
        line_cf = always_redraw(lambda: Line(corners[2], dot_f.get_center(), color=RED,stroke_width=3))
        line_ef = always_redraw(lambda: Line(e_position, dot_f.get_center(), color=RED,stroke_width=3))
        # 添加动态元素
        self.add(line_cf, line_ef, dot_f, text_f)
        # self.play(
        #     t.animate.set_value(0.9),
        #     run_time=4,
        #     rate_func=linear
        # )
        # self.play(
        #     t.animate.set_value(0.1),
        #     run_time=4,
        #     rate_func=linear
        # )
        # self.play(
        #     t.animate.set_value(0.9),
        #     run_time=4,
        #     rate_func=linear
        # )
        self.play(
            MoveAlongPath(dot_f, diagonal_bd),
            run_time=6,
            rate_func=linear
        )
        self.play(
            MoveAlongPath(dot_f, diagonal_bd.reverse_points()),
            run_time=8,
            rate_func=linear
        )
        self.wait(2)

# manim -p 几何题.py Draw3DSphere