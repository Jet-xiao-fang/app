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
        
        # 创建正方形
        rectangle = Rectangle(width=6, height=6, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.5)
        title = Tex("求$BP$的最小值？", color=YELLOW).next_to(rectangle, UP, buff=0.8)
        self.add(title)
        
        # 获取正方形的四个角
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)   # 左上 (D)
        ]
        
        # 标记正方形的四个顶点
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
        
        # 显示边长标签
        side_label = Tex("6", color=YELLOW, font_size=30)
        side_label.next_to(rectangle, DOWN, buff=0.2)
        
        # 添加所有元素到场景
        self.add(rectangle, *dots, *texts, side_label)
        self.wait(1)
        
        # 计算圆心（AD的中点）
        center = (corners[0] + corners[3]) / 2
        radius = 3  # AD的长度是6，所以半径是3
        
        # 创建点P（起始位置在45度）
        start_angle = PI/4  # 45度
        p_dot = Dot(color=PURPLE, radius=0.08)
        p_dot.move_to(center + radius * np.array([np.cos(start_angle), np.sin(start_angle), 0]))
        
        # 创建点P的标签并设置为动态更新
        p_label = Tex("P", color=WHITE, font_size=30)
        p_label.add_updater(lambda m: m.next_to(p_dot, UR, buff=0.1))
        
        # 创建线段AP、DP、BP
        ap_line = always_redraw(lambda: Line(corners[0], p_dot.get_center(), color=GREEN))
        dp_line = always_redraw(lambda: Line(corners[3], p_dot.get_center(), color=GREEN))
        bp_line = always_redraw(lambda: Line(corners[1], p_dot.get_center(), color=RED))
        
        # 创建半圆（右半圆）
        semicircle = Arc(
            radius=radius,
            start_angle=-PI/2,
            angle=PI,
            arc_center=center,
            color=YELLOW
        )
        
        self.play(
            Create(p_dot),
            Write(p_label),
            Create(ap_line),
            Create(dp_line)
        )
        self.wait(1)
        
        self.play(Create(bp_line))
        self.wait(1)
        
        # 新轨迹函数（从45°到-45°来回运动）
        def semicircle_path(t):
            angle = PI/4 * np.cos(2 * PI * t)  # 在45°和-45°之间来回摆动
            return center + radius * np.array([np.cos(angle), np.sin(angle), 0])
        
        # 点P在半圆上运动
        self.play(
            MoveAlongPath(p_dot, ParametricFunction(semicircle_path, t_range=[0, 1])),
            run_time=4,
            rate_func=linear
        )
        self.play(
            MoveAlongPath(p_dot, ParametricFunction(semicircle_path, t_range=[1, 2])),
            run_time=4,
            rate_func=linear
        )
        
        self.wait(2)

# 运行命令：manim -p 正方形内一点.py MathSymbolsScene