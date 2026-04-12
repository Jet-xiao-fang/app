from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class MathSymbolsScene(Scene):
    def construct(self):

        rectangle = Rectangle(width=6, height=3, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.5)
        titile = Tex(r"求$\frac{AP}{BP}$的最大值？",color=YELLOW).next_to(rectangle,UP,buff = 1.5)
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

        width_label = Text("3", color=YELLOW, font_size=20)
        width_label.next_to(rectangle, RIGHT, buff=0.2)

        self.add(length_label, width_label)

        self.add(rectangle, *dots, *texts)
        
         # 计算 DC 的中点（圆心）
        D = corners[3]  # 左上角 (D)
        C = corners[2]  # 右上角 (C)
        DC_midpoint = (D + C) / 2  # DC 的中点
        
        
        # 创建完整圆（后续裁剪为半圆）
        circle = Circle(radius=3, arc_center=DC_midpoint, color=RED, stroke_width=4)
        
        # 裁剪为下半圆（从 0% 到 50%）
        semicircle = circle.copy()
        semicircle.pointwise_become_partial(circle, 0.5, 1)
        
        self.add(semicircle)
        p = Dot(semicircle.point_at_angle(190 * DEGREES), color=YELLOW)
        p_label = always_redraw(lambda: Text("P", color=WHITE, font_size=28).next_to(p, UP, buff=0.2))
        self.add(p, p_label)
        
        line_ap = always_redraw(lambda: DashedLine(rectangle.get_corner(DL),
                                             p.get_center(), color=ORANGE, stroke_width=3))
        line_bp = always_redraw(lambda: DashedLine(rectangle.get_corner(DR), 
                                                   p.get_center(), color=GREEN, stroke_width=3))
        
        trail = TracedPath(p.get_center, stroke_color=YELLOW, stroke_width=2, dissipating_time=0.2)
        self.play(
            Create(line_ap),
            Create(line_bp),
            Write(trail),
            run_time=1.5
        )
        
        self.play(
            MoveAlongPath(p, semicircle),
            run_time=6,
            rate_func=linear,
        )
        self.play(
            MoveAlongPath(p, semicircle),
            run_time=6,
            rate_func=linear,
        )
        self.wait(2)
        

        

# manim -p 正方形与半圆.py MathSymbolsScene
