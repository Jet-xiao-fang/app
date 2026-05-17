from manim import *
from Logo import LogoScene  # 导入带 Logo 的基础场景类

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantPhysicsFormulas(LogoScene):
    def construct(self):
        # 设置宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        self.add_logo()  # 添加 Logo

        # 公式数据：(LaTeX公式, 中文名称, 发现者及年份)
        formulas_data = [
            (r"a^2 + b^2 = c^2", "毕达哥拉斯定理", "毕达哥拉斯 (公元前530年)"),
            (r"\log(xy) = \log x + \log y", "对数", "约翰·纳皮尔 (1610年)"),
            (r"\frac{d}{dt}f(t) = \lim_{h \to 0} \frac{f(t+h)-f(t)}{h}", "微积分", "艾萨克·牛顿 (1668年)"),
            (r"F = G\frac{m_1 m_2}{r^2}", "万有引力定律", "艾萨克·牛顿 (1687年)"),
            (r"i = \sqrt{-1}", "虚数单位", "莱昂哈德·欧拉 (1750年)"),
            (r"V - E + F = 2", "欧拉多面体公式", "莱昂哈德·欧拉 (1751年)"),
            (r"\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}", "正态分布", "卡尔·弗里德里希·高斯 (1810年)"),
            (r"\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}", "波动方程", "让·勒朗·达朗贝尔 (1746年)"),
            (r"\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx", "傅里叶变换", "让·巴普蒂斯·约瑟夫·傅里叶 (1822年)"),
            (r"\rho \left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v} \cdot \nabla \mathbf{v}\right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}", "纳维-斯托克斯方程", "克劳德-路易·纳维和乔治·斯托克斯 (19世纪)"),
            (r"\begin{aligned} \nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\ \nabla \cdot \mathbf{B} &= 0 \\ \nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\ \nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \end{aligned}", "麦克斯韦方程组", "詹姆斯·克拉克·麦克斯韦 (1865年)"),
            (r"dS \geq 0", "热力学第二定律", "路德维希·玻尔兹曼 (1874年)"),
            (r"E = mc^2", "相对论质能方程", "阿尔伯特·爱因斯坦 (1905年)"),
            (r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi", "薛定谔方程", "埃尔温·薛定谔 (1927年)"),
            (r"H = -\sum_x p(x) \log p(x)", "信息论熵公式", "克劳德·香农 (1949年)"),
            (r"x_{t+1} = k x_t (1 - x_t)", "混沌理论逻辑斯蒂映射", "罗伯特·梅 (1975年)"),
            (r"\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0", "布莱克-舒尔斯方程", "费雪·布莱克和迈伦·舒尔斯 (1973年)")
        ]

        previous_content = None

        for idx, (formula_tex, name_text, info_text) in enumerate(formulas_data, start=1):
            # 创建公式名称
            name = Text(name_text, font="Microsoft YaHei", font_size=56, color=YELLOW)
            # 创建公式
            formula = MathTex(formula_tex, color=WHITE, font_size=54)
            # 适当缩放公式（若过长则缩小）
            if len(formula_tex) > 50:
                formula.scale(0.5)
            # 创建发现人及年份信息
            info = Text(info_text, font="Microsoft YaHei", font_size=42, color=BLUE_C)

            # 垂直排列：名称在上，公式居中，信息在下
            content = VGroup(name, formula, info).arrange(DOWN, buff=1.5, center=True)
            content.move_to(ORIGIN)

            if idx == 1:
                # 第一个公式直接添加，不使用动画
                self.add(name, formula, info)
            else:
                # 清除上一个内容
                self.play(FadeOut(previous_content, shift=UP, scale=0.8), run_time=0.5)
                # 使用动画展示新公式
                self.play(
                    Write(name),
                    Write(formula),
                    FadeIn(info, shift=UP * 0.3),
                    run_time=1.5
                )

            self.wait(0.5)
            previous_content = content

        # 清除最后一个公式
        if previous_content:
            self.play(FadeOut(previous_content, shift=UP), run_time=0.5)

        self.wait(0.5)

# 运行命令：manim -pqh 新公式.py ImportantPhysicsFormulas