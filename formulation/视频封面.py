from manim import *
import random
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_rate = 60

class MathCover(Scene):
    def construct(self):
       
        # 创建深色背景
        background = Rectangle(
            width=self.camera.frame_width,
            height=self.camera.frame_height,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        self.add(background)
        
        # 创建星空 - 使用更兼容的方法设置透明度
        stars = VGroup()
        for _ in range(300):
            # 创建星星时直接设置初始透明度
            initial_opacity = np.random.uniform(0.3, 0.8)
            star = Dot(
                point=np.array([
                    np.random.uniform(-4, 4),
                    np.random.uniform(-7, 7),
                    0
                ]),
                radius=np.random.uniform(0.01, 0.05),
                color=random.choice([WHITE, BLUE_B, BLUE_E, YELLOW_C]),
                fill_opacity=initial_opacity
            )
            stars.add(star)
        
        # 添加动态星星效果 - 修复透明度问题
        def update_star(star):
            # 使用fill_opacity而不是opacity
            new_opacity = star.fill_opacity + np.random.uniform(-0.2, 0.2) * 0.05
            new_opacity = np.clip(new_opacity, 0.3, 0.8)
            star.set_fill(opacity=new_opacity)
        
        # 创建标题
        title = Text("10个不定积分公式", font_size=48, color=BLUE)
        title_box = SurroundingRectangle(
            title, 
            color=WHITE, 
            buff=0.4,
            fill_color="#0D3B66",
            fill_opacity=0.8,
            stroke_width=2
        )
        title_group = VGroup(title_box, title)
        title_group.to_edge(UP, buff=1.0)
        
        # 添加标题发光效果
        title_glow = title.copy()
        title_glow.set_color("#FFA500")
        title_glow.set_stroke(width=8, color="#FFA500", opacity=0.3)
        title_glow.set_fill(opacity=0)
        title_glow.scale(1.05)
        title_group.add(title_glow)
        
        # 添加数学公式装饰
        formulas = VGroup(
            MathTex(r"\int e^{ax} \,dx = \frac{1}{a}e^{ax} + C", color=BLUE_C),
            MathTex(r"\int \frac{1}{x} \,dx = \ln|x| + C", color=GREEN_C),
            MathTex(r"\int \cos(ax) \,dx = \frac{1}{a}\sin(ax) + C", color=YELLOW_C),
            MathTex(r"\int \frac{1}{1+x^2} \,dx = \arctan(x) + C", color=RED_C)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        for formula in formulas:
            formula.scale(0.8)
            formula.set_opacity(0.8)
            formula.set_stroke(width=1, color=WHITE, opacity=0.3)
        
        formulas.next_to(title_group, DOWN, buff=1.0)
        
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
        
    
        # 添加装饰线条
        line1 = Line(LEFT * 3.5, RIGHT * 3.5, color=BLUE_E, stroke_width=1)
        line1.next_to(title_group, DOWN, buff=0.4)
        
        line2 = Line(LEFT * 3, RIGHT * 3, color=BLUE_D, stroke_width=0.8)
        line2.next_to(formulas, DOWN, buff=0.8)
        
        # 组合所有元素
        self.add(stars)
        self.add(big_integral)
        self.add(math_symbols)
        self.add(title_group)
        self.add(line1)
        self.add(formulas)
        self.add(line2)
        
        # 添加动画效果
        # self.play(
        #     FadeIn(title_group, shift=DOWN * 0.5),
        #     FadeIn(formulas, lag_ratio=0.1),
        #     run_time=2
        # )
    

# manim -pqh --format=png 视频封面.py MathCover -r 1920,1080