from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080

class ConeVolumeProof(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0B1A"
        # 创建坐标系 - 移除 scale(0.9)
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 5, 1],
            x_length=7,
            y_length=6,
            axis_config={"color": WHITE, "stroke_width": 3},
            tips=False
        ).set_aspect_ratio(1.0)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y")) 
        o = Dot(axes.c2p(0,0))
        label_O = Tex("O").next_to(o,DL,buff=0.1).scale(0.5)
        titile = Tex(r"求$OC+BC$的最小值？",color=YELLOW).next_to(axes,UP,buff = 1.5)
        # 固定点B
        C_point = axes.c2p(0, 3)
        C_dot = Dot(C_point, color=YELLOW)
        C_label = Tex("B(0,3)", font_size=28, color=YELLOW).next_to(C_dot, LEFT, buff=0.1)
        self.add(axes,axis_labels,C_dot,C_label,o,label_O,titile)
       
        # 点C（在x轴正半轴上移动）
        # 创建一个点，初始位置在 x = -3, y = 0
        dot = Dot(axes.c2p(0.5, 0), color=YELLOW)
        A_label = always_redraw(lambda: Tex("A", font_size=28, color=YELLOW).next_to(dot, DOWN, buff=0.1))
        self.add(dot,A_label)
        
        def get_b_position(a_pos):
            c_dot = C_dot.get_center()
            ac_vector = c_dot - a_pos
            # 旋转90度得到PC向量（顺时针或逆时针都可以）
            ab_vector = np.array([-ac_vector[1], ac_vector[0], 0])  # 旋转90度
            b_pos = a_pos - ab_vector  # 使PB=PC且垂直
            return b_pos
        c = always_redraw(lambda: Dot(get_b_position(dot.get_center()),color=YELLOW))
        c_label = always_redraw(lambda: Tex("C").next_to(c,UP,buff=0.05).scale(0.5))
        
        triangle = always_redraw(lambda: Polygon(
            C_dot.get_center(),
            dot.get_center(),
            c.get_center(),
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.5
        ))
        # 创建直角符号
        right_angle = always_redraw(lambda: 
            RightAngle(Line(dot.get_center(), C_dot.get_center()),
                       Line(dot.get_center(), c.get_center()),
                       length=0.2,
                       color=YELLOW,
                       quadrant=(1, 1)))
         # 线段AC
        line_ac = always_redraw(lambda: Line(o.get_center(),c.get_center()))
        self.add(c,c_label,triangle,right_angle,line_ac)
        self.wait(0.5)
        # 让点沿着x轴从 -3 移动到 3
        self.play(
            dot.animate.move_to(axes.c2p(3, 0)),
            run_time=6,  # 动画时长为3秒
            rate_func=linear  # 匀速运动
        )
        self.play(
            dot.animate.move_to(axes.c2p(0.5, 0)),
            run_time=6,  # 动画时长为3秒
            rate_func=linear  # 匀速运动
        )
        
        self.wait(3)

# 运行命令: manim -p 三角形移动.py ConeVolumeProof