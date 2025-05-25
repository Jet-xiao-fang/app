from manim import *
import math

class CosTaylorApproximation(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        
        # 坐标系配置
        axes = Axes(
            x_range=[-PI, PI, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).to_edge(DOWN)
        
        # 生成泰勒展开式文本的函数（已适配cos）
        def get_taylor_formula(order):
            terms = []
            for n in range(0, order+1, 2):
                if n == 0:  # 处理首项
                    terms.append("1")
                    continue
                
                k = n // 2
                sign = "-" if k % 2 else "+"
                term = fr"\frac{{x^{{{n}}}}}{{{n}!}}"
                terms.append(sign + term)
            
            formula = "T_{}(x) = ".format(order) + " ".join(terms)
            # 修正首项后的符号间距
            formula = formula.replace("- ", "- ", 1)
            return MathTex(formula).scale(0.8).to_corner(UR).shift(LEFT*2)

        # 原始余弦曲线（红色）
        original_curve = axes.plot(math.cos, color="#EF5350")
        original_label = axes.get_graph_label(
            original_curve, 
            label="\\cos(x)", 
            direction=UR
        ).set_color("#EF5350")

        # 泰勒多项式配置（偶数阶）
        orders = [0, 2, 4, 6, 8]
        colors = [BLUE_B, BLUE_C, BLUE_D, TEAL_B, TEAL_D]
        
        # 生成所有曲线和公式
        taylor_curves = []
        formula_objects = []
        for i, order in enumerate(orders):
            # 生成近似曲线
            def taylor_func(x, order=order):
                return sum(((-1)**k) * (x**(2*k))/math.factorial(2*k) 
                        for k in range(0, (order//2)+1))
            
            curve = axes.plot(taylor_func, color=colors[i])
            taylor_curves.append(curve)
            
            # 生成对应的公式对象
            formula = get_taylor_formula(order)
            formula.set_color(colors[i])
            formula_objects.append(formula)

        # 动画序列
        self.play(Create(axes), run_time=2)
        self.play(Create(original_curve), Write(original_label))
        self.wait()
        
        current_curve = original_curve.copy()
        current_label = original_label.copy()
        current_formula = None
        
        for curve, formula in zip(taylor_curves, formula_objects):
            # 同时进行三个动画：曲线变换、标签更新、公式显示
            anims = [
                ReplacementTransform(current_curve, curve),
                ReplacementTransform(current_label, formula),
            ]
            
            if current_formula:
                anims.append(FadeOut(current_formula))
                
            self.play(*anims, run_time=2)
            self.wait(0.5)
            
            # 添加公式渐入动画
            self.play(Write(formula))
            self.wait(0.5)
            
            current_curve = curve
            current_label = formula
            current_formula = formula.copy()
        
        self.wait(3)

#   manim -pqh cosx泰勒展开.py CosTaylorApproximation -r 1920,1080