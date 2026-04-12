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
        # 创建坐标系 - 调整位置为偏下
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=9,
            y_length=6,
            axis_config={
                "color": "#ECEFF1",
                "stroke_width": 3,
                "tip_length": 0.1,
                "tip_width": 0.2
            },
            tips=True,
        ).shift(DOWN * 1.5)
        
        # 添加坐标轴标签
        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=UP, buff=0.2)
        self.add(axes, x_label, y_label)
        
        curves = [
            # 心形线
            {
                "title": "心形线",
                "func": lambda t: [16*np.sin(t)**3, 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t), 0],
                "t_range": [0, 2*PI],
                "color": RED,
                "equation_lines": [
                    r"x(t) = 16\sin^3 t",
                    r"y(t) = 13\cos t - 5\cos 2t - 2\cos 3t - \cos 4t"
                ],
                "scale": 0.2
            },
            # 蝴蝶曲线
            {
                "title": "蝴蝶曲线",
                "func": lambda t: [np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5),
                                  np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5), 0],
                "t_range": [0, 12*PI],
                "color": PINK,
                "equation_lines": [
                    r"x(t) = \sin t(e^{\cos t} - 2\cos 4t - \sin^5(t/12))",
                    r"y(t) = \cos t(e^{\cos t} - 2\cos 4t - \sin^5(t/12))"
                ],
                "scale": 0.8
            },
            # 玫瑰曲线
            {
                "title": "玫瑰曲线",
                "func": lambda t: [3*np.cos(3*t)*np.cos(t), 3*np.cos(3*t)*np.sin(t), 0],
                "t_range": [0, 2*PI],
                "color": PURPLE,
                "equation_lines": [
                    r"x(t) = 3\cos 3t \cos t",
                    r"y(t) = 3\cos 3t \sin t"
                ],
                "scale": 0.8
            },
            # 双纽线
            {
                "title": "双纽线",
                "func": lambda t: [3*np.sqrt(np.cos(2*t))*np.cos(t), 3*np.sqrt(np.cos(2*t))*np.sin(t), 0],
                "t_range": [-PI/4, PI/4],
                "color": BLUE,
                "equation_lines": [
                    r"x(t) = 3\sqrt{\cos 2t} \cos t",
                    r"y(t) = 3\sqrt{\cos 2t} \sin t"
                ],
                "scale": 0.8
            },
            # 星形线
            {
                "title": "星形线",
                "func": lambda t: [3*np.cos(t)**3, 3*np.sin(t)**3, 0],
                "t_range": [0, 2*PI],
                "color": ORANGE,
                "equation_lines": [
                    r"x(t) = 3\cos^3 t",
                    r"y(t) = 3\sin^3 t"
                ],
                "scale": 0.8
            },
            # 螺旋线
            {
                "title": "螺旋线",
                "func": lambda t: [0.5*t*np.cos(t), 0.5*t*np.sin(t), 0],
                "t_range": [0, 6*PI],
                "color": GREEN,
                "equation_lines": [
                    r"x(t) = 0.5t \cos t",
                    r"y(t) = 0.5t \sin t"
                ],
                "scale": 0.5
            },
            # 利萨如图形
            {
                "title": "利萨如图形",
                "func": lambda t: [3*np.sin(3*t), 3*np.cos(2*t), 0],
                "t_range": [0, 2*PI],
                "color": YELLOW,
                "equation_lines": [
                    r"x(t) = 3\sin 3t",
                    r"y(t) = 3\cos 2t"
                ],
                "scale": 0.8
            },
            # 椭圆
            {
                "title": "椭圆",
                "func": lambda t: [4*np.cos(t), 2*np.sin(t), 0],
                "t_range": [0, 2*PI],
                "color": TEAL,
                "equation_lines": [
                    r"x(t) = 4\cos t",
                    r"y(t) = 2\sin t"
                ],
                "scale": 0.8
            },
            # 双曲线
            {
                "title": "双曲线",
                "func": lambda t: [2*np.cosh(t), np.sinh(t), 0],
                "t_range": [-2, 2],
                "color": MAROON,
                "equation_lines": [
                    r"x(t) = 2\cosh t",
                    r"y(t) = \sinh t"
                ],
                "scale": 0.8
            },
            # 摆线
            {
                "title": "摆线",
                "func": lambda t: [3*(t - np.sin(t)), 3*(1 - np.cos(t)), 0],
                "t_range": [0, 4*PI],
                "color": GOLD,
                "equation_lines": [
                    r"x(t) = 3(t - \sin t)",
                    r"y(t) = 3(1 - \cos t)"
                ],
                "scale": 0.3
            }
        ]
        
        # 创建初始函数和标签
        curve = curves[0]
        title = Tex(curve["title"], font_size=42, color=curve["color"]).to_edge(UP, buff=3)
        
        # 创建方程 - 统一字体大小为36，左对齐到屏幕左侧
        equation_lines = []
        for line in curve["equation_lines"]:
            eq_line = MathTex(line, color=curve["color"], font_size=36)
            equation_lines.append(eq_line)
        
        equation = VGroup(*equation_lines)
        equation.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        # 将方程左对齐到屏幕左侧，并放置在标题下方
        equation.next_to(title, DOWN, buff=0.4)
        equation.to_edge(LEFT,buff=0.5)  # 左对齐到屏幕左侧
        
        
        # 创建图形
        graph = self.create_graph(axes, curve["func"], curve["t_range"], curve["color"], curve["scale"])
        
        # 添加背景框使方程更清晰
        eq_bg = SurroundingRectangle(equation, color=curve["color"], buff=0.2, stroke_width=1, fill_opacity=0.08)
        
        self.play(Create(graph), Write(equation), Write(eq_bg), Write(title), run_time=1.5)

        # 动画展示所有函数
        for i in range(1, len(curves)):
            curve = curves[i]
            new_title = Tex(curve["title"], font_size=42, color=curve["color"]).to_edge(UP, buff=3)
            
            # 创建新方程 - 统一字体大小为36，左对齐到屏幕左侧
            new_equation_lines = []
            for line in curve["equation_lines"]:
                eq_line = MathTex(line, color=curve["color"], font_size=36)
                new_equation_lines.append(eq_line)
            
            new_equation = VGroup(*new_equation_lines)
            new_equation.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            # 将新方程左对齐到屏幕左侧，并放置在标题下方
            new_equation.next_to(new_title, DOWN, buff=0.4)
            new_equation.to_edge(LEFT,buff=0.5)  # 左对齐到屏幕左侧
            new_eq_bg = SurroundingRectangle(new_equation, color=curve["color"], buff=0.2, stroke_width=1, fill_opacity=0.08)
            new_graph = self.create_graph(axes, curve["func"], curve["t_range"], curve["color"], curve["scale"])
            
            self.play(
                ReplacementTransform(graph, new_graph),
                ReplacementTransform(equation, new_equation),
                ReplacementTransform(eq_bg, new_eq_bg),
                ReplacementTransform(title, new_title),
                run_time=1.5
            )
            graph = new_graph
            equation = new_equation
            eq_bg = new_eq_bg
            title = new_title
            self.wait(0.5)
    
    def create_graph(self, axes, func, t_range=None, color=WHITE, scale=1):
        """创建函数图像"""
        if t_range:
            graph = axes.plot_parametric_curve(func, t_range=t_range, color=color, stroke_width=4)
            return graph.scale(scale, about_point=axes.coords_to_point(0, 0))
        graph = axes.plot_parametric_curve(func, color=WHITE, stroke_width=4)
        return graph.scale(scale, about_point=axes.coords_to_point(0, 0))


# 运行命令: manim -p -ql 参数方程测试.py FunctionGallery