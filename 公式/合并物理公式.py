from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class PhysicsFormulasMerged(Scene):
    def construct(self):

        formulas_data = [
            {
                "name": "匀变速直线运动速度公式",
                "formula": r"v = v_0 + at",
                "info": "运动学基础公式",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "匀变速直线运动位移公式",
                "formula": r"s = v_0 t + \frac{1}{2}at^2",
                "info": "运动学基础公式",
                "color": WHITE,
                "scale": 1.3
            },
            {
                "name": "牛顿第二定律",
                "formula": r"F = ma",
                "info": "经典力学核心",
                "color": WHITE,
                "scale": 1.8
            },
            {
                "name": "万有引力定律",
                "formula": r"F = G\frac{m_1 m_2}{r^2}",
                "info": "天体力学基础",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "功的计算公式",
                "formula": r"W = Fs \cos\theta",
                "info": "功与能量基础",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "动能公式",
                "formula": r"E_k = \frac{1}{2}mv^2",
                "info": "能量守恒基础",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "胡克定律",
                "formula": r"F = kx",
                "info": "弹性力学基础",
                "color": WHITE,
                "scale": 1.8
            },
            {
                "name": "功率公式",
                "formula": r"P = \frac{W}{t}",
                "info": "功与能量基础",
                "color": WHITE,
                "scale": 1.8
            },
            {
                "name": "欧姆定律",
                "formula": r"I = \frac{U}{R}",
                "info": "电路基础",
                "color": WHITE,
                "scale": 1.8
            },
            {
                "name": "安培力公式",
                "formula": r"F = BIL \sin\theta",
                "info": "电磁学基础",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "爱因斯坦质能方程",
                "formula": r"E = mc^2",
                "info": "相对论基础",
                "color": WHITE,
                "scale": 2
            },
            {
                "name": "欧姆定律（另一形式）",
                "formula": r"V = IR",
                "info": "电路基础",
                "color": WHITE,
                "scale": 2
            },
            {
                "name": "高斯定律",
                "formula": r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}",
                "info": "电磁学基本定理",
                "color": WHITE,
                "scale": 1.2
            },
            {
                "name": "热力学第二定律",
                "formula": r"\Delta S \geqslant \frac{Q}{T}",
                "info": "热力学基本定律",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "薛定谔方程",
                "formula": r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi",
                "info": "量子力学基本方程",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "洛伦兹力公式",
                "formula": r"F = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})",
                "info": "电磁学基本定律",
                "color": WHITE,
                "scale": 1.2
            },
            {
                "name": "薄透镜方程",
                "formula": r"\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}",
                "info": "光学基础",
                "color": WHITE,
                "scale": 1.3
            },
            {
                "name": "光子能量公式",
                "formula": r"E = h\nu",
                "info": "量子物理基础",
                "color": WHITE,
                "scale": 1.8
            },
        ]

        first_item = formulas_data[0]
        first_name = Text(first_item["name"], font="STXingkai", font_size=56, color=YELLOW)
        first_formula = MathTex(first_item["formula"], color=first_item.get("color", WHITE), font_size=54)
        first_info = Text(first_item["info"], font="STXingkai", font_size=42, color=TEAL)
        scale = first_item.get("scale", 1.0)
        if scale != 1.0:
            first_formula.scale(scale)
        old_content = VGroup(first_name, first_formula, first_info).arrange(DOWN, buff=1.5, center=True)
        old_content.move_to(ORIGIN)

        self.play(
            Write(first_name),
            Write(first_formula),
            FadeIn(first_info, shift=UP * 0.3),
            run_time=1.5
        )
        self.wait(0.5)

        for item in formulas_data[1:]:
            new_name = Text(item["name"], font="STXingkai", font_size=56, color=YELLOW)
            new_formula = MathTex(item["formula"], color=item.get("color", WHITE), font_size=54)
            new_info = Text(item["info"], font="STXingkai", font_size=42, color=TEAL)
            scale = item.get("scale", 1.0)
            if scale != 1.0:
                new_formula.scale(scale)
            new_content = VGroup(new_name, new_formula, new_info).arrange(DOWN, buff=1.5, center=True)
            new_content.move_to(ORIGIN)

            self.play(
                ReplacementTransform(old_content, new_content),
                run_time=0.8
            )
            self.wait(0.5)
            old_content = new_content

        self.play(FadeOut(old_content, shift=UP), run_time=0.5)

        self.wait(0.5)


# manim -pqh 合并物理公式.py PhysicsFormulasMerged
