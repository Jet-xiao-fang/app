from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class GridExample(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        rectangle = Rectangle(width=4, height=4, color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        title = Tex("求$CP+BP$的最小值？", color=YELLOW).next_to(rectangle, UP, buff=1.5)
        corners = [
            rectangle.get_corner(DL),
            rectangle.get_corner(DR),
            rectangle.get_corner(UR),
            rectangle.get_corner(UL)
        ]
        self.add(title)
        labels = ["A", "B", "C", "D"]
        dots = []
        texts = []
        for idx, (corner, label) in enumerate(zip(corners, labels)):
            dot = Dot(corner, color=RED)
            if idx == 0:
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DL, buff=0.1)
            if idx == 1:
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DR, buff=0.1)
            if idx == 2:
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UR, buff=0.1)
            if idx == 3:
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UL, buff=0.1)
            dots.append(dot)
            texts.append(text)
        length_label = Text("4", color=YELLOW, font_size=36)
        length_label.next_to(rectangle, RIGHT, buff=0.2)
        self.add(length_label)

        self.add(rectangle, *dots, *texts)

        circle = Circle(
            radius=2,
            color=BLUE,
            fill_color=GREEN,
            fill_opacity=0.5
        )
        circle.move_to(rectangle.get_corner(DL))

        p = Dot(circle.point_at_angle(0), color=RED)
        p_label = always_redraw(lambda: Text("P", color=WHITE, font_size=28).next_to(p, UP, buff=0.2))
        self.add(circle, p, p_label)
        line_cp = always_redraw(lambda: Line(rectangle.get_corner(UR),
                                             p.get_center(), color=YELLOW, stroke_width=2))
        line_bp = always_redraw(lambda: Line(rectangle.get_corner(DR), p.get_center(), color=YELLOW, stroke_width=2))
        trail = TracedPath(p.get_center, stroke_color=RED, stroke_width=2, dissipating_time=0.2)
        self.play(
            Create(line_cp),
            Create(line_bp),
            Write(trail),
            run_time=2
        )
        self.play(
            MoveAlongPath(p, circle),
            run_time=6,
            rate_func=linear,
        )
        self.play(
            MoveAlongPath(p, circle),
            run_time=6,
            rate_func=linear,
        )
        self.wait(2)
        

    

# manim -pqh --format=png 正方形与圆1.py GridExample -r 1920,1080