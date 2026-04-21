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
        title = Tex("求$EP+PC$的最小值？", color=YELLOW).next_to(rectangle, UP, buff=3)
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)   # 左上 (D)
        ]
        self.add(title)
        
        # 标记矩形顶点
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
        
        # 添加尺寸标注
        length_label = Text("6", color=YELLOW, font_size=20)
        length_label.next_to(rectangle, DOWN, buff=0.2)

        width_label = Text("4", color=YELLOW, font_size=20)
        width_label.next_to(rectangle, RIGHT, buff=0.2)

        self.add(length_label, width_label)
        self.add(rectangle, *dots, *texts)

        # 创建圆（以D点为圆心）
        circle = Circle(
            radius=2, 
            color=GREEN,
            fill_opacity=0.3,
            fill_color=GREEN
        ).scale(0.8)
        circle.move_to(rectangle.get_corner(UL))
        self.add(circle)
        
        # 计算AD中点（点E的初始位置）
        ad_mid = (corners[0] + corners[3]) / 2
        e_dot = Dot(ad_mid, color=YELLOW)
        e_label = Text("E", color=WHITE, font_size=24).next_to(e_dot, LEFT, buff=0.1)
        self.add(e_dot, e_label)
        
        # 创建点P（初始在A点）
        p_dot = Dot(corners[0], color=PINK)
        p_label = Text("P", color=WHITE, font_size=24).next_to(p_dot, DOWN, buff=0.1)
        self.add(p_dot, p_label)
        
        # 创建PE和PC线段
        pe_line = Line(p_dot.get_center(), e_dot.get_center(), color=YELLOW)
        pc_line = Line(p_dot.get_center(), corners[2], color=ORANGE)  # C点
        
        # 添加轨迹跟踪
        pe_trace = TracedPath(e_dot.get_center, stroke_color=YELLOW, stroke_width=2, stroke_opacity=0.5)
        pc_trace = TracedPath(p_dot.get_center, stroke_color=ORANGE, stroke_width=2, stroke_opacity=0.5)
        
        # 添加所有元素
        self.add(pe_line, pc_line, pe_trace, pc_trace)
        
        # 创建角度跟踪器（控制E点在圆上的位置）
        angle_tracker = ValueTracker(3*PI/2)  # 从下方开始（270度）
        
        # 创建位置跟踪器（控制P点在AB边上的位置）
        pos_tracker = ValueTracker(0)
        
        # 更新点E的位置（圆周运动）
        e_dot.add_updater(lambda m: m.move_to(
            circle.get_center() + np.array([
                1.6 * np.cos(angle_tracker.get_value()), 
                1.6 * np.sin(angle_tracker.get_value()), 
                0
            ])
        ))
        e_label.add_updater(lambda m: m.next_to(e_dot, LEFT, buff=0.1))
        
        # 更新点P的位置（在AB边上移动）
        p_dot.add_updater(lambda m: m.move_to(
            interpolate(corners[0], corners[1], pos_tracker.get_value())
        ))
        p_label.add_updater(lambda m: m.next_to(p_dot, DOWN, buff=0.1))
        
        # 更新PE线段
        pe_line.add_updater(lambda m: m.become(
            Line(p_dot.get_center(), e_dot.get_center(), color=YELLOW)
        ))
        
        # 更新PC线段
        pc_line.add_updater(lambda m: m.become(
            Line(p_dot.get_center(), corners[2], color=ORANGE)
        ))
        
        # 动画序列
        self.wait(1)
        
        # 点E圆周运动，点P同时移动
        self.play(
            angle_tracker.animate.set_value(3*PI/2 + 2*PI),
            pos_tracker.animate.set_value(1),
            run_time=8,
            rate_func=linear
        )
        
        # 点E继续运动，点P返回
        self.play(
            angle_tracker.animate.set_value(3*PI/2 + 4*PI),
            pos_tracker.animate.set_value(0),
            run_time=8,
            rate_func=linear
        )
        
        # 最终展示
        self.wait(3)


# manim -p 正方形与2动点.py MathSymbolsScene
