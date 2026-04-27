from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080

class ImportantFormulas(Scene):
    def construct(self):

        formulas = [
            {
                "name": "勾股定理",
                "inventor": "毕达哥拉斯 (公元前6世纪)",
                "formula": MathTex("a^2 + b^2 = c^2"),
                "color": BLUE,
                "scale": 0.8
            },
            {
                "name": "牛顿第二定律",
                "inventor": "艾萨克·牛顿 (1687)",
                "formula": MathTex(r"\mathbf{F} = m\mathbf{a}"),
                "color": GREEN,
                "scale": 0.8
            },
            {
                "name": "万有引力定律",
                "inventor": "艾萨克·牛顿 (1687)",
                "formula": MathTex(r"F = G \frac{m_1 m_2}{r^2}"),
                "color": GREEN,
                "scale": 0.8

            },
            {
                "name": "欧拉公式",
                "inventor": "莱昂哈德·欧拉 (1748)",
                "formula": MathTex(r"e^{i\pi} + 1 = 0"),
                "color": PURPLE,
                "scale": 0.8
            },
            {
                "name": "热力学第二定律",
                "inventor": "鲁道夫·克劳修斯 (1850)",
                "formula": MathTex(r"\Delta S_{\text{总}} \geq 0"),
                "color": ORANGE,
                "scale": 0.8

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
                "color": TEAL,
                "scale": 0.3
            },
            {
                "name": "质能方程",
                "inventor": "阿尔伯特·爱因斯坦 (1905)",
                "formula": MathTex(r"E = mc^2"),
                "color": YELLOW,
                "scale": 0.8
            },
            {
                "name": "薛定谔方程",
                "inventor": "埃尔温·薛定谔 (1926)",
                "formula": MathTex(r"i\hbar \frac{\partial}{\partial t} \Psi = \hat{H} \Psi"),
                "color": PINK,
                "scale": 0.8
            },
            {
                "name": "香农信息熵",
                "inventor": "克劳德·香农 (1948)",
                "formula": MathTex(r"H(X) = -\sum p(x) \log_2 p(x)"),
                "color": MAROON,
                "scale": 0.6
            },
            {
                "name": "哈勃定律",
                "inventor": "埃德温·哈勃 (1929)",
                "formula": MathTex(r"v = H_0 d"),
                "color": GOLD,
                "scale": 0.8
            }
        ]
        
        # 创建公式组（分为左右两列）
        left_column = VGroup()
        right_column = VGroup()
        
        # 添加公式到两列
        for i, formula_data in enumerate(formulas):
            # 创建公式组
            formula_group = VGroup()
            
            # 创建序号 (1-based)
            number = Text(str(i+1), 
                         font="Microsoft YaHei",
                         font_size=20,
                         color=formula_data["color"],
                         weight=BOLD)
            
            # 创建公式名称
            name = Text(formula_data["name"], 
                       font="Microsoft YaHei",
                       font_size=22,
                       color=formula_data["color"])
            
            # 创建发明人信息
            inventor = Text(formula_data["inventor"], 
                          font="Microsoft YaHei",
                          font_size=16,
                          color=LIGHT_GRAY)
            
            # 创建公式
            formula = formula_data["formula"]
            formula.set_color(WHITE)
            formula.scale(formula_data["scale"])
            
            # 创建标题行 (序号 + 名称)
            title_row = VGroup(number, name)
            title_row.arrange(RIGHT, buff=0.15, aligned_edge=LEFT)
            
            # 组合所有元素
            formula_group.add(title_row, inventor, formula)
            formula_group.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            
            # 添加到左列或右列
            if i < 5:
                left_column.add(formula_group)
            else:
                right_column.add(formula_group)
        
        # 排列两列
        left_column.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        right_column.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        
        # 定位两列
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
        
        self.wait(3)

# 运行命令：manim -p 公式模版1.py ImportantFormulas    