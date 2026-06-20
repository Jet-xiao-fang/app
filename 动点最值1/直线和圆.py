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
        titile = Tex("求$PA-PB$的最大值?",color=YELLOW,font_size=56).next_to(axes,UP,buff = 1)
        self.add(titile)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point)
        origin_label = MathTex("O").next_to(origin_dot, DR, buff=0.1)
        
        # 点C(0,-2)
        C_coords = (0, -2)
        C_point = Dot(axes.c2p(*C_coords), color=RED)
        Label_C = MathTex("C").next_to(C_point, LEFT+UP, buff=0.1)
        
        # 点A(0,-2)
        A_coords = (-2, -2)
        A_point = Dot(axes.c2p(*A_coords), color=RED)
        Label_A = MathTex("A").next_to(A_point, DOWN, buff=0.1)
        
        # 点B(0,-2)
        B_coords = (2, -2)
        B_point = Dot(axes.c2p(*B_coords), color=RED)
        Label_B = MathTex("B").next_to(B_point, DOWN, buff=0.1)
        
        Line_AB = Line(A_point.get_center(), B_point.get_center(), color=YELLOW, stroke_width=4)
        Label_AB = MathTex(r"2\sqrt{3}", font_size=26).next_to(Line_AB, DOWN, buff=0.1)
        
        # 圆（圆心在原点，半径1）
        circle = Circle(
            radius=1,
            color=BLUE_C,
            stroke_width=4
        ).move_to(axes.c2p(0, 0)).scale(2)
        
        # 点P在圆上运动，连接直线AP和BP
        
        # 2. 创建点P，初始放在圆的起始位置（最右侧）
        point = Dot(color=RED, point=circle.point_from_proportion(0))
        point_label = Text("P", color=RED).next_to(point, UR, buff=0.1)
        
        trace = TracedPath(point.get_center, stroke_color=RED, stroke_width=2,dissipating_time=0.1)
        
        self.add(axes, axis_labels, origin_dot,
                 origin_label, C_point, Label_C, circle, point, point_label, trace)
        
        self.play(Create(Line_AB), Create(A_point), Create(B_point), Create(Label_A), Create(Label_B),
                  Create(Label_AB))
        
        # 3. 创建一个值跟踪器，用于控制点在圆上的进度
        # 它的值从0开始
        theta_tracker = ValueTracker(0)

        # 4. 为点P添加更新函数
        # 这个函数会在每一帧被调用，根据theta_tracker的值更新点的位置
        def update_point(mob):
            # 从ValueTracker中获取当前进度值
            # 这里乘以2表示让点运动两圈
            progress = theta_tracker.get_value()
            # 计算点在圆上的新位置
            new_point = circle.point_from_proportion(progress % 1)
            mob.move_to(new_point)
            # 同时更新标签的位置，使其始终跟在点旁边
            point_label.next_to(mob, UR, buff=0.1)
            
        line_ap = always_redraw(lambda: DashedLine(A_point.get_center(),
                                             point.get_center(), color=GREEN, stroke_width=4))
        line_bp = always_redraw(lambda: DashedLine(B_point.get_center(),
                                             point.get_center(), color=ORANGE, stroke_width=4))
        self.add(line_ap, line_bp)
        point.add_updater(update_point)
        
        # 5. 播放动画：让ValueTracker的值从0变化到2
        # 这会让点沿着圆运动两圈
        self.play(theta_tracker.animate.set_value(2), run_time=10, rate_func=linear)
        
        self.wait(3)
        



# manim -p 直线和圆.py ParabolaPlot