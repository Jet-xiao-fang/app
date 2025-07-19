from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class DynamicLineChart(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        a = Dot(point=LEFT*2)
        b = Dot(point=RIGHT*2)
        line_ab = Line(a)
        self.add(a,b)

# 运行命令: 
# manim -pqh 圆与三角.py DynamicLineChart -r 1920,1080