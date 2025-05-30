from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class FibonacciGeometry(Scene):
    def construct(self):
        
        title = Text("斐波那契数列的几何演示", font_size=40, color=BLUE)
        caption = Text("正方形边长 = 斐波那契数 | 螺旋线趋近黄金分割", font_size=24, color=GRAY)
        caption.next_to(title, DOWN)

        self.play(
        Write(title,run_time=3),
        FadeIn(caption, shift=UP,run_time=3)
        )
        self.wait(3)
        
    
        
        
        

       
# manim -pqh 数列.py FibonacciGeometry -r 1920,1080

