from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class ConeVolumeProof(Scene):
    def construct(self):
        
        # 创建坐标系 - 移除 scale(0.9)
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 6, 1],
            x_length=7,
            y_length=7,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False
        ).set_aspect_ratio(1.0).shift(DOWN*0.5)  # 向下移动0.5单位使整体居中
        
        # 添加坐标标签
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        # origin_label = Tex("O", font_size=24).next_to(axes.c2p(0,0), DL, SMALL_BUFF)
        
        # 固定点B
        B_point = axes.c2p(0, 3)
        B_dot = Dot(B_point, color=YELLOW)
        B_label = Tex("B(0,3)", font_size=28, color=YELLOW).next_to(B_dot, LEFT, buff=0.1)
        
        # 值跟踪器控制点C的x坐标（仅正半轴）
        c_tracker = ValueTracker(0.5)
        
        # 点C（在x轴正半轴上移动）
        def get_C():
            c = c_tracker.get_value()
            return axes.c2p(c, 0)
        
        C_dot = Dot(color=RED).add_updater(lambda d: d.move_to(get_C()))
        C_label = Tex("C", font_size=28).add_updater(
            lambda m: m.next_to(C_dot, DOWN, buff=0.1))
        
        # 点A（由几何条件决定）
        def get_A():
            c = c_tracker.get_value()
            # 计算点A坐标的公式
            x_a = 30 / (c**2 + 9)
            y_a = 3 + (10 * c) / (c**2 + 9)
            return axes.c2p(x_a, y_a)
        
        A_dot = Dot(color=GREEN).add_updater(lambda d: d.move_to(get_A()))
        A_label = Tex("A", font_size=28).add_updater(
            lambda m: m.next_to(A_dot, UP, buff=0.1))
        
        # 三角形ABC
        triangle = always_redraw(lambda: Polygon(
            get_A(), B_point, get_C(),
            color=BLUE, fill_opacity=0.3, stroke_width=2
        ))
        
        # AB和BC边
        AB_line = always_redraw(lambda: Line(B_point, get_A(), color=YELLOW))
        BC_line = always_redraw(lambda: Line(B_point, get_C(), color=YELLOW))
        
        # 添加线段OA（从原点O到点A）
        OA_line = always_redraw(lambda: Line(axes.c2p(0,0), get_A(), 
                                            color=PURPLE, stroke_width=2))
        
        # 添加点O
        O_dot = Dot(axes.c2p(0,0), color=WHITE)
        O_label = Tex("O", font_size=24).next_to(axes.c2p(0,0), UL, buff=0.1)
        
        # 添加线段标签
        OA_label = Tex("OA", font_size=22, color=PURPLE).next_to(OA_line, UP, buff=0.1)
        OA_label.add_updater(lambda m: m.next_to(OA_line, UP, buff=0.1))
        
        # 标题 - 调整字体大小
        title = Tex(r"直角$\triangle ABC$，$\angle ABC=90^\circ$，面积$=5$", 
                   font_size=36, color=YELLOW)
        title.next_to(axes,UP,buff=1.5)
        
        # 添加所有元素
        self.add(axes, x_label, y_label)
        self.add(B_dot, B_label, C_dot, C_label, A_dot, A_label)
        self.add(O_dot, O_label)
        self.add(triangle, AB_line, BC_line, OA_line)
        self.add(OA_label)
        self.add(title)
        
        # 点C的运动轨迹
        c_trajectory = TracedPath(C_dot.get_center, stroke_color=RED, stroke_width=2)
        self.add(c_trajectory)
        
        # 点A的运动轨迹
        a_trajectory = TracedPath(A_dot.get_center, stroke_color=GREEN, stroke_width=2)
        self.add(a_trajectory)
        
        # 动画序列：点C在正半轴运动
        self.play(
            c_tracker.animate.set_value(5),
            run_time=8,
            rate_func=linear
        )
        self.wait(2)
        
        # 快速返回动画
        self.play(
            c_tracker.animate.set_value(0.5),
            run_time=6,
            rate_func=linear
        )
        self.wait(2)

# 运行命令: manim -p 反演变换.py ConeVolumeProof