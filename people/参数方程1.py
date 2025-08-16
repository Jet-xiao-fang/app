from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np

class DynamicParametricSpiral(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 固定参数
        a = 1
        c = 0
        # 参数显示
        b_value = Variable(20, MathTex("b"), num_decimal_places=0)

        # 初始曲线
        def parametric_curve(t, b=20):
            x = np.cos(a*t) + np.cos(b*t)/2
            y = np.sin(a*t) + np.sin(b*t)/2
            return np.array([x, y, 0])
        
        curve = always_redraw(
            lambda: ParametricFunction(
                lambda t: parametric_curve(t, b_value.tracker.get_value()),
                t_range=[0, 2*PI],
                color=BLUE,
                stroke_width=3
            ).scale(2)
        )
        
        self.play(Create(curve), run_time=1)
        # 动态变化b值
        self.play(
            b_value.tracker.animate.set_value(60),
            rate_func=linear,
            run_time=6
        )
        
        # 添加追踪点
        # dot = Dot(color=RED).scale(0.7)
        # dot.move_to(curve.get_start())
        
        # # 添加轨迹
        # trajectory = VMobject()
        # trajectory.set_points_as_corners([dot.get_center(), dot.get_center()])
        # trajectory.set_stroke(RED, 2, opacity=0.8)
        
        # # 动画追踪点
        # self.add(dot, trajectory)
        # self.play(
        #     MoveAlongPath(dot, curve, rate_func=linear),
        #     UpdateFromFunc(
        #         trajectory,
        #         lambda m: m.append_points([dot.get_center()])
        #     ),
        #     run_time=8
        # )

# 运行命令: manim -pqh 参数方程1.py DynamicParametricSpiral -r 1920,1080