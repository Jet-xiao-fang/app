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
        self.camera.background_color = "#0F0F1A"

        # 绘制正方形，边长 4
        square = Square(side_length=4, color=BLUE)
        square.set_fill(BLUE, opacity=0.3)
        square.move_to(ORIGIN)
        self.add(square)

        # 顶点坐标 (左下->右下->右上->左上)
        A = square.get_corner(DL)   # 左下
        B = square.get_corner(DR)   # 右下
        C = square.get_corner(UR)   # 右上
        D = square.get_corner(UL)   # 左上

        # 标注顶点
        dots = VGroup(
            Dot(A, color=RED),
            Dot(B, color=RED),
            Dot(C, color=RED),
            Dot(D, color=RED)
        )
        labels = VGroup(
            Tex("A", color=WHITE).next_to(A, DL, buff=0.15),
            Tex("B", color=WHITE).next_to(B, DR, buff=0.15),
            Tex("C", color=WHITE).next_to(C, UR, buff=0.15),
            Tex("D", color=WHITE).next_to(D, UL, buff=0.15)
        )
        
        side_label = Tex("4", color=YELLOW).next_to(square, DOWN, buff=0.2)
        title = Tex(r"求$BP$的最小值？", color=YELLOW)
        title.to_edge(UP, buff=3)
        
        self.add(square, dots, labels, side_label, title)

        # 半圆：以 AD 为直径，圆心为 AD 中点，半径 = 2
        center = (A + D) / 2          # 左边中点
        radius = 2
        
        # 绘制半圆（向右，从 D 到 A 的弧）
        # 角度从 PI/2 (90°, 即 D 点) 到 -PI/2 (-90°, 即 A 点)
        semicircle = Arc(
            radius=radius,
            start_angle=PI/2,   # 从 D 开始
            angle=-PI,          # 顺时针画 180 度到 A
            arc_center=center,
            color=YELLOW,
            stroke_width=3
        )

        # 点 P 的初始位置（D 点）
        p_dot = Dot(color=PURPLE, radius=0.08)
        p_dot.move_to(D)
        p_label = Tex("P", color=WHITE).add_updater(lambda m: m.next_to(p_dot, UR, buff=0.1))

        # 辅助线段 AP, DP, BP（动态更新）
        ap_line = always_redraw(lambda: Line(A, p_dot.get_center(), color=GREEN))
        dp_line = always_redraw(lambda: Line(D, p_dot.get_center(), color=GREEN))
        bp_line = always_redraw(lambda: Line(B, p_dot.get_center(), color=RED))

        self.play(
            Create(p_dot),
            Write(p_label),
            Create(ap_line),
            Create(dp_line)
        )
        self.wait(0.5)
        self.play(Create(bp_line))

        # 定义半圆路径参数方程（角度从 90° 到 -90°，匀速）
        def semicircle_path(t):
            angle = PI/2 - PI * t   # t=0 -> 90° (D), t=1 -> -90° (A)
            return center + radius * np.array([np.cos(angle), np.sin(angle), 0])

        # 运行动画：P 沿半圆从 D 运动到 A
        self.play(
            MoveAlongPath(
                p_dot,
                ParametricFunction(semicircle_path, t_range=[0, 1]),
                rate_func=linear
            ),
            run_time=6
        )
        
        
        self.play(
            MoveAlongPath(
                p_dot,
                ParametricFunction(lambda t: semicircle_path(1 - t), t_range=[0, 1]),
                rate_func=linear
            ),
            run_time=6
        )

        self.wait(2)
        
        # 清除所有动态对象（可选，避免退出时报错）
        self.clear()

# 运行命令：manim -p 正方形内一点.py MathSymbolsScene