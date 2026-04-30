from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class LongestFormula(Scene):
    def construct(self):
        # 设置宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        
        # 创建标题
        title = Text("物理学中最复杂的公式", 
                    font_size=48,
                    color="#FFD700",
                    weight=BOLD).to_edge(UP, buff=0.5)
        subtitle = Text("标准模型拉格朗日量", 
                      font_size=36,
                      color=YELLOW_C).next_to(title, DOWN, buff=0.2)
        

        # 创建公式（标准模型拉格朗日量的简化版）
        formula = MathTex(
            r"\mathcal{L}_{\text{SM}} = &-\frac{1}{4} F_{\mu\nu}^a F^{a\mu\nu} \\",
            r"&+ i \bar{\psi}_i \gamma^\mu D_\mu \psi_i \\",
            r"&+ (D_\mu \phi)^\dagger (D^\mu \phi) \\",
            r"&- V(\phi) \\",
            r"&+ \bar{\psi}_i y_{ij} \psi_j \phi \\",
            r"&+ \lambda \left( \phi^\dagger \phi - \frac{v^2}{2} \right)^2 \\",
            r"&+ \frac{1}{2} \partial_\mu h \partial^\mu h \\",
            r"&- \frac{1}{2} m_h^2 h^2 \\",
            r"&+ \sum_{f} \left( i \bar{f} \gamma^\mu \partial_\mu f - m_f \bar{f} f \right) \\",
            r"&- \frac{1}{4} B_{\mu\nu} B^{\mu\nu} \\",
            r"&- \frac{1}{4} W_{\mu\nu}^a W^{a\mu\nu} \\",
            r"&- \frac{1}{4} G_{\mu\nu}^a G^{a\mu\nu} \\",
            r"&+ \mathcal{L}_{\text{Yukawa}} \\",
            r"&+ \mathcal{L}_{\text{Higgs}} \\",
            r"&+ \theta_{\text{QCD}} \frac{g_s^2}{32\pi^2} G_{\mu\nu}^a \tilde{G}^{a\mu\nu} \\",
            font_size=32,
            color=WHITE
        )
        
        # 调整公式位置
        formula.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        formula.scale(0.8).next_to(subtitle, DOWN, buff=0.5)
        
        # 添加公式描述
        description = Text(
            "该公式描述了自然界中除引力外的所有基本相互作用",
            font="Microsoft YaHei",
            font_size=24,
            color=LIGHT_GRAY
        ).next_to(formula, DOWN, buff=0.5)
        
        # 添加粒子物理标准模型的组成部分
        components = VGroup(
            Text("• 电磁力", color=BLUE, font_size=24),
            Text("• 弱核力", color=GREEN, font_size=24),
            Text("• 强核力", color=RED, font_size=24),
            Text("• 费米子(物质粒子)", color=YELLOW, font_size=24),
            Text("• 玻色子(力载体)", color=PURPLE, font_size=24),
            Text("• 希格斯场", color=ORANGE, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(description, DOWN, buff=0.1)
        
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(0.5)
        
        # 逐行显示公式
        for i, line in enumerate(formula):
            self.play(
                Write(line),
                run_time=0.8 if i < 5 else 0.5
            )
            if i == 4 or i == 8 or i == 12:
                self.wait(0.5)
        
        self.play(FadeIn(description, shift=UP), run_time=1.5)
        self.wait(1)
        
        # 显示组成部分
        for comp in components:
            self.play(FadeIn(comp, shift=LEFT), run_time=0.7)
        
        self.wait(2)
        
        # 添加注释
        note = Text(
            "此公式包含量子电动力学(QED)、量子色动力学(QCD)\n和电弱统一理论(EWT)的核心内容",
            font="Microsoft YaHei",
            font_size=16,
            color=GREEN_B
        ).next_to(components, DOWN, buff=0.1)
        
        self.play(Write(note), run_time=2)
        self.wait(3)
        
        
# manim -pqh --format=png 最长公式.py LongestFormula -r 1920,1080