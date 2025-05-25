from manim import *
import math
class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 6, 1],
            x_length=12,
            y_length=6,
            
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-6, 6, 0.5],
            y_range=[0, 6, 0.5],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1"},
            x_length=12,
            y_length=6
            
        )
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))  # 使用MathTex
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        # 创建半径为2的上半圆，圆心在原点
        semicircle = Arc(
            radius=2,          # 半径改为2
            start_angle=0,     # 从右侧开始（0弧度）
            angle=PI,          # 画180°（上半圆）
            color=RED,
            arc_center=axes.c2p(0, 0),  # 直接指定圆心坐标
            stroke_width=2
        )
        A_coords = (-2, 0)  # 数学坐标系中的坐标
        A_point = Dot(axes.c2p(*A_coords), color=RED)  # 转换到场景坐标系
        Label_A = Tex("A").next_to(A_point, DOWN, buff=0.1)
        B_coords = (2, 0)  # 数学坐标系中的坐标
        B_point = Dot(axes.c2p(*B_coords), color=RED)  # 转换到场景坐标系
        Label_B = Tex("B").next_to(B_point, DOWN, buff=0.1)

        self.add(grid, axes, axis_labels, origin_dot, origin_label,semicircle,Label_A,Label_B)

        vt = ValueTracker(-1.5)  # 初始值对应x=1

        P = always_redraw(lambda: Dot(
            axes.c2p(vt.get_value(), math.sqrt(2*2-vt.get_value()*vt.get_value())),
            color=YELLOW
        ))
        P_label = always_redraw(lambda: Tex("P").next_to(P, UP, buff=0.15))
        AP = always_redraw(lambda: DashedLine(
            A_point.get_center(), 
            P.get_center(),
            color=RED_C,
            stroke_width=2.5
        ))
        BP = always_redraw(lambda: DashedLine(
            B_point.get_center(),
            P.get_center(),
            color=BLUE_C,
            stroke_width=2.5
        ))
        self.play(
            Create(P),
            Write(P_label),
            Create(AP),
            Create(BP),
            run_time = 2
        )
         # 轨迹跟踪（网页6的抛物线绘制扩展）
        trace = TracedPath(P.get_center, dissipating_time=1, stroke_color=YELLOW)
        self.add(trace)  # 添加轨迹追踪
        # 动画控制（网页5的运动控制优化）
        self.play(
            vt.animate.set_value(1.5),  # x从1运动到4
            rate_func=linear,
            run_time=6
        )
        self.play(
            vt.animate.set_value(-1.5),  # x从1运动到4
            rate_func=linear,
            run_time=6
        )
        self.wait(2)

        
        
      
# manim -pqh 半圆.py ParabolaPlot -r 1920,1080