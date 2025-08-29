from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np
class CosTaylorApproximation(Scene):
    def construct(self):
        # 坐标系配置
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI/2],  # x 从 -2π 到 2π，刻度间隔 π/2
            y_range=[-3, 3, 1],         # y 从 -1.5 到 1.5，刻度间隔 0.5
            x_length=10,
            y_length=8,
            axis_config={"color": "#ECEFF1",
                         "stroke_width": 3,
                         "tip_length": 0.1,
                         "tip_width": 0.2},
            tips=True,  # 不显示箭头
        ).shift(DOWN * 0.5)
        
        my_run_time=0.5
        
        self.add(axes)
        
        parabola = axes.plot_parametric_curve(
            lambda t: [6*np.cos(t)/(1+np.sin(t)**2), 6*np.cos(t)*np.sin(t)/(1+np.sin(t)**2), 0],  
            t_range=[-PI, PI],
            color=GREEN,
            stroke_width=4
        ).scale(0.8)
        # 添加方程标签
        equation = MathTex(
            r"x(t) &= \dfrac{6\cos t}{1+\sin^2 t} \\",
            r"y(t) &= \dfrac{6\cos t \sin t}{1+\sin^2 t}",
            color=GREEN
        ).to_corner(UL) 
        self.play(Create(parabola),Write(equation),run_time=my_run_time)
        
        
        p1 = axes.plot_parametric_curve(
            lambda t: [3*np.cos(t)**3, 3*np.sin(t)**3, 0],  
            t_range=[-PI, PI],
            color=ORANGE,
            stroke_width=4
        ).scale(0.8)
        # 添加方程标签
        e1 = MathTex(
            r"x(t) &= 3\sin^3 t \\",
            r"y(t) &= 3\cos^3 t",
            color=ORANGE
        ).to_corner(UL) 
        self.play(ReplacementTransform(parabola,p1),ReplacementTransform(equation,e1),run_time=my_run_time)
        
        p2 = axes.plot_parametric_curve(
            lambda t: [3*np.sin(2*t)*np.cos(t), 3*np.sin(2*t)*np.sin(t), 0],
            t_range=[-PI, PI],
            color=ORANGE,
            stroke_width=4
        ).scale(0.8)
        # 添加方程标签
        e2 = MathTex(
            r"x(t) &= 3\sin(2t)cos(t) \\",
            r"y(t) &= 3\sin(2t)sin(t)",
            color=ORANGE
        ).to_corner(UL) 
        self.play(ReplacementTransform(p1,p2),ReplacementTransform(e1,e2),run_time=my_run_time)
        
        
        p3 = axes.plot_parametric_curve(
            lambda t: [3*np.sin(t)**3, 3*(13/16*np.cos(t)-5/16*np.cos(2*t)-2/16*np.cos(3*t)-1/16*np.cos(4*t)), 0],
            t_range=[-PI, PI],
            color=RED,
            stroke_width=4
        ).scale(0.8)
        # 添加方程标签
        e3 = MathTex(
                r"x(t) &= 3\sin^3 t \\",
                r"y(t) &= 3 \left( \frac{13}{16} \cos t - \frac{5}{16} \cos 2t - \frac{2}{16} \cos 3t - \frac{1}{16} \cos 4t \right)",

                color=RED
            ).to_corner(UL)
       
        self.play(ReplacementTransform(p2,p3),ReplacementTransform(e2,e3),run_time=my_run_time)
        
        p8 = axes.plot(
        lambda x: np.sin(x),
        color=PINK,
        stroke_width=4
        )
        e8 = MathTex(r"y = \sin(x)", color=PINK).to_corner(UL)
        self.play(ReplacementTransform(p3, p8), ReplacementTransform(e3, e8),run_time=my_run_time)
        
        p9 = axes.plot(
        lambda x: np.sin(x+PI/6),
        color=PURPLE,
        stroke_width=4
        )
        e9 = MathTex(r"y = \sin\left(x + \frac{\pi}{6}\right)", color=PURPLE).to_corner(UL)
        self.play(ReplacementTransform(p8, p9), ReplacementTransform(e8, e9),run_time=my_run_time)
        
        
        p10 = axes.plot(
        lambda x: np.sin(x+PI/3),
        color=GRAY,
        stroke_width=4
        )
        e10 = MathTex(r"y = \sin\left(x + \frac{\pi}{3}\right)", color=GRAY).to_corner(UL)
        self.play(ReplacementTransform(p9, p10), ReplacementTransform(e9, e10),run_time=my_run_time)
        
        p11 = axes.plot(
        lambda x: np.sin(x+PI/2),
        color=BLUE,
        stroke_width=4
        )
        e11 = MathTex(r"y = \sin\left(x + \frac{\pi}{2}\right)", color=BLUE).to_corner(UL)
        self.play(ReplacementTransform(p10, p11), ReplacementTransform(e10, e11),run_time=my_run_time)
        
        
        p12 = axes.plot(
        lambda x: np.sin(2*x),
        color=GOLD,
        stroke_width=4
        )
        e12 = MathTex(r"y = \sin(2x)", color=GOLD).to_corner(UL)
        
        self.play(ReplacementTransform(p11, p12), ReplacementTransform(e11, e12),run_time=my_run_time)
        
        p13 = axes.plot(
        lambda x: np.sin(3*x),
        color=YELLOW,
        stroke_width=4
        )
        e13 = MathTex(r"y = \sin(3x)", color=YELLOW).to_corner(UL)
        self.play(ReplacementTransform(p12, p13), ReplacementTransform(e12, e13),run_time=my_run_time)
        
        p14 = axes.plot(
        lambda x: np.sin(4*x),
        color=RED_A,
        stroke_width=4
        )
        e14 = MathTex(r"y = \sin(4x)", color=RED_A).to_corner(UL)
        self.play(ReplacementTransform(p13, p14), ReplacementTransform(e13, e14),run_time=my_run_time)
        
        p15 = axes.plot(
            lambda x: np.cos(x),
            color=RED_B,
            stroke_width=4
        )
        e15 = MathTex(r"y = \cos(x)", color=RED_B).to_corner(UL)
        self.play(ReplacementTransform(p14, p15), ReplacementTransform(e14, e15),run_time=my_run_time)

        p16 = axes.plot(
            lambda x: np.cos(x+PI/6),
            color=ORANGE,
            stroke_width=4
        )
        e16 = MathTex(r"y = \cos\left(x + \frac{\pi}{6}\right)", color=ORANGE).to_corner(UL)
        self.play(ReplacementTransform(p15, p16), ReplacementTransform(e15, e16),run_time=my_run_time)

        p17 = axes.plot(
            lambda x: np.cos(x+PI/3),
            color=PINK,
            stroke_width=4
        )
        e17 = MathTex(r"y = \cos\left(x + \frac{\pi}{3}\right)", color=ORANGE).to_corner(UL)
        self.play(ReplacementTransform(p16, p17), ReplacementTransform(e16, e17),run_time=my_run_time)
        
        p18 = axes.plot(
            lambda x: np.cos(x+PI/2),
            color=PINK,
            stroke_width=4
        )
        e18 = MathTex(r"y = \cos\left(x + \frac{\pi}{2}\right)", color=ORANGE).to_corner(UL)
        self.play(ReplacementTransform(p17, p18), ReplacementTransform(e17, e18),run_time=my_run_time)

        p19 = axes.plot(
            lambda x: np.cos(2*x),
            color=BLUE_B,
            stroke_width=4
        )
        e19 = MathTex(r"y = \cos(2x)", color=ORANGE).to_corner(UL)
        self.play(ReplacementTransform(p18, p19), ReplacementTransform(e18, e19),run_time=my_run_time)

        p20 = axes.plot(
            lambda x: np.cos(3*x),
            color=BLUE_B,
            stroke_width=4
        )
        e20 = MathTex(r"y = \cos(3x)", color=ORANGE).to_corner(UL)
        self.play(ReplacementTransform(p19, p20), ReplacementTransform(e19, e20),run_time=my_run_time)
        
        p21 = axes.plot(
            lambda x: np.cos(4*x),
            color=BLUE,
            stroke_width=4
        )
        e21 = MathTex(r"y = \cos(4x)", color=BLUE).to_corner(UL)
        self.play(ReplacementTransform(p20, p21), ReplacementTransform(e20, e21),run_time=my_run_time)
        
        k_slider = ValueTracker(1) 
        
        def func(x, k):
            # 使用更稳定的心形曲线方程
            # 限制x的范围在[-1.8, 1.8]之间以避免复数结果
            x_clipped = np.clip(x, -1.8, 1.8)
            return (x_clipped**2)**(1/3) + 0.9 * np.sqrt(3.3 - x_clipped**2) * np.sin(k * PI * x_clipped)
             
        def get_curve():
            k_val = k_slider.get_value()
            x_min, x_max = -1.8, 1.8  # 限制x的范围
            x_vals = np.linspace(x_min, x_max, 500)
            y_vals = func(x_vals, k_val)
            
            # 过滤掉无效值
            valid_mask = np.isfinite(y_vals)
            x_valid = x_vals[valid_mask]
            y_valid = y_vals[valid_mask]
            
            return axes.plot_line_graph(
                x_valid, y_valid,
                line_color=RED,  # 改为红色，更符合心形曲线的传统颜色
                stroke_width=2,
                add_vertex_dots=False
            )
        
        curve = always_redraw(get_curve)
        e = MathTex(r"y = |x|^{2/3} + 0.9 \sqrt{3.3 - x^2} \cdot \sin(k \pi x)", 
                    color=RED).to_corner(UL)  # 相应地调整公式显示
        
        # 添加k值标签
        k_label = always_redraw(lambda: MathTex(
            f"k = {int(k_slider.get_value())}",
            color=RED
        ).next_to(e, DOWN))
        
        self.add(k_label)
        self.play(ReplacementTransform(p21, curve), ReplacementTransform(e21, e), run_time=my_run_time)
        
        # k值从1变化到20的动画
        self.play(
            k_slider.animate.set_value(16),
            run_time=5,  # 10秒完成变化
            rate_func=linear
        )
        self.wait(2)
        

#   manim -pqh 参数方程2.py CosTaylorApproximation -r 1920,1080