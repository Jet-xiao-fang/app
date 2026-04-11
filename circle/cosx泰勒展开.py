from manim import *
import math

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CosTaylorApproximation(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"

        # 坐标系配置（调整y范围和高度，留出上下空间）
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
        title = Tex("$\\cos(x)$ 泰勒展开式", color=YELLOW, font_size=48)
        title.to_edge(UP, buff=0.5)

        # 生成泰勒展开式文本的函数（已适配cos，并放置于左下角）
        def get_taylor_formula(order):
            terms = []
            for n in range(0, order + 1, 2):
                if n == 0:  # 首项为常数1
                    terms.append("1")
                    continue
                k = n // 2
                sign = "-" if k % 2 else "+"
                term = fr"\frac{{x^{{{n}}}}}{{{n}!}}"
                terms.append(sign + term)
            formula = "T_{}(x) = ".format(order) + " ".join(terms)
            # 修正首项后的符号间距
            formula = formula.replace("- ", "- ", 1)
            # 放在左下角，对齐左边缘，距离底部一定缓冲
            return MathTex(formula).scale(0.7).to_corner(DOWN + LEFT, buff=0.3)

        # 原始余弦曲线（红色）
        original_curve = axes.plot(math.cos, color="#EF5350")
        original_label = axes.get_graph_label(
            original_curve,
            label="\\cos(x)",
            direction=UP,
            x_val=-2.5,               # 偏左放置，避免与泰勒公式重叠
            buff=0.1
        ).set_color("#EF5350")

        # 泰勒多项式配置（偶数阶）
        orders = [0, 2, 4, 6, 8]
        colors = [BLUE_B, BLUE_C, BLUE_D, TEAL_B, TEAL_D]

        taylor_curves = []
        formula_objects = []
        for i, order in enumerate(orders):
            def taylor_func(x, order=order):
                return sum(((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
                           for k in range(0, (order // 2) + 1))
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
            self.play(Write(formula))
            self.wait(0.5)
            current_curve = curve
            current_label = formula
            current_formula = formula.copy()

        self.wait(3)

#   manim -pqh cosx泰勒展开.py CosTaylorApproximation