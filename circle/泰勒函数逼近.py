from manim import *
import math

class TaylorApproximationEnhanced(Scene):
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
        
        # 生成泰勒展开式文本的函数
        def get_taylor_formula(order):
            terms = []
            for n in range(1, order+1, 2):
                sign = "-" if (n-1)//2 % 2 else "+"
                if n == 1:  # 首项不需要符号
                    term = r"x"
                else:
                    term = fr"\frac{{x^{{{n}}}}}{{{n}!}}"
                    term = sign + term
                terms.append(term)
            
            formula = "T_{}(x) = ".format(order) + " ".join(terms)
            # 修正首项的符号问题
            formula = formula.replace("+ ", "", 1).replace("- ", "-", 1)
            return MathTex(formula).scale(0.8).to_corner(UR).shift(LEFT*2)

        # 原始正弦曲线
        original_curve = axes.plot(lambda x: math.sin(x), color="#EF5350")
        original_label = axes.get_graph_label(original_curve, label="\\sin(x)", direction=UR).set_color("#EF5350")

        # 泰勒多项式配置
        orders = [1, 3, 5, 7, 9]
        colors = [BLUE_B, BLUE_C, BLUE_D, TEAL_B, TEAL_D]
        
        # 生成所有曲线和公式
        taylor_curves = []
        formula_objects = []
        for i, order in enumerate(orders):
            # 生成近似曲线
            def taylor_func(x, order=order):
                return sum(((-1)**((k-1)//2)) * (x**k)/math.factorial(k) 
                        for k in range(1, order+1, 2))
            
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

#   manim -pqh 泰勒函数逼近.py TaylorApproximationEnhanced -r 1920,1080