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
        self.camera.background_color = "#0F0F1A"
        
        # 创建坐标系 - 移除 scale(0.9)
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-1, 7, 1],
            x_length=7,
            y_length=8,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False
        ).set_aspect_ratio(1.0)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y")) 
        o = Dot(axes.c2p(0,0))
        label_O = Tex("O").next_to(o,DL,buff=0.1).scale(0.5)
        titile = Tex(r"求$BP^2+CP^2$的最小值？",color=YELLOW).next_to(axes,UP,buff = 1.5)
        # 固定点B
        C_point = axes.c2p(0, 4)
        C_dot = Dot(C_point, color=RED)
        C_label = Tex("C", font_size=32).next_to(C_dot, LEFT, buff=0.1)
        self.add(axes,axis_labels,C_dot,C_label,o,label_O,titile)
       
        B_point = axes.c2p(4, 0)
        B_dot = Dot(B_point, color=RED)
        B_label = Tex("B", font_size=32).next_to(B_dot, DOWN, buff=0.1)

        D_point = axes.c2p(3, 4)
        D_dot = Dot(D_point, color=RED)
        D_label = Tex("D", font_size=28).next_to(D_point, LEFT, buff=0.1)

        self.add(B_dot,B_label,D_dot,D_label)

        def parabola(x):
            return -x**2 + 3*x + 4
            
        graph = axes.plot(
            parabola, 
            color=GREEN, 
            stroke_width=4,
            x_range=[-1.2, 4.2]  # 限制x范围以确保曲线在y值域内
        )
        graph_label = axes.get_graph_label(
            graph, 
            label=Tex('$y=-x^{2}+3x+4$'), 
            direction=UR,
            x_val = 1.5,
            buff = 0.1,
            dot = False
        ).set_color(PINK).scale(0.8)
        
        
        
        circle = Circle(
            radius=1,
            stroke_width = 3,
            color=ORANGE
        ).move_to(D_point)
        
        self.add(graph_label,graph,circle)
        
        # P_dot = Dot(color=RED).move_to(circle.point_at_angle(90 * DEGREES)) 
        P_dot = Dot(
            color=RED,
            radius=0.08
        ).move_to(circle.point_at_angle(90 * DEGREES))
        
        P_label = always_redraw(lambda: Tex("P", font_size=28, color=YELLOW).next_to(P_dot, RIGHT, buff=0.1))
        # 跟踪点的轨迹
        traced_path = TracedPath(P_dot.get_center, stroke_color=YELLOW,stroke_width=2, dissipating_time=0.2)
        self.add(P_dot,P_label,traced_path)
        
        line_cp=always_redraw(lambda: Line(C_dot.get_center(),P_dot.get_center(),stroke_width=5,color=BLUE))
        line_bp=always_redraw(lambda: Line(B_dot.get_center(),P_dot.get_center(),stroke_width=5,color=BLUE))
        self.play(Write(line_cp),Write(line_bp),run_time=2)
        self.play(
            Rotating(
                P_dot,
                radians=2 * PI,  # 旋转360度（一圈）
                about_point=circle.get_center(),  # 围绕圆心旋转
                run_time=5,
                rate_func=linear
            )
        )
        self.play(
            Rotating(
                P_dot,
                radians=2 * PI,  # 再旋转一圈
                about_point=circle.get_center(),
                run_time=5,
                rate_func=linear
            )
        )
        self.wait(3)

# 运行命令: manim -pqh --format=png 9月13日.py ConeVolumeProof -r 1080,1920