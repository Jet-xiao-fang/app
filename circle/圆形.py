from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class ImportantFormulas(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("世界上最重要的10个公式", 
                    font="Microsoft YaHei",
                    font_size=36,
                    color=YELLOW).to_edge(UP, buff=0.6)
        
        subtitle = Text("人类智慧的结晶，科学进步的基石",
                      font="Microsoft YaHei",
                      font_size=24,
                      color=GRAY).next_to(title, DOWN, buff=0.2)
        
        self.play(FadeIn(title, shift=UP*0.5, scale=0.8))
        self.play(Write(subtitle))
        self.wait(1)
        
        # 2. 创建公式列表
        formulas = [
            {
                "name": "勾股定理",
                "inventor": "毕达哥拉斯 (公元前6世纪)",
                "formula": MathTex("a^2 + b^2 = c^2"),
                "color": BLUE
            },
            {
                "name": "牛顿第二定律",
                "inventor": "艾萨克·牛顿 (1687)",
                "formula": MathTex(r"\mathbf{F} = m\mathbf{a}"),
                "color": GREEN
            },
            {
                "name": "万有引力定律",
                "inventor": "艾萨克·牛顿 (1687)",
                "formula": MathTex(r"F = G \frac{m_1 m_2}{r^2}"),
                "color": GREEN
            },
            {
                "name": "欧拉公式",
                "inventor": "莱昂哈德·欧拉 (1748)",
                "formula": MathTex(r"e^{i\pi} + 1 = 0"),
                "color": PURPLE
            },
            {
                "name": "热力学第二定律",
                "inventor": "鲁道夫·克劳修斯 (1850)",
                "formula": MathTex(r"\Delta S_{\text{总}} \geq 0"),
                "color": ORANGE
            },
            {
                "name": "麦克斯韦方程组",
                "inventor": "詹姆斯·麦克斯韦 (1865)",
                "formula": MathTex(r"""
                \begin{aligned}
                \nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
                \nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
                \nabla \cdot \mathbf{B} &= 0 \\
                \nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
                \end{aligned}
                """),
                "color": TEAL
            },
            {
                "name": "质能方程",
                "inventor": "阿尔伯特·爱因斯坦 (1905)",
                "formula": MathTex(r"E = mc^2"),
                "color": YELLOW
            },
            {
                "name": "薛定谔方程",
                "inventor": "埃尔温·薛定谔 (1926)",
                "formula": MathTex(r"i\hbar \frac{\partial}{\partial t} \Psi = \hat{H} \Psi"),
                "color": PINK
            },
            {
                "name": "香农信息熵",
                "inventor": "克劳德·香农 (1948)",
                "formula": MathTex(r"H(X) = -\sum p(x) \log_2 p(x)"),
                "color": MAROON
            },
            {
                "name": "哈勃定律",
                "inventor": "埃德温·哈勃 (1929)",
                "formula": MathTex(r"v = H_0 d"),
                "color": GOLD
            }
        ]
        
        # 3. 创建公式组（分为左右两列）
        left_column = VGroup()
        right_column = VGroup()
        
        # 4. 添加公式到两列
        for i, formula_data in enumerate(formulas):
            # 创建公式组
            formula_group = VGroup()
            
            # 添加公式名称
            name = Text(formula_data["name"], 
                       font="Microsoft YaHei",
                       font_size=22,
                       color=formula_data["color"])
            
            # 添加发明人信息
            inventor = Text(formula_data["inventor"], 
                          font="Microsoft YaHei",
                          font_size=18,
                          color=LIGHT_GRAY)
            
            # 添加公式
            formula = formula_data["formula"]
            formula.set_color(WHITE)
            
            # 调整复杂公式的大小
            if formula_data["name"] == "麦克斯韦方程组" or formula_data["name"] == "香农信息熵":
                formula.scale(0.6)
            elif len(formula.tex_string) > 30:
                formula.scale(0.7)
            else:
                formula.scale(0.8)
            
            # 组合元素
            formula_group.add(name, inventor, formula)
            formula_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            
            # 添加到左列或右列
            if i < 5:
                left_column.add(formula_group)
            else:
                right_column.add(formula_group)
        
        # 5. 排列两列
        left_column.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        right_column.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        
        # 6. 定位两列
        left_column.to_edge(LEFT, buff=0.5).shift(DOWN*0.5)
        right_column.to_edge(RIGHT, buff=0.3).shift(DOWN*0.5)
        
        # 逐项显示左列公式
        for item in left_column:
            self.play(FadeIn(item, shift=RIGHT*0.5, scale=0.9))
            self.wait(0.3)
        
        # 逐项显示右列公式
        for item in right_column:
            self.play(FadeIn(item, shift=LEFT*0.5, scale=0.9))
            self.wait(0.3)
        
        # 9. 添加强调效果
        highlight_rect = SurroundingRectangle(
            formulas[6]["formula"],  # 质能方程
            color=YELLOW,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(highlight_rect))
        self.wait(1)
        self.play(FadeOut(highlight_rect))
        
        # 10. 添加版权信息
        copyright = Text("数学之美 · 科学之光",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_B).to_edge(DOWN, buff=0.5)
        
        date = Text("2025年-爱物理的小方", 
                   font="Microsoft YaHei",
                   font_size=20,
                   color=GREY_B).next_to(copyright, DOWN, buff=0.2)
        
        self.play(
            FadeIn(copyright, shift=UP*0.3),
            FadeIn(date, shift=UP*0.3),
            run_time=1.5
        )
        
        # 11. 结束动画
        self.wait(3)
        self.play(
            FadeOut(left_column),
            FadeOut(right_column),
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(copyright),
            FadeOut(date)
        )
        self.wait(1)
        