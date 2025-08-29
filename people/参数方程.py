from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class ParametricSpiral(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 定义参数方程
        def parametric_curve(t,a,b,c):
            # a, c = 1, 0
            x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
            y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3
            return np.array([x, y, 0])
        
        # 创建可跟踪的a,b,c值变量
        a_value = Variable(1, MathTex("a"), num_decimal_places=0)
        b_value = Variable(1, MathTex("b"), num_decimal_places=0)
        c_value = Variable(0, MathTex("c"), num_decimal_places=0)
       
        # 标题和方程
        title = Tex(r"神奇的参数方程", font_size=48,color=YELLOW).to_edge(UP,buff=1.5)
        equation = MathTex(
            r"x(t) &= \cos(at) + \frac{\cos(bt)}{2} + \frac{\sin(ct)}{3} \\",
            r"y(t) &= \sin(at) + \frac{\sin(bt)}{2} + \frac{\cos(ct)}{3}",
            font_size=36
        ).next_to(title, DOWN, buff=0.5)
        
        # 动态显示参数（直接更新b值）
        params = always_redraw(
            lambda: MathTex(
                f"a={int(a_value.tracker.get_value())},\\ b={int(b_value.tracker.get_value())},\\ c={int(c_value.tracker.get_value())}", 
                font_size=40,
                color=RED
            ).next_to(equation, DOWN, buff=0.3)
        )
         # 创建曲线
        curve = always_redraw(
            lambda: ParametricFunction(
                lambda t: parametric_curve(t,
                                           a_value.tracker.get_value(),
                                           b_value.tracker.get_value(),
                                           c_value.tracker.get_value()),
                t_range=[0, 2*PI],
                stroke_width=3
            ).scale(1.8).shift(DOWN * 1).set_color(color=[BLUE, PURPLE, RED])
        )
        self.add(title,equation,params)
        self.wait(0.5)
        self.play(Create(curve), run_time=0.5)
        self.play(
            b_value.tracker.animate.set_value(60),
            rate_func=linear,
            run_time=6
        )
        self.play(
            b_value.tracker.animate.set_value(1),
            rate_func=linear,
            run_time=6
        )
        self.wait(0.5)
        self.play(
            a_value.tracker.animate.set_value(60),
            rate_func=linear,
            run_time=6
        )
        self.play(
            a_value.tracker.animate.set_value(1),
            rate_func=linear,
            run_time=6
        )
        self.wait(0.5)
        self.play(
            c_value.tracker.animate.set_value(60),
            rate_func=linear,
            run_time=6
        )
        self.play(
            c_value.tracker.animate.set_value(0),
            rate_func=linear,
            run_time=6
        )
        self.wait(2)
        
        
# manim -pqh 参数方程.py ParametricSpiral -r 1080,1920