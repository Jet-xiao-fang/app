from manim import *
import numpy as np

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class FibonacciGeometry(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 创建标题 - 添加渐变和描边效果
        title = Text("能做出来一定是天才", 
                   font_size=60, 
                   color=BLUE,
                   stroke_width=1.5,
                   stroke_color=BLUE_E)
        title.set_color_by_gradient(BLUE_B, BLUE_D)
        
        # 创建公式 - 使用更好的颜色对比
        formula = MathTex(
            r"\frac{810 \times 811 \times 812 \times \cdots \times 2010}{810^n}",
            font_size=50,
            color=YELLOW_C
        )
        formula.next_to(title, DOWN, buff=0.7)
        
        # 添加公式背景框
        formula_box = SurroundingRectangle(formula, color=BLUE_E, 
                                          fill_color="#1A1A2E", 
                                          fill_opacity=0.7, 
                                          corner_radius=0.2)
        formula_box.stretch(1.2, 0)  # 水平方向稍微拉长
        
        # 创建说明文字 - 添加颜色强调
        caption = Text(
            "要保持分式为整数，求n的最大值", 
            font_size=44, 
            color=LIGHT_GRAY,
            t2c={"n": YELLOW}  # n 为黄色
        )
        caption.next_to(formula_box, DOWN, buff=0.5)
        
        # 创建装饰元素
        dots = VGroup(*[Dot(color=BLUE_E, radius=0.05) for _ in range(20)])
        dots.arrange_in_grid(4, 5, buff=0.4)
        dots.move_to(ORIGIN).shift(UP * 3.5)
        for dot in dots:
            dot.set_opacity(0.5)
        
        # 组合所有元素
        group = VGroup(dots, title, formula_box, formula, caption)
        group.move_to(ORIGIN)  # 移动到画面中心
        
        # 优化动画序列
        self.play(
            FadeIn(dots, shift=DOWN, scale=0.8, run_time=2),
            LaggedStart(
                GrowFromCenter(title, run_time=1.5),
                Create(formula_box, run_time=1.2),
                Write(formula, run_time=2.5),
                lag_ratio=0.3
            )
        )
        
        self.play(
            FadeIn(caption, shift=UP, run_time=1.5),
            dots.animate.shift(UP * 0.2).scale(1.05).set_opacity(0.8),
            run_time=1.5
        )
        
        # 添加最后的强调效果
        self.play(
            Flash(formula[0][-3:],  # 高亮 n
                flash_radius=1.2,
                line_length=0.8,
                num_lines=15,
                color=YELLOW,
                run_time=1.5
            ),
            Wiggle(caption[12:13], scale_value=1.3, rotation_angle=0.1, run_time=1.5)  # 抖动 n
        )
        
        # 添加保持时间
        self.wait(8)
        
        # 优雅的退出动画
        self.play(
            FadeOut(group, shift=UP, scale=0.9, run_time=2),
            dots.animate.scale(0.5).set_opacity(0)
        )
        self.wait(1)                
# manim -pqh 数列.py FibonacciGeometry -r 1920,1080

