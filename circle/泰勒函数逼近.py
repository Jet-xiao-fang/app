from manim import *
import math

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class TaylorApproximationEnhanced(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 调整坐标轴比例：使画面更紧凑，留出上下空间
        axes = Axes(
            x_range=[-PI, PI, 1],
            y_range=[-1.5, 1.5, 0.5],      # 缩小y范围，减少空白
            x_length=8,
            y_length=4.5,                  # 降低高度，为上下文字留出空间
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        )
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        
        # 标题：移到顶部中央，适当缩小字体并减小上边距
        title = Tex("$\\sin(x)$ 泰勒展开式", color=YELLOW, font_size=48)
        title.to_edge(UP, buff=0.5)
        
        # 公式生成函数：缩小字体，位置改为左下角（不遮挡坐标轴）
        def get_taylor_formula(order):
            terms = []
            for n in range(1, order+1, 2):
                sign = "-" if (n-1)//2 % 2 else "+"
                if n == 1:
                    term = r"x"
                else:
                    term = fr"\frac{{x^{{{n}}}}}{{{n}!}}"
                    term = sign + term
                terms.append(term)
            formula = "T_{}(x) = ".format(order) + " ".join(terms)
            formula = formula.replace("+ ", "", 1).replace("- ", "-", 1)
            # 放在左下角，对齐左边缘，距离底部一定缓冲
            return MathTex(formula).scale(0.7).to_corner(DOWN + LEFT, buff=0.3)

        # 原始正弦曲线
        original_curve = axes.plot(lambda x: math.sin(x), color="#EF5350")
        original_label = axes.get_graph_label(original_curve, label="\\sin(x)", 
                                              direction=DOWN, x_val=-2.5).set_color("#EF5350")

        # 泰勒多项式配置
        orders = [1, 3, 5, 7, 9]
        colors = [BLUE_B, BLUE_C, BLUE_D, TEAL_B, TEAL_D]
        
        taylor_curves = []
        formula_objects = []
        for i, order in enumerate(orders):
            def taylor_func(x, order=order):
                return sum(((-1)**((k-1)//2)) * (x**k)/math.factorial(k) 
                        for k in range(1, order+1, 2))
            curve = axes.plot(taylor_func, color=colors[i])
            taylor_curves.append(curve)
            formula = get_taylor_formula(order)
            formula.set_color(colors[i])
            formula_objects.append(formula)

        # 动画序列
        self.play(Create(axes), Create(axis_labels), run_time=1.5)
        self.play(Write(title), run_time=1)          # 标题单独出现
        self.play(Create(original_curve), Write(original_label))
        self.wait()
        
        current_curve = original_curve.copy()
        current_label = original_label.copy()
        current_formula = None
        
        for curve, formula in zip(taylor_curves, formula_objects):
            anims = [
                ReplacementTransform(current_curve, curve),
                ReplacementTransform(current_label, formula),
            ]
            if current_formula:
                anims.append(FadeOut(current_formula))
            self.play(*anims, run_time=2)
            self.wait(0.5)
            self.play(Write(formula))               # 公式渐入（实际已存在，但为了视觉效果）
            self.wait(0.5)
            current_curve = curve
            current_label = formula
            current_formula = formula.copy()
        
        self.wait(3)

#   manim -pqh 泰勒函数逼近.py TaylorApproximationEnhanced