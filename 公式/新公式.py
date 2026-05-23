from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantPhysicsFormulas(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"

        # 公式数据列表，每个元素为字典，包含 name, formula, info, color, scale
        formulas_data = [
            {
                "name": "毕达哥拉斯定理",
                "formula": r"a^2 + b^2 = c^2",
                "info": "毕达哥拉斯 (公元前530年)",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "对数",
                "formula": r"\log(xy) = \log x + \log y",
                "info": "约翰·纳皮尔 (1610年)",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "微积分",
                "formula": r"\frac{d}{dt}f(t) = \lim_{h \to 0} \frac{f(t+h)-f(t)}{h}",
                "info": "艾萨克·牛顿 (1668年)",
                "color": WHITE,
                "scale": 1.2
            },
            {
                "name": "万有引力定律",
                "formula": r"F = G\frac{m_1 m_2}{r^2}",
                "info": "艾萨克·牛顿 (1687年)",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "虚数单位",
                "formula": r"i = \sqrt{-1}",
                "info": "莱昂哈德·欧拉 (1750年)",
                "color": WHITE,
                "scale": 2
            },
            {
                "name": "欧拉多面体公式",
                "formula": r"V - E + F = 2",
                "info": "莱昂哈德·欧拉 (1751年)",
                "color": WHITE,
                "scale": 2
            },
            {
                "name": "正态分布",
                "formula": r"\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}",
                "info": "卡尔·弗里德里希·高斯 (1810年)",
                "color": WHITE,
                "scale": 1.2
            },
            {
                "name": "波动方程",
                "formula": r"\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}",
                "info": "让·勒朗·达朗贝尔 (1746年)",
                "color": WHITE,
                "scale": 1.2
            },
            {
                "name": "傅里叶变换",
                "formula": r"\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx",
                "info": "让·巴普蒂斯·约瑟夫·傅里叶 (1822年)",
                "color": WHITE,
                "scale": 1.3
            },
            {
                "name": "纳维-斯托克斯方程",
                "formula": r"\rho \left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v} \cdot \nabla \mathbf{v}\right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}",
                "info": "克劳德-路易·纳维和乔治·斯托克斯 (19世纪)",
                "color": WHITE,
                "scale": 1
            },
            {
                "name": "麦克斯韦方程组",
                "formula": r"\begin{aligned} \nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\ \nabla \cdot \mathbf{B} &= 0 \\ \nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\ \nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \end{aligned}",
                "info": "詹姆斯·克拉克·麦克斯韦 (1865年)",
                "color": WHITE,
                "scale": 0.6
            },
            {
                "name": "热力学第二定律",
                "formula": r"dS \geq 0",
                "info": "路德维希·玻尔兹曼 (1874年)",
                "color": WHITE,
                "scale": 2
            },
            {
                "name": "相对论质能方程",
                "formula": r"E = mc^2",
                "info": "阿尔伯特·爱因斯坦 (1905年)",
                "color": WHITE,
                "scale": 2
            },
            {
                "name": "薛定谔方程",
                "formula": r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi",
                "info": "埃尔温·薛定谔 (1927年)",
                "color": WHITE,
                "scale": 1.5
            },
            {
                "name": "信息论熵公式",
                "formula": r"H = -\sum_x p(x) \log p(x)",
                "info": "克劳德·香农 (1949年)",
                "color": WHITE,
                "scale": 1.3
            },
            {
                "name": "混沌理论逻辑斯蒂映射",
                "formula": r"x_{t+1} = k x_t (1 - x_t)",
                "info": "罗伯特·梅 (1975年)",
                "color": WHITE,
                "scale": 1.3
            },
            {
                "name": "布莱克-舒尔斯方程",
                "formula": r"\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0",
                "info": "费雪·布莱克和迈伦·舒尔斯 (1973年)",
                "color": WHITE,
                "scale": 0.65
            }
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
        
        
# manim -pqh 新公式.py ImportantPhysicsFormulas