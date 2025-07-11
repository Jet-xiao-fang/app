from manim import *
import numpy as np
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
        rectangle = Rectangle(width=6, height=4, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.5).scale(0.8)
        title = Tex("求$DE+DF$的最小值？", color=YELLOW).next_to(rectangle, UP, buff=1.5)
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)   # 左上 (D)
        ]
        AB = 6
        AD = 4
        AC = np.sqrt(AB**2 + AD**2)
        # 标记矩形顶点
        labels = ["A", "B", "C", "D"]
        dots = []
        texts = []
        for idx, (corner, label) in enumerate(zip(corners, labels)):
            dot = Dot(corner, color=RED)
            if idx == 0:  # A (左下)
                text = Tex(label, color=WHITE, font_size=30).next_to(dot, DL, buff=0.1)
            elif idx == 1:  # B (右下)
                text = Tex(label, color=WHITE, font_size=30).next_to(dot, DR, buff=0.1)
            elif idx == 2:  # C (右上)
                text = Tex(label, color=WHITE, font_size=30).next_to(dot, UR, buff=0.1)
            elif idx == 3:  # D (左上)
                text = Tex(label, color=WHITE, font_size=30).next_to(dot, UL, buff=0.1)

            dots.append(dot)
            texts.append(text)
        
        # 添加尺寸标注
        length_label = Tex("6", color=YELLOW, font_size=30)
        length_label.next_to(rectangle, DOWN, buff=0.2)

        width_label = Tex("4", color=YELLOW, font_size=30)
        width_label.next_to(rectangle, RIGHT, buff=0.2)

        # 添加对角线AC
        diagonal = Line(corners[0], corners[2], color=GREEN)

        # 添加初始元素
        self.add(title, rectangle, *dots, *texts, length_label, width_label, diagonal)
        self.wait(1)
        
        # 创建动点E和F
        t = ValueTracker(0)  # 参数控制器
        
        # 点E在AB上移动
        E = always_redraw(lambda: Dot(
            interpolate(corners[0], corners[1], t.get_value()),
            color=RED
        ))
        
        # 点F在AC上移动，满足AE=CF
        F = always_redraw(lambda: Dot(
            interpolate(corners[2], corners[0], (t.get_value() * AB) / AC),
            color=RED
        ))
        
        # 添加E、F标签
        E_label = always_redraw(lambda: Tex("E", color=PINK, font_size=30).next_to(E, DOWN, buff=0.1))
        F_label = always_redraw(lambda: Tex("F", color=RED, font_size=30).next_to(F, DOWN, buff=0.1))
        
        # 创建连接线
        DE = always_redraw(lambda: Line(corners[3], E.get_center(), color=YELLOW))
        DF = always_redraw(lambda: Line(corners[3], F.get_center(), color=YELLOW))
        
        # 添加所有动态元素
        self.play(
            Create(E), Create(F),
            Write(E_label), Write(F_label)
        )
        self.play(Create(DE), Create(DF))
        
        # 动画演示点移动
        self.play(
            t.animate.set_value(1),
            run_time=6,
            rate_func=linear
        )
        self.play(
            t.animate.set_value(0),
            run_time=6,
            rate_func=linear
        )
        
        # 最终展示
        self.wait(3)


# manim -pqh 逆等线.py MathSymbolsScene -r 1920,1080 
