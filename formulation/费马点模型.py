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
        
        # 创建矩形
        rectangle = Rectangle(width=4, height=4, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.5).scale(0.8)
        title = Tex("求$PA+PB+PD$的最小值？", color=YELLOW).next_to(rectangle, UP, buff=1.5)
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)   # 左上 (D)
        ]
        self.add(title)
        
        # 创建四个角的点和标签
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
        
        # 添加矩形和标签
        self.play(Create(rectangle))
        self.play(*[Create(d) for d in dots], *[Write(t) for t in texts])
        self.wait(1)
        
        # 创建对角线AC
        diag_ac = Line(corners[0], corners[2], color=YELLOW)
        self.play(Create(diag_ac))
        self.wait(1)
        length_label = Tex("$2\sqrt{2}$", color=YELLOW, font_size=20)
        length_label.next_to(rectangle, DOWN, buff=0.2)
        self.play(Write(length_label))
        # 创建点P及其移动动画
        p_tracker = ValueTracker(0.0)
        p_dot = always_redraw(lambda: Dot(
            diag_ac.point_from_proportion(p_tracker.get_value()),
            color=YELLOW
        ))
        p_label = always_redraw(lambda: Tex("P", color=YELLOW, font_size=24).next_to(p_dot, UP, buff=0.1))
        
        # 创建动态线段
        ap_line = always_redraw(lambda: Line(
            corners[0], 
            p_dot.get_center(), 
            color=BLUE_B,
            stroke_width=3
        ))
        bp_line = always_redraw(lambda: Line(
            corners[1], 
            p_dot.get_center(), 
            color=GREEN_B,
            stroke_width=3
        ))
        pd_line = always_redraw(lambda: Line(
            p_dot.get_center(), 
            corners[3], 
            color=RED_B,
            stroke_width=3
        ))
        
        # 添加点P和线段
        self.play(Create(p_dot), Write(p_label))
        self.play(Create(ap_line), Create(bp_line), Create(pd_line))
        self.wait(0.5)
        
        # 点P移动动画
        self.play(
            p_tracker.animate.set_value(1.0),
            rate_func=there_and_back,
            run_time=8
        )
        self.wait(2)

# manim -pqh 费马点模型.py MathSymbolsScene -r 1920,1080 
