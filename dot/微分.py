from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CalculusFormulas(Scene):
    def construct(self):
        # 场景标题
        title = Text("微积分核心公式: 极限", font_size=42, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.9).to_edge(UP))
        self.wait(0.5)
        
        # 创建两列容器
        col1 = VGroup()
        col2 = VGroup()
        
        # 基础极限部分 - 左列
        basic_title = Text("基础极限", font_size=20, color=YELLOW)
        basic_formulas = VGroup(
            MathTex(r"\lim_{x \to a} c = c", font_size=30),
            MathTex(r"\lim_{x \to a} x = a", font_size=30),
            MathTex(r"\lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)", font_size=30),
            MathTex(r"\lim_{x \to a} [c \cdot f(x)] = c \cdot \lim_{x \to a} f(x)", font_size=30),
            MathTex(r"\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)", font_size=30),
            MathTex(r"\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}", font_size=30),
            MathTex(r"\text{(若} \lim_{x \to a} g(x) \neq 0)", font_size=26),
            MathTex(r"\lim_{x \to a} [f(x)]^{g(x)} = \left[\lim_{x \to a} f(x)\right]^{\lim_{x \to a} g(x)}", font_size=30),
            MathTex(r"\text{(若极限存在且为正)}", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        
        col1.add(basic_title, basic_formulas)
        col1.arrange(DOWN, buff=0.4)
        
        # 重要极限部分 - 右列
        important_title = Text("重要极限", font_size=20, color=GREEN)
        important_formulas = VGroup(
            MathTex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1", font_size=30),
            MathTex(r"\lim_{x \to 0} \frac{\tan x}{x} = 1", font_size=30),
            MathTex(r"\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}", font_size=30),
            MathTex(r"\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e", font_size=30),
            MathTex(r"\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e", font_size=30),
            MathTex(r"\lim_{x \to 0} \frac{e^x - 1}{x} = 1", font_size=30),
            MathTex(r"\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1", font_size=30),
            MathTex(r"\lim_{x \to 0} \frac{a^x - 1}{x} = \ln a", font_size=30),
            MathTex(r"\lim_{x \to 0} \frac{(1 + x)^a - 1}{x} = a", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        
        col2.add(important_title, important_formulas)
        col2.arrange(DOWN, buff=0.4)
        
        # 将两列并排放置
        columns = VGroup(col1, col2)
        columns.arrange(RIGHT, buff=1.2, aligned_edge=UP)  # 修改点：TOP -> UP
        columns.next_to(title, DOWN, buff=0.1).scale(0.9)
        
        # 动画显示两列
        self.play(
            FadeIn(col1, shift=DOWN),
            FadeIn(col2, shift=DOWN),
            run_time=1.5
        )
        self.wait(2)
        
        # 添加说明框
        note_box = Rectangle(
            width=10, height=1.2, 
            fill_color=BLACK, fill_opacity=0.7, 
            stroke_color=YELLOW, stroke_width=2
        )
        note_box.next_to(columns, DOWN, buff=0.5)
        note_text = Text(
            "这些极限公式是微积分的基础，在导数、积分和级数中有广泛应用",
            font_size=26, color=WHITE
        )
        note_text.move_to(note_box)
        
        self.play(
            Create(note_box),
            Write(note_text),
            run_time=1.5
        )
        self.wait(2)
        
        # 渐变消失所有元素
        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.1),
            run_time=2
        )