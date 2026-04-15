from manim import *
import numpy as np

class TransformingFunctions(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 10, 1],
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(-5, 5.1, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 10.1, 2),
            }
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # 标题
        title = Text("数学函数变换", font_size=48).to_edge(UP)
        
        # 添加坐标系和标题
        self.play(Write(axes), Write(axes_labels), FadeIn(title))
        self.wait(0.5)
        
        # 1. 线性函数: y = x
        linear_func = axes.plot(lambda x: x, color=RED)
        linear_label = MathTex("y = x", color=RED).next_to(linear_func, UP)
        
        self.play(Create(linear_func), Write(linear_label))
        self.wait(1)
        
        # 2. 线性函数 -> 二次函数: y = x → y = x²
        quadratic_func = axes.plot(lambda x: x**2, color=YELLOW)
        quadratic_label = MathTex("y = x^2", color=YELLOW).next_to(quadratic_func.get_end(), UR)
        
        self.play(
            ReplacementTransform(linear_func, quadratic_func),
            ReplacementTransform(linear_label, quadratic_label),
            run_time=2
        )
        self.wait(1)
        
        # 3. 二次函数 -> 正弦函数: y = x² → y = sin(x)
        sin_func = axes.plot(lambda x: np.sin(x), color=GREEN)
        sin_label = MathTex("y = \\sin(x)", color=GREEN).next_to(sin_func.get_top(), UP)
        
        self.play(
            ReplacementTransform(quadratic_func, sin_func),
            ReplacementTransform(quadratic_label, sin_label),
            run_time=2
        )
        self.wait(1)
        
        # 4. 正弦函数 -> 指数函数: y = sin(x) → y = e^x
        exp_func = axes.plot(lambda x: np.exp(x), color=PURPLE)
        exp_label = MathTex("y = e^x", color=PURPLE).next_to(exp_func.get_end(), UR)
        
        self.play(
            ReplacementTransform(sin_func, exp_func),
            ReplacementTransform(sin_label, exp_label),
            run_time=2
        )
        self.wait(1)
        
        # 5. 指数函数 -> 对数函数: y = e^x → y = ln(x)
        log_func = axes.plot(
            lambda x: np.log(x) if x > 0 else -10, 
            x_range=[0.001, 5],
            color=ORANGE
        )
        log_label = MathTex("y = \\ln(x)", color=ORANGE).next_to(log_func.get_end(), RIGHT)
        
        self.play(
            ReplacementTransform(exp_func, log_func),
            ReplacementTransform(exp_label, log_label),
            run_time=2
        )
        self.wait(1)
        
        # 6. 对数函数 -> 绝对值函数: y = ln(x) → y = |x|
        abs_func = axes.plot(lambda x: abs(x), color=TEAL)
        abs_label = MathTex("y = |x|", color=TEAL).next_to(abs_func.get_top(), UP)
        
        self.play(
            ReplacementTransform(log_func, abs_func),
            ReplacementTransform(log_label, abs_label),
            run_time=2
        )
        self.wait(1)
        
        # 7. 绝对值函数 -> 线性函数: 循环回起点
        linear_func2 = axes.plot(lambda x: x, color=RED)
        linear_label2 = MathTex("y = x", color=RED).next_to(linear_func2, UP)
        
        self.play(
            ReplacementTransform(abs_func, linear_func2),
            ReplacementTransform(abs_label, linear_label2),
            run_time=2
        )
        self.wait(1)
        
        # 结束场景 - 直接淡出所有内容
        self.play(
            FadeOut(linear_func2),
            FadeOut(linear_label2),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(title),
            run_time=2
        )
        self.wait(2)

# 运行命令：manim -p 函数图像展示.py TransformingFunctions