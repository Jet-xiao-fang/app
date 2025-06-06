from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantFormulas(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        
        # 1. 创建标题
        title = Text("世界上最重要的10个公式", 
                    font="Microsoft YaHei",
                    font_size=48,
                    gradient=(BLUE, GREEN))
        
        # 2. 创建公式列表 (左边列)
        formulas_left = [
            MathTex("E = mc^2"),  # 爱因斯坦质能方程
            MathTex("F = G\\frac{m_1 m_2}{r^2}"),  # 万有引力定律
            MathTex("e^{i\\pi} + 1 = 0"),  # 欧拉公式
            MathTex("i\\hbar\\frac{\\partial}{\\partial t}\\Psi = \\hat{H}\\Psi"),  # 
            Tex("陈平不等式：2000>3000")
        ]
        
        # 3. 创建公式列表 (右边列)
        formulas_right = [
            MathTex("\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}"),  # 麦克斯韦方程组
            MathTex("S = k_B \\ln \\Omega"),  # 玻尔兹曼熵公式
            MathTex("\\frac{\\mathrm{d}^2x}{\\mathrm{d}t^2} + \\omega_0^2 x = 0"),  # 简谐运动方程
            MathTex("\\Delta S = \\int \\frac{\\delta Q}{T}"),  # 热力学第二定律
            MathTex("R_{\\mu\\nu} - \\frac{1}{2}g_{\\mu\\nu}R + g_{\\mu\\nu}\\Lambda = \\frac{8\\pi G}{c^4}T_{\\mu\\nu}")  # 爱因斯坦场方程
        ]
        
        # 4. 调整公式大小（缩小复杂公式）
        for formula in formulas_left + formulas_right:
            formula.scale(0.7 if len(formula.tex_string) > 30 else 0.8)
        
        # 5. 创建公式列布局
        col1 = VGroup(*formulas_left).arrange(
            DOWN, buff=0.5, aligned_edge=LEFT
        )
        
        col2 = VGroup(*formulas_right).arrange(
            DOWN, buff=0.5, aligned_edge=LEFT
        )
        
        # 6. 水平排列两列公式
        columns = VGroup(col1, col2).arrange(
            RIGHT, buff=0.5, aligned_edge=UP
        )
        
        # 7. 创建整体布局
        layout = VGroup(title, columns).arrange(
            DOWN, buff=1.0
        ).to_edge(UP).shift(DOWN*0.5)
        
        # 8. 添加序号标记
        indices_left = [Tex(f"{i+1}.", font_size=28).next_to(formulas_left[i], LEFT) for i in range(5)]
        indices_right = [Tex(f"{i+6}.", font_size=28).next_to(formulas_right[i], LEFT) for i in range(5)]
        
        col1_with_index = VGroup(*[VGroup(indices_left[i], formulas_left[i]) for i in range(5)])
        col2_with_index = VGroup(*[VGroup(indices_right[i], formulas_right[i]) for i in range(5)])
        
        # 9. 重新布局
        columns = VGroup(col1_with_index, col2_with_index).arrange(
            RIGHT, buff=2.0, aligned_edge=UP
        )
        layout = VGroup(title, columns).arrange(DOWN, buff=1.0).to_edge(UP).shift(DOWN*0.5)
        
        # 10. 添加装饰元素
        underline = Underline(title, color=BLUE, buff=0.2)
        
        # 11. 动画展示
        self.play(Write(title), run_time=1.5)
        self.play(Create(underline))
        self.wait(0.5)
        
        # 逐个展示公式
        for i in range(5):
            # 展示左边公式
            self.play(Write(indices_left[i]), 
                      Write(formulas_left[i]), 
                      run_time=1.0)
            self.wait(0.3)
            
            # 展示右边公式
            self.play(Write(indices_right[i]), 
                      Write(formulas_right[i]), 
                      run_time=1.0)
            self.wait(0.3)
        
        # 12. 添加最终效果
        final_box = SurroundingRectangle(columns, color=YELLOW, buff=0.5)
        self.play(Create(final_box), run_time=2)
        
        # 13. 添加版权信息
        copyright = Text("数学之美",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_B).to_edge(DOWN)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)

# 运行命令：manim -pqh --format=png 圆形.py ImportantFormulas -r 1920,1080