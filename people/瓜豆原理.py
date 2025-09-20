from manim import *
import numpy as np

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CircularMotionAnimation(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 坐标系配置
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 6, 1],
            x_length=9,
            y_length=8,
            axis_config={"color": "#ECEFF1", "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y")) 
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        tex = Tex(r"点A在圆上运动", color=YELLOW).next_to(axes, UP, buff=1.5)
        
        # 固定点C在(0,2)
        C = Dot(axes.c2p(0,2), color=RED)
        C_label = MathTex("C").next_to(C, LEFT, buff=0.1)
        
        # 圆的半径
        circle_radius = 2
        # 绘制圆轨迹
        circle = Circle(radius=circle_radius, color=WHITE, stroke_width=2).move_to(C.get_center())
        circle.set_style(stroke_opacity=0.3)
        
        # 初始点A在圆上
        initial_angle = 0
        initial_A = self.point_on_circle(initial_angle, circle_radius, C.get_center())
        A = Dot(axes.c2p(*initial_A), color=GREEN)
        A_label = MathTex("A").next_to(A, UP, buff=0.1)
        
        # 线段（使用always_redraw确保动态更新）
        AC_line = always_redraw(lambda: Line(C.get_center(), A.get_center(), color=YELLOW))
        OA_line = always_redraw(lambda: Line(origin_point, A.get_center(), color=RED))
        
        # 显示OA长度的文本
        oa_length_text = always_redraw(lambda: 
            Tex(f"OA = {np.linalg.norm(A.get_center() - origin_point):.2f}", 
                color=RED).next_to(OA_line, RIGHT, buff=0.3))
        
        # 添加所有元素到场景
        self.add(axes, origin_dot, axis_labels, origin_label, tex)
        self.add(C, C_label)
        self.add(A, A_label)
        self.add(AC_line, OA_line)
        self.add(circle)
        self.add(oa_length_text)
        
        # 点A位置更新函数（在圆上运动）
        def update_A(mob, alpha):
            angle = 2 * PI * alpha  # 从0到2π
            x, y = self.point_on_circle(angle, circle_radius, C.get_center())
            mob.move_to(axes.c2p(x, y))
        
        # 标签位置更新函数
        def update_A_label(mob):
            mob.next_to(A, UP, buff=0.1)
        
        # 添加更新器
        A_label.add_updater(update_A_label)
        
        # 创建轨迹路径
        trace = TracedPath(A.get_center, stroke_color=GREEN, stroke_width=4)
        self.add(trace)
        
        # 点A在圆上运动的动画
        self.play(
            UpdateFromAlphaFunc(A, update_A),
            rate_func=linear,
            run_time=10
        )
        
        self.wait(2)
    
    def point_on_circle(self, angle, radius, center):
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        return (x, y)

# 运行命令: manim -pqh 瓜豆原理.py CircularMotionAnimation