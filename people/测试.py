from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np

class FunctionGallery(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 创建坐标系
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=6,
            axis_config={
                "color": "#ECEFF1",
                "stroke_width": 3,
                "tip_length": 0.1,
                "tip_width": 0.2
            },
            tips=True,
        ).shift(DOWN * 0.5)
        
        self.add(axes)
        
        # 函数列表和对应的标签
        functions = [
            (lambda x: x**2, "y = x^2", [-1.5, 1.5]),
            (lambda x: -x**2, "y = -x^2", [-1.5, 1.5]),
            (lambda x: x, "y = x", [-1.5, 1.5]),
            (lambda x: np.abs(x), r"y = |x|", [-1.5, 1.5]),
            (lambda x: x+1, r"y = x+1", [-1.5, 1.5]),
            (lambda x: -x+1, r"y = -x+1", [-1.5, 1.5]),
            (lambda x: -2*x+1, r"y = -2x+2", [-1.5, 1.5]),
            (lambda x: x**3, r"y = x^3", [-1.5, 1.5]),
            (lambda x: np.sin(x), r"y = \sin(x)", None),
            (lambda x: np.sin(x+PI/6), r"y = \sin\left(x + \frac{\pi}{6}\right)", None),
            (lambda x: np.sin(x+PI/3), r"y = \sin\left(x + \frac{\pi}{3}\right)", None),
            (lambda x: np.sin(x+PI/2), r"y = \sin\left(x + \frac{\pi}{2}\right)", None),
            (lambda x: np.sin(2*x), r"y = \sin(2x)", None),
            (lambda x: np.sin(3*x), r"y = \sin(3x)", None),
            (lambda x: np.sin(4*x), r"y = \sin(4x)", None),
            (lambda x: np.cos(x), r"y = \cos(x)", None),
            (lambda x: np.cos(x+PI/6), r"y = \cos\left(x + \frac{\pi}{6}\right)", None),
            (lambda x: np.cos(x+PI/3), r"y = \cos\left(x + \frac{\pi}{3}\right)", None),
            (lambda x: np.cos(x+PI/2), r"y = \cos\left(x + \frac{\pi}{2}\right)", None),
            (lambda x: np.cos(2*x), r"y = \cos(2x)", None),
            (lambda x: np.cos(3*x), r"y = \cos(3x)", None),
            (lambda x: np.cos(4*x), r"y = \cos(4x)", None),
        ]
        
        # 创建初始函数和标签
        func, label, x_range = functions[0]
        graph = self.create_graph(axes, func, x_range)
        equation = MathTex(label, color=ORANGE).next_to(axes, UP, buff=0.2)
        self.play(Create(graph), Write(equation), run_time=0.5)
        
        # 动画展示所有函数
        for i in range(1, len(functions)):
            func, label, x_range = functions[i]
            new_graph = self.create_graph(axes, func, x_range)
            new_equation = MathTex(label, color=ORANGE).next_to(axes, UP, buff=0.2)
            
            self.play(
                ReplacementTransform(graph, new_graph),
                ReplacementTransform(equation, new_equation),
                run_time=0.5
            )
            graph = new_graph
            equation = new_equation
    
    def create_graph(self, axes, func, x_range=None):
        """创建函数图像"""
        if x_range:
            return axes.plot(func, x_range=x_range, color=WHITE, stroke_width=4)
        return axes.plot(func, color=WHITE, stroke_width=4)

# manim -pqh 测试.py FunctionGallery -r 1920,1080