from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
import numpy as np
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class ParametricSpiral(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 标题和方程
        title = Tex(r"神奇的参数方程", font_size=48, color=YELLOW).to_edge(UP, buff=1.5)
        equation = MathTex(
            r"x(t) &= \cos(at) + \frac{\cos(bt)}{2} + \frac{\sin(ct)}{3} \\",
            r"y(t) &= \sin(at) + \frac{\sin(bt)}{2} + \frac{\cos(ct)}{3}",
            font_size=36
        ).next_to(title, DOWN, buff=0.5)
        
        # 参数控制面板
        params = VGroup(
            MathTex("a = ", font_size=36),
            DecimalNumber(1, num_decimal_places=0),
            MathTex("b = ", font_size=36),
            DecimalNumber(1, num_decimal_places=0),
            MathTex("c = ", font_size=36),
            DecimalNumber(0, num_decimal_places=0)
        ).arrange(RIGHT, buff=0.5).next_to(equation, DOWN, buff=0.3)
        
        # 创建参数跟踪器
        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(1)
        c_tracker = ValueTracker(0)
        
        # 更新参数显示
        params[1].add_updater(lambda m: m.set_value(a_tracker.get_value()))
        params[3].add_updater(lambda m: m.set_value(b_tracker.get_value()))
        params[5].add_updater(lambda m: m.set_value(c_tracker.get_value()))
        
        self.add(title, equation, params)
        self.wait(0.5)
        
        # 创建曲线
        curve = always_redraw(
            lambda: ParametricFunction(
                lambda t: self.parametric_curve(t, a_tracker.get_value(), b_tracker.get_value(), c_tracker.get_value()),
                t_range=[0, 2*PI],
                stroke_width=4
            ).scale(1.8).shift(DOWN * 1).set_color(color=[BLUE, PURPLE, RED])
        )
        
        self.play(Create(curve), run_time=0.5)
        
        # 动画序列
        animations = [
            (b_tracker, 60, 6),
            (b_tracker, 1, 6),
            (a_tracker, 60, 6),
            (a_tracker, 1, 6),
            (c_tracker, 60, 6),
            (c_tracker, 0, 6)
        ]
        
        for tracker, target_value, duration in animations:
            self.play(
                tracker.animate.set_value(target_value),
                rate_func=linear,
                run_time=duration
            )
        
        self.wait(2)
        
        # 添加更多参数方程
        self.play(FadeOut(title), FadeOut(equation), FadeOut(params), FadeOut(curve))
        self.show_more_curves()
    
    def parametric_curve(self, t, a, b, c):
        x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
        y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3
        return np.array([x, y, 0])
    
    def show_more_curves(self):
        # 更多参数方程示例
        curves = [
            {
                "title": "玫瑰曲线",
                "equation": MathTex(
                    r"x(t) &= \cos(4t)\cos(t) \\",
                    r"y(t) &= \cos(4t)\sin(t)",
                    font_size=36
                ),
                "func": lambda t: np.array([
                    np.cos(4*t) * np.cos(t),
                    np.cos(4*t) * np.sin(t),
                    0
                ]),
                "color": PINK,
                "scale": 2.5
            },
            {
                "title": "利萨如图形",
                "equation": MathTex(
                    r"x(t) &= \sin(3t) \\",
                    r"y(t) &= \cos(5t)",
                    font_size=36
                ),
                "func": lambda t: np.array([
                    np.sin(3*t),
                    np.cos(5*t),
                    0
                ]),
                "color": BLUE,
                "scale": 2.5
            },
            {
                "title": "心形线",
                "equation": MathTex(
                    r"x(t) &= 16\sin^3(t) \\",
                    r"y(t) &= 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t)",
                    font_size=30
                ),
                "func": lambda t: np.array([
                    16 * np.sin(t)**3,
                    13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                    0
                ]),
                "color": RED,
                "scale": 0.5
            },
            {
                "title": "蝴蝶曲线",
                "equation": MathTex(
                    r"x(t) &= \sin(t)(e^{\cos t} - 2\cos(4t) - \sin^5(t/12)) \\",
                    r"y(t) &= \cos(t)(e^{\cos t} - 2\cos(4t) - \sin^5(t/12))",
                    font_size=28
                ),
                "func": lambda t: np.array([
                    np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5),
                    np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5),
                    0
                ]),
                "color": PURPLE,
                "scale": 1.5
            },
            {
                "title": "阿基米德螺线",
                "equation": MathTex(
                    r"x(t) &= t\cos(t) \\",
                    r"y(t) &= t\sin(t)",
                    font_size=36
                ),
                "func": lambda t: np.array([
                    t * np.cos(t),
                    t * np.sin(t),
                    0
                ]),
                "color": TEAL,
                "scale": 0.5,
                "t_range": [0, 10*PI]
            }
        ]
        
        for curve_data in curves:
            title = Tex(curve_data["title"], font_size=48, color=YELLOW).to_edge(UP, buff=1.5)
            equation = curve_data["equation"].next_to(title, DOWN, buff=0.5)
            
            t_range = curve_data.get("t_range", [0, 2*PI])
            curve = ParametricFunction(
                curve_data["func"],
                t_range=t_range,
                stroke_width=4
            ).scale(curve_data["scale"]).set_color(curve_data["color"])
            
            self.play(
                Write(title),
                Write(equation),
                Create(curve),
                run_time=2
            )
            self.wait(3)
            self.play(
                FadeOut(title),
                FadeOut(equation),
                FadeOut(curve),
                run_time=1
            )
        
        # 结束语
        end_text = Text("参数方程之美", font_size=60, color=YELLOW)
        self.play(Write(end_text), run_time=2)
        self.wait(3)
        
# manim -pqh 参数之美.py ParametricSpiral -r 1080,1920