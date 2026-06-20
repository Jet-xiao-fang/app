from manim import *
import numpy as np

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=8,
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-3, 3, 0.5],
            y_range=[-4, 4, 0.5],
            x_length=6,
            y_length=8,
            background_line_style={
                "stroke_color": "#546E7A",
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={"color": "#ECEFF1"},
        )
                
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point)
        origin_label = MathTex("O").next_to(origin_dot, DR, buff=0.1)
        titile = Tex("求$CD$的最大值?",color=YELLOW,font_size=56).next_to(axes,UP,buff = 1)
        self.add(titile)
        # 大圆（圆心在原点，半径2）
        circle = Circle(
            radius=2,
            color=BLUE,
            stroke_width=4
        ).move_to(axes.c2p(0, 0))
        
        # 半圆（圆心在(1,0)，半径1，上半部分）
        semicircle = Arc(
            radius=1,
            angle=PI,
            color=RED,
            stroke_width=4,
            arc_center=axes.c2p(1, 0)
        )
        
        # A和B是半圆的直径端点
        A_point = axes.c2p(-2, 0)
        B_point = axes.c2p(2, 0)
        A_dot = Dot(A_point, color=YELLOW)
        B_dot = Dot(B_point, color=YELLOW)
        A_label = MathTex("A").next_to(A_dot, DL, buff=0.1)
        B_label = MathTex("B").next_to(B_dot, DR, buff=0.1)
        
        # 点C和D（初始在(0,0)和(0,-2)）
        C_dot = Dot(axes.c2p(0, 0), color=GREEN)
        D_dot = Dot(axes.c2p(0, -2), color=PURPLE)
        C_label = MathTex("C").next_to(C_dot, UR, buff=0.1)
        D_label = MathTex("D").next_to(D_dot, DR, buff=0.1)
        
        # 位置函数
        def get_C_pos(theta):
            x = 1 + np.cos(theta)
            y = np.sin(theta)
            return axes.c2p(x, y)
        
        def get_D_pos(theta):
            x = 1 + np.cos(theta)
            y = -np.sqrt(4 - x**2)
            return axes.c2p(x, y)
        
        theta_tracker = ValueTracker(np.pi)  # 初始 C 在 (0,0)
        
        # ======= 使用 always_redraw 创建动态虚线 CD =======
        def get_CD_line():
            # 直接用 DashedLine，传入正确的参数
            return DashedLine(
                start=get_C_pos(theta_tracker.get_value()),
                end=get_D_pos(theta_tracker.get_value()),
                color=GREEN,
                stroke_width=3
            )
        CD_line = always_redraw(get_CD_line)
        # =================================================
        
        # 添加所有元素
        self.add(axes, axis_labels, origin_dot, origin_label,
                 circle, semicircle, A_dot, B_dot, A_label, B_label,
                 C_dot, D_dot, C_label, D_label, CD_line)
        self.bring_to_front(CD_line)
        
        self.wait(0.5)
        
        # 为点 C、D 及其标签添加更新器
        C_dot.add_updater(lambda m: m.move_to(get_C_pos(theta_tracker.get_value())))
        D_dot.add_updater(lambda m: m.move_to(get_D_pos(theta_tracker.get_value())))
        C_label.add_updater(lambda m: m.next_to(get_C_pos(theta_tracker.get_value()), UR, buff=0.1))
        D_label.add_updater(lambda m: m.next_to(get_D_pos(theta_tracker.get_value()), DR, buff=0.1))
        
        # 正向：从 (0,0) 到 (2,0)
        self.play(theta_tracker.animate.set_value(0), run_time=6, rate_func=linear)
        # 反向：从 (2,0) 回到 (0,0)
        self.play(theta_tracker.animate.set_value(np.pi), run_time=6, rate_func=linear)
        
        self.wait(1)
        
        # 清除更新器（CD_line 由 always_redraw 管理，无需清除）
        C_dot.clear_updaters()
        D_dot.clear_updaters()
        C_label.clear_updaters()
        D_label.clear_updaters()
        # 若需要停止 CD_line 的更新，可执行 self.remove(CD_line)
        
        self.wait(2)