from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class DynamicLineChart(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        a = Dot(point=LEFT*2)
        b = Dot(point=RIGHT*2)
        o = Dot(point=ORIGIN)
        line_ab = Line(start=a.get_center(),end=b.get_center(),color=BLUE,stroke_width = 3)
        label_A = Tex("A").next_to(a, LEFT,buff=0.1).scale(0.5)
        label_B = Tex("B").next_to(b, RIGHT,buff=0.1).scale(0.5)
        label_O = Tex("O").next_to(o,DOWN,buff=0.1).scale(0.5)
        
        self.add(a,b,o,line_ab,label_A,label_B,label_O)
        
        circle = Circle(
            radius=1,
            color=ORANGE
        )
        self.add(circle)
        
        p = Dot(point=circle.point_at_angle(45 * DEGREES),color=RED)
        label_p = always_redraw(lambda: Tex("P").next_to(p,DOWN,buff=0.05).scale(0.5))
        
        self.add(p,label_p)
        
        def get_c_position(p_pos):
            b_pos = b.get_center()
            pb_vector = b_pos - p_pos
            # 旋转90度得到PC向量（顺时针或逆时针都可以）
            pc_vector = np.array([-pb_vector[1], pb_vector[0], 0])  # 旋转90度
            c_pos = p_pos + pc_vector  # 使PB=PC且垂直
            return c_pos
        
        c = always_redraw(lambda: Dot(get_c_position(p.get_center()),color=YELLOW))
        c_label = always_redraw(lambda: Tex("C").next_to(c,UP,buff=0.05).scale(0.5))
        
        triangle = always_redraw(lambda: Polygon(
            b.get_center(),
            p.get_center(),
            c.get_center(),
            color=BLUE, fill_color=BLUE, fill_opacity=0.5
        ))
        # 创建直角符号
        right_angle = always_redraw(lambda: 
            RightAngle(Line(p.get_center(), b.get_center()),
                       Line(p.get_center(), c.get_center()),
                       length=0.2,
                       color=YELLOW,
                       quadrant=(1, 1)))
        # 线段AC
        line_ac = always_redraw(lambda: Line(a.get_center(),c.get_center(),color=RED))
        self.add(c,c_label,triangle,right_angle,line_ac)
        
        self.wait(1)
        # 创建上半圆（0到180度）
        upper_half_circle = Arc(
            radius=1,
            start_angle=0,
            angle=PI,  # 180度
            color=ORANGE
        )
        self.play(
            MoveAlongPath(p,upper_half_circle),
            run_time=12,
            rate_func=there_and_back
        )
        self.wait(2)
        

# 运行命令: 
# manim -pqh 圆与三角.py DynamicLineChart -r 1920,1080