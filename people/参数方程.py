from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np

class ParametricSpiral(Scene):
    def construct(self):
        # 定义参数方程
        def parametric_curve(t):
            a, b, c = 1, 6, 14  # 可以调整这些参数获得不同效果
            x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
            y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3
            return np.array([x, y, 0])
        
        # 创建曲线
        curve = ParametricFunction(
            parametric_curve,
            t_range=[0, 2*PI],
            color=BLUE,
            stroke_width=3
        ).scale(2)
        
        # 添加标题
        title = Tex(r"参数方程螺旋线", font_size=48)
        title.to_edge(UP)
        
        # 显示方程
        equation = MathTex(
            r"x(t) &= \cos(at) + \frac{\cos(bt)}{2} + \frac{\sin(ct)}{3} \\",
            r"y(t) &= \sin(at) + \frac{\sin(bt)}{2} + \frac{\cos(ct)}{3}",
            font_size=36
        )
        equation.next_to(title, DOWN, buff=0.5)
        
        # 添加参数值
        params = Tex(r"$a=1,\ b=6,\ c=14$", font_size=32)
        params.next_to(equation, DOWN, buff=0.3)
        
        # 动画序列
        self.play(Write(title))
        self.play(Write(equation))
        self.play(Write(params))
        self.wait(1)
        
        # 绘制曲线
        self.play(Create(curve), run_time=5)
        self.wait(2)
        
        # 添加追踪点
        dot = Dot(color=RED).scale(0.7)
        dot.move_to(curve.get_start())
        
        # 添加轨迹
        trajectory = VMobject()
        trajectory.set_points_as_corners([dot.get_center(), dot.get_center()])
        trajectory.set_stroke(RED, 2, opacity=0.8)
        
        # 动画追踪点
        self.add(dot, trajectory)
        self.play(
            MoveAlongPath(dot, curve, rate_func=linear),
            UpdateFromFunc(
                trajectory,
                lambda m: m.append_points([dot.get_center()])
            ),
            run_time=8
        )
        self.wait(3)

# 运行命令: manim -pqh 参数方程.py ParametricSpiral -r 1080,1920