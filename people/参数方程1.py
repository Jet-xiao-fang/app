from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class DynamicParametricSpiral(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 定义参数方程
        def parametric_curve(t,k):
            # a, c = 1, 0
            x = (k-1)*np.cos(t) + np.cos(k*t-t) 
            y = (k-1)*np.sin(t) - np.sin(k*t-t)
            return np.array([x, y, 0])
        
        # 创建可跟踪的a,b,c值变量
        k_value = Variable(1, MathTex("k"), num_decimal_places=0)
        
        # 标题和方程
        title = Tex(r"参数方程螺旋线", font_size=48,color=YELLOW).to_edge(UP,buff=1.5)
        equation = MathTex(
            r"x(t) &= \left(k-1\right)\cos(t)+\cos(kt-t) \\",
            r"y(t) &= \left(k-1\right)\sin(t)-\sin(kt-1)",
            font_size=36
        ).next_to(title, DOWN, buff=0.5)
        
        # 动态显示参数（直接更新b值）
        params = always_redraw(
            lambda: MathTex(
                f"k={int(k_value.tracker.get_value())}", 
                font_size=40,
                color=RED
            ).next_to(equation, DOWN, buff=0.3)
        )
         # 创建曲线
        curve = always_redraw(
            lambda: ParametricFunction(
                lambda t: parametric_curve(t, k_value.tracker.get_value()),
                t_range=[0, 2*PI],
                color=BLUE,
                stroke_width=3
            ).scale(0.5).shift(DOWN * 1)
        )
        # 动画序列
        self.play(Write(title), Write(equation))
        self.add(params)  # 直接添加动态params
        self.wait(0.5)
        self.play(Create(curve), run_time=1)
        self.play(
            k_value.tracker.animate.set_value(-3),
            rate_func=linear,
            run_time=4
        )
        self.wait(2)

# 运行命令: manim -pqh 参数方程1.py DynamicParametricSpiral -r 1080,1920