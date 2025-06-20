from manim import *
import random
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class MathCover(Scene):
    def construct(self):
       
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        # 创建标题
        title = Text("10个不定积分公式", font_size=48, color=BLUE)
        
        # 添加数学公式装饰
        formulas = VGroup(
            MathTex(r"\int e^{ax} \,dx = \frac{1}{a}e^{ax} + C", color=BLUE_C),
            MathTex(r"\int \frac{1}{x} \,dx = \ln|x| + C", color=GREEN_C),
            MathTex(r"\int \cos(ax) \,dx = \frac{1}{a}\sin(ax) + C", color=YELLOW_C),
            MathTex(r"\int \frac{1}{1+x^2} \,dx = \arctan(x) + C", color=RED_C)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        title.next_to(formula,UP,buff=1.5)
        for formula in formulas:
            formula.scale(0.8)
            formula.set_opacity(0.8)
            formula.set_stroke(width=1, color=WHITE, opacity=0.3)
        
        
        # 添加大积分符号装饰
        big_integral = MathTex(r"\int", font_size=150, color=BLUE_D)
        big_integral.set_fill(opacity=0.1)
        big_integral.set_stroke(width=1, color=BLUE_E, opacity=0.2)
        big_integral.to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)
        
        # 添加装饰性数学符号
        math_symbols = VGroup(
            MathTex(r"\infty", font_size=40, color=PURPLE_A).shift(UR * 1.5),
            MathTex(r"\sum", font_size=50, color=TEAL_A).shift(DR * 1.5),
            MathTex(r"\pi", font_size=60, color=RED_A).shift(UL * 1.5),
            MathTex(r"\partial", font_size=45, color=GOLD_A).shift(DL * 1.5)
        )
        
        
        self.play(
            FadeIn(title, shift=DOWN * 0.5),
            FadeIn(formulas, lag_ratio=0.1),
            run_time=4
        )
    

# manim -pqh --format=png 视频封面.py MathCover -r 1920,1080