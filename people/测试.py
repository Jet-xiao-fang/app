from manim import *
# config.frame_height = 16
# config.frame_width = 9
# config.pixel_height = 1920
# config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np
class CosTaylorApproximation(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 坐标系配置
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI/2],  # x 从 -2π 到 2π，刻度间隔 π/2
            y_range=[-1.5, 1.5, 0.5],         # y 从 -1.5 到 1.5，刻度间隔 0.5
            x_length=10,
            y_length=6,
            axis_config={"color": "#ECEFF1",
                         "stroke_width": 3,
                         "tip_length": 0.1,
                         "tip_width": 0.2},
            tips=True,  # 不显示箭头
        )
        
        my_run_time=0.5
        
        self.add(axes)
        
        #y = x²
        parabola = axes.plot(
            lambda x: x**2, 
            x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        # 添加方程标签
        equation = MathTex("y = x^2", color=ORANGE).next_to(axes, UP, buff=0.2)
        
        self.play(Create(parabola),Write(equation),run_time=my_run_time)
        
        #y = -x²
        p1 = axes.plot(
            lambda x: -x**2, 
            x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        # 添加方程标签
        e1 = MathTex("y = -x^2", color=ORANGE).next_to(axes, UP, buff=0.2)
        
        self.play(ReplacementTransform(parabola,p1),ReplacementTransform(equation,e1),run_time=my_run_time)
        
        p2 = axes.plot(
            lambda x: x,
             x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        e2 = MathTex("y = x", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p1,p2),ReplacementTransform(e1,e2),run_time=my_run_time)
        
        p3 = axes.plot(
            lambda x: np.abs(x),
             x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        e3 = MathTex(r"y = |x|", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p2,p3),ReplacementTransform(e2,e3),run_time=my_run_time)
        
        p4 = axes.plot(
            lambda x: x+1,
             x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        e4 = MathTex(r"y = x+1", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p3,p4),ReplacementTransform(e3,e4),run_time=my_run_time)
        
        
        p5 = axes.plot(
            lambda x: -x+1,
             x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        e5 = MathTex(r"y = -x+1", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p4,p5),ReplacementTransform(e4,e5),run_time=my_run_time)
        
        p6 = axes.plot(
            lambda x: -2*x+1,
             x_range=[-1.5, 1.5],
            color=WHITE,
            stroke_width=4
        )
        e6 = MathTex(r"y = -2x+2", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p5,p6),ReplacementTransform(e5,e6),run_time=my_run_time)
        
        p7 = axes.plot(
        lambda x: x ** 3,  # y = x³
        x_range=[-1.5, 1.5],  # 可调整 x 范围
        color=WHITE,
        stroke_width=4
        )
        e7 = MathTex(r"y = x^3", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p6, p7), ReplacementTransform(e6, e7),run_time=my_run_time)
        
        
        p8 = axes.plot(
        lambda x: np.sin(x),
        color=WHITE,
        stroke_width=4
        )
        e8 = MathTex(r"y = \sin(x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p7, p8), ReplacementTransform(e7, e8),run_time=my_run_time)
        
        p9 = axes.plot(
        lambda x: np.sin(x+PI/6),
        color=WHITE,
        stroke_width=4
        )
        e9 = MathTex(r"y = \sin\left(x + \frac{\pi}{6}\right)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p8, p9), ReplacementTransform(e8, e9),run_time=my_run_time)
        
        
        p10 = axes.plot(
        lambda x: np.sin(x+PI/3),
        color=WHITE,
        stroke_width=4
        )
        e10 = MathTex(r"y = \sin\left(x + \frac{\pi}{3}\right)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p9, p10), ReplacementTransform(e9, e10),run_time=my_run_time)
        
        p11 = axes.plot(
        lambda x: np.sin(x+PI/2),
        color=WHITE,
        stroke_width=4
        )
        e11 = MathTex(r"y = \sin\left(x + \frac{\pi}{2}\right)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p10, p11), ReplacementTransform(e10, e11),run_time=my_run_time)
        
        
        p12 = axes.plot(
        lambda x: np.sin(2*x),
        color=WHITE,
        stroke_width=4
        )
        e12 = MathTex(r"y = \sin(2x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        
        self.play(ReplacementTransform(p11, p12), ReplacementTransform(e11, e12),run_time=my_run_time)
        
        p13 = axes.plot(
        lambda x: np.sin(3*x),
        color=WHITE,
        stroke_width=4
        )
        e13 = MathTex(r"y = \sin(3x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p12, p13), ReplacementTransform(e12, e13),run_time=my_run_time)
        
        p14 = axes.plot(
        lambda x: np.sin(4*x),
        color=WHITE,
        stroke_width=4
        )
        e14 = MathTex(r"y = \sin(4x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p13, p14), ReplacementTransform(e13, e14),run_time=my_run_time)
        
        p15 = axes.plot(
            lambda x: np.cos(x),
            color=WHITE,
            stroke_width=4
        )
        e15 = MathTex(r"y = \cos(x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p14, p15), ReplacementTransform(e14, e15),run_time=my_run_time)

        p16 = axes.plot(
            lambda x: np.cos(x+PI/6),
            color=WHITE,
            stroke_width=4
        )
        e16 = MathTex(r"y = \cos\left(x + \frac{\pi}{6}\right)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p15, p16), ReplacementTransform(e15, e16),run_time=my_run_time)

        p17 = axes.plot(
            lambda x: np.cos(x+PI/3),
            color=WHITE,
            stroke_width=4
        )
        e17 = MathTex(r"y = \cos\left(x + \frac{\pi}{3}\right)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p16, p17), ReplacementTransform(e16, e17),run_time=my_run_time)
        
        p18 = axes.plot(
            lambda x: np.cos(x+PI/2),
            color=WHITE,
            stroke_width=4
        )
        e18 = MathTex(r"y = \cos\left(x + \frac{\pi}{2}\right)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p17, p18), ReplacementTransform(e17, e18),run_time=my_run_time)

        p19 = axes.plot(
            lambda x: np.cos(2*x),
            color=WHITE,
            stroke_width=4
        )
        e19 = MathTex(r"y = \cos(2x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p18, p19), ReplacementTransform(e18, e19),run_time=my_run_time)

        p20 = axes.plot(
            lambda x: np.cos(3*x),
            color=WHITE,
            stroke_width=4
        )
        e20 = MathTex(r"y = \cos(3x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p19, p20), ReplacementTransform(e19, e20),run_time=my_run_time)
        
        p21 = axes.plot(
            lambda x: np.cos(4*x),
            color=WHITE,
            stroke_width=4
        )
        e21 = MathTex(r"y = \cos(4x)", color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(ReplacementTransform(p20, p21), ReplacementTransform(e20, e21),run_time=my_run_time)

        

#   manim -pqh 测试.py CosTaylorApproximation -r 1920,1080