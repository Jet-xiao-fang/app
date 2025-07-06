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
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        
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
        origin_label = Tex("O", font_size=24).next_to(axes.c2p(0,0), DL, SMALL_BUFF)
        
        # 添加点A(0,1)和点B(3,2)
        A = Dot(axes.c2p(0,1), color=YELLOW, radius=0.08)
        B = Dot(axes.c2p(3,2), color=YELLOW, radius=0.08)
        A_label = Tex("A(0,1)", font_size=28, color=YELLOW).next_to(A, LEFT, buff=0.1)
        B_label = Tex("B(3,2)", font_size=28, color=YELLOW).next_to(B, UR, buff=0.1)
        
        # 创建动点P及其轨迹
        P_tracker = ValueTracker(0.5)  # 初始x位置
        P = always_redraw(lambda: Dot(
            axes.c2p(P_tracker.get_value(), 0),
            color=RED,
            radius=0.08
        ))
        P_label = always_redraw(lambda: Tex("P", font_size=28, color=RED)
            .next_to(P.get_center(), DOWN, buff=0.1))
        
        # 创建动态线段AP和BP
        AP = always_redraw(lambda: Line(
            A.get_center(),
            P.get_center(),
            color=BLUE_B,
            stroke_width=3
        ))
        BP = always_redraw(lambda: Line(
            B.get_center(),
            P.get_center(),
            color=GREEN_B,
            stroke_width=3
        ))
        
        # 添加坐标说明
        # coord_desc = VGroup(
        #     Tex("动点P在x正半轴上运动", font_size=32, color=RED),
        #     Tex("连接AP和BP", font_size=32, color=BLUE)
        # ).arrange(DOWN, buff=0.3).to_edge(UP, buff=0.5)
        title = Tex(r"求$PA+2PB$的最小值？", 
                   font_size=48, color=RED)
        title.next_to(axes,UP,buff=1.5)
        
        # 添加所有元素到场景
        self.add(axes, x_label, y_label, origin_label)
        self.add(A, B, A_label, B_label)
        self.add(AP, BP, P, P_label)
        self.add(title)
        
        # 添加动画效果
        self.wait(1)
        
        # P点移动动画
        self.play(
            P_tracker.animate.set_value(5),
            rate_func=there_and_back,
            run_time=8
        )
        
        # 特殊位置演示
        special_points = [1.0, 2.0, 4.0]
        for x in special_points:
            self.play(
                P_tracker.animate.set_value(x),
                run_time=1.5
            )
            self.wait(0.5)
        
        # 回到初始位置
        self.play(
            P_tracker.animate.set_value(0.5),
            run_time=1.5
        )
        
        self.wait(2)
        
# 运行命令: manim -pqh --format=png 两个定点.py ConeVolumeProof -r 1920,1080