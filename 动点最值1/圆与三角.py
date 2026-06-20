from manim import *
import numpy as np

config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex


class DynamicLineChart(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 创建点A、B、O
        a = Dot(point=LEFT*2+DOWN*1, color=BLUE)
        b = Dot(point=RIGHT*2+DOWN*1, color=BLUE)
        o = Dot(point=ORIGIN+DOWN*1, color=BLUE)
        
        # 线段AB
        line_ab = Line(start=a.get_center(), end=b.get_center(), color=BLUE, stroke_width=3)
        
        # 标签
        label_A = Tex("A", color=WHITE).next_to(a, LEFT, buff=0.1).scale(0.5)
        label_B = Tex("B", color=WHITE).next_to(b, RIGHT, buff=0.1).scale(0.5)
        label_O = Tex("O", color=WHITE).next_to(o, DOWN, buff=0.1).scale(0.5)
        title = Tex("求$AC$的取值范围?", color=WHITE).to_edge(UP, buff=2.5)
        
        self.add(a, b, o, line_ab, label_A, label_B, label_O, title)
        
        # 圆
        circle = Circle(radius=1, color=ORANGE)
        circle.move_to(DOWN*1)
        self.add(circle)
        
        # 点P（初始位置在15度）
        p = Dot(point=circle.point_at_angle(15 * DEGREES), color=RED)
        label_p = always_redraw(lambda: Tex("P", color=WHITE).next_to(p, DOWN, buff=0.05).scale(0.5))
        
        self.add(p, label_p)
        
        # 定义C点的位置（使PB⊥PC且PB=PC）
        def get_c_position(p_pos):
            b_pos = b.get_center()
            pb_vector = b_pos - p_pos
            # 旋转90度得到PC向量
            pc_vector = np.array([-pb_vector[1], pb_vector[0], 0])
            c_pos = p_pos + pc_vector
            return c_pos
        
        # 点C及其标签
        c = always_redraw(lambda: Dot(get_c_position(p.get_center()), color=YELLOW))
        c_label = always_redraw(lambda: Tex("C", color=WHITE).next_to(c, UP, buff=0.05).scale(0.5))
        
        # 三角形PBC
        triangle = always_redraw(lambda: Polygon(
            b.get_center(),
            p.get_center(),
            c.get_center(),
            color=BLUE, fill_color=BLUE, fill_opacity=0.3
        ))
        
        # 直角符号
        right_angle = always_redraw(lambda: 
            RightAngle(
                Line(p.get_center(), b.get_center()),
                Line(p.get_center(), c.get_center()),
                length=0.2,
                color=YELLOW
            ))
        
        # 线段AC
        line_ac = always_redraw(lambda: Line(a.get_center(), c.get_center(), color=RED, stroke_width=4))
        
        self.add(c, c_label, triangle, right_angle, line_ac)
        
        # ========== 使用 ValueTracker 控制P点运动 ==========
        angle_tracker = ValueTracker(15 * DEGREES)
        
        def update_p_by_angle(mob):
            angle = angle_tracker.get_value()
            new_pos = circle.get_center() + circle.radius * np.array([np.cos(angle), np.sin(angle), 0])
            mob.move_to(new_pos)
        
        p.add_updater(update_p_by_angle)
        
        # 运动：15° -> 145° -> 15°（往返运动）
        self.play(
            angle_tracker.animate.set_value(180 * DEGREES),
            run_time=6,
            rate_func=linear
        )
        self.play(
            angle_tracker.animate.set_value(0 * DEGREES),
            run_time=6,
            rate_func=linear
        )
        
        # 可选：再运动一次
        # self.play(
        #     angle_tracker.animate.set_value(145 * DEGREES),
        #     run_time=6,
        #     rate_func=linear
        # )
        # self.play(
        #     angle_tracker.animate.set_value(15 * DEGREES),
        #     run_time=6,
        #     rate_func=linear
        # )
        
        # 清理updater
        p.clear_updaters()
        
        self.wait(3)
        
#  manim -p 圆与三角.py DynamicLineChart