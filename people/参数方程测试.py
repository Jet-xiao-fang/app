from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
import numpy as np

class FunctionGallery(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 创建坐标系
        axes = Axes(
             x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=8,
            axis_config={
                "color": "#ECEFF1",
                "stroke_width": 3,
                "tip_length": 0.1,
                "tip_width": 0.2
            },
            tips=True,
        ).shift(DOWN * 1)
        
        self.add(axes)
        
        curves = [
            # 心形线
            {
                "title": "心形线",
                "func": lambda t: [16*np.sin(t)**3, 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t), 0],
                "t_range": [0, 2*PI],
                "color": RED,
                "equation": MathTex(
                    r"x(t) &= 16\sin^3 t \\",
                    r"y(t) &= 13\cos t - 5\cos 2t - 2\cos 3t - \cos 4t",
                    color=RED
                ),
                "scale": 0.3
            },
            # 蝴蝶曲线
            {
                "title": "蝴蝶曲线",
                "func": lambda t: [np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5),
                                  np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5), 0],
                "t_range": [0, 12*PI],
                "color": PINK,
                "equation": MathTex(
                    r"x(t) &= \sin t(e^{\cos t} - 2\cos 4t - \sin^5(t/12)) \\",
                    r"y(t) &= \cos t(e^{\cos t} - 2\cos 4t - \sin^5(t/12))",
                    color=PINK
                ),
                "scale": 1.5
            },
            # 玫瑰曲线
            {
                "title": "玫瑰曲线",
                "func": lambda t: [3*np.cos(3*t)*np.cos(t), 3*np.cos(3*t)*np.sin(t), 0],
                "t_range": [0, 2*PI],
                "color": PURPLE,
                "equation": MathTex(
                    r"x(t) &= 3\cos 3t \cos t \\",
                    r"y(t) &= 3\cos 3t \sin t",
                    color=PURPLE
                ),
                "scale": 1.0
            },
            # 双纽线
            {
                "title": "双纽线",
                "func": lambda t: [3*np.sqrt(np.cos(2*t))*np.cos(t), 3*np.sqrt(np.cos(2*t))*np.sin(t), 0],
                "t_range": [-PI/4, PI/4],
                "color": BLUE,
                "equation": MathTex(
                    r"x(t) &= 3\sqrt{\cos 2t} \cos t \\",
                    r"y(t) &= 3\sqrt{\cos 2t} \sin t",
                    color=BLUE
                ),
                "scale": 1.0
            },
            # 星形线
            {
                "title": "星形线",
                "func": lambda t: [3*np.cos(t)**3, 3*np.sin(t)**3, 0],
                "t_range": [0, 2*PI],
                "color": ORANGE,
                "equation": MathTex(
                    r"x(t) &= 3\cos^3 t \\",
                    r"y(t) &= 3\sin^3 t",
                    color=ORANGE
                ),
                "scale": 1.0
            },
            # 螺旋线
            {
                "title": "螺旋线",
                "func": lambda t: [0.5*t*np.cos(t), 0.5*t*np.sin(t), 0],
                "t_range": [0, 6*PI],
                "color": GREEN,
                "equation": MathTex(
                    r"x(t) &= 0.5t \cos t \\",
                    r"y(t) &= 0.5t \sin t",
                    color=GREEN
                ),
                "scale": 0.5
            },
            # 利萨如图形
            {
                "title": "利萨如图形",
                "func": lambda t: [3*np.sin(3*t), 3*np.cos(2*t), 0],
                "t_range": [0, 2*PI],
                "color": YELLOW,
                "equation": MathTex(
                    r"x(t) &= 3\sin 3t \\",
                    r"y(t) &= 3\cos 2t",
                    color=YELLOW
                ),
                "scale": 1.0
            },
            # 椭圆
            {
                "title": "椭圆",
                "func": lambda t: [4*np.cos(t), 2*np.sin(t), 0],
                "t_range": [0, 2*PI],
                "color": TEAL,
                "equation": MathTex(
                    r"x(t) &= 4\cos t \\",
                    r"y(t) &= 2\sin t",
                    color=TEAL
                ),
                "scale": 1.0
            },
            # 双曲线
            {
                "title": "双曲线",
                "func": lambda t: [2*np.cosh(t), np.sinh(t), 0],
                "t_range": [-2, 2],
                "color": MAROON,
                "equation": MathTex(
                    r"x(t) &= 2\cosh t \\",
                    r"y(t) &= \sinh t",
                    color=MAROON
                ),
                "scale": 1.0
            },
            # 摆线
            {
                "title": "摆线",
                "func": lambda t: [3*(t - np.sin(t)), 3*(1 - np.cos(t)), 0],
                "t_range": [0, 4*PI],
                "color": GOLD,
                "equation": MathTex(
                    r"x(t) &= 3(t - \sin t) \\",
                    r"y(t) &= 3(1 - \cos t)",
                    color=GOLD
                ),
                "scale": 0.5
            }
        ]
        
        
        # 创建初始函数和标签
        curve = curves[0]
        title = Tex(curve["title"], font_size=48, color=curve["color"]).to_edge(UP, buff=2)
        graph = self.create_graph(axes, curve["func"], curve["t_range"], curve["color"], curve["scale"])
        equation = curve["equation"].set_color(curve["color"]).next_to(axes, UP, buff=1).scale(curve["scale"])
        self.play(Create(graph), Write(equation),Write(title), run_time=1.5)

        # 动画展示所有函数
        for i in range(1, len(curves)):
            curve = curves[i]
            new_title = Tex(curve["title"], font_size=48, color=curve["color"]).to_edge(UP, buff=2)
            new_graph = self.create_graph(axes, curve["func"], curve["t_range"], curve["color"], curve["scale"])
            new_equation = curve["equation"].set_color(curve["color"]).next_to(axes, UP, buff=1).scale(curve["scale"])
            
            self.play(
                ReplacementTransform(graph, new_graph),
                ReplacementTransform(equation, new_equation),
                ReplacementTransform(title, new_title),
                run_time=1.5
            )
            graph = new_graph
            equation = new_equation
            title = new_title
            self.wait(0.5)  # 添加短暂停顿
    
    def create_graph(self, axes, func, t_range=None,color=WHITE,scale=1):
        """创建函数图像"""
        if t_range:
            return axes.plot_parametric_curve(func, t_range=t_range, color=color, stroke_width=4).scale(scale)
        return axes.plot_parametric_curve(func, color=WHITE, stroke_width=4)

# manim -pqh 参数方程测试.py FunctionGallery