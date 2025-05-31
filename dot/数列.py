from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class FibonacciGeometry(Scene):
    def construct(self):
        
        title = Text("能做出来一定是天才", font_size=60, color=BLUE)
        

        # 添加数学公式
        formula = MathTex(r"\frac{810 \times 811 \times 812 \times \cdots \times 2010}{810^n}",font_size=50,color=RED_C)
        formula.next_to(title,DOWN,buff=0.5)
        caption = Text(
            "要保持分式为整数，求n的最大值", 
            font_size=44, 
            color=GRAY,
            t2c={"n": YELLOW}  # n 为黄色
        )
        caption.next_to(formula, DOWN)
        self.play(
        Write(title,run_time=3),
        Write(formula,run_time=3)  # 显示公式
        # FadeIn(caption, shift=UP,run_time=3)
        )
         # 组合成一个 VGroup 并整体居中
        group = VGroup(title, formula, caption)
        group.move_to(ORIGIN)  # 移动到画面中心
        self.wait(0.5)
        self.play(FadeIn(caption, shift=UP,run_time=3))
        self.wait(10)

        
        
    
           
# manim -pqh 数列.py FibonacciGeometry -r 1920,1080

