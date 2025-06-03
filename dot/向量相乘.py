from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class PhysicsDotProduct(Scene):
    def construct(self):
        # 设置场景标题
        title = Text("向量点积在物理学中的应用", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.7).to_edge(UP))
        self.wait(0.5)
        
        
        
        # 其他物理应用
        applications_title = Text("点积在其他物理领域的应用", font_size=42, color=GREEN)
        applications = VGroup(
            Text("1. 电学: 电场强度 · 位移 = 电势差", font_size=30),
            Text("2. 磁学: 磁通量 = 磁场 · 面积向量", font_size=30),
            Text("3. 力学: 功率 = 力 · 速度", font_size=30),
            Text("4. 光学: 光通量 = 光强 · 面积向量", font_size=30),
            Text("5. 流体力学: 流量 = 流速 · 面积向量", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)
        
        
        
    

# manim -pqh --format=png 向量相乘.py PhysicsDotProduct -r 1920,1080