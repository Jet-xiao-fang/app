from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class LogarithmFormulas(Scene):
    def construct(self):
        # 设置深色星空背景
        self.camera.background_color = "#0F0B1A"
        
        # 1. 标题设计
        title = Text("重要对数公式", 
                    font="Microsoft YaHei",
                    font_size=48,
                    color="#FF7F50").set_shade(0.5)
        subtitle = Text("Essential Logarithmic Formulas", 
                       font="Arial",
                       font_size=28,
                       color=LIGHT_GRAY)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3).to_edge(UP)
        
        # 2. 核心公式展示
        formulas = VGroup(
            MathTex(r"\log_a(bc) = \log_a b + \log_a c"),
            MathTex(r"\log_a\left(\frac{b}{c}\right) = \log_a b - \log_a c"),
            MathTex(r"\log_a(b^c) = c \cdot \log_a b"),
            MathTex(r"\log_a b = \frac{\log_c b}{\log_c a}"),
            MathTex(r"a^{\log_a b} = b"),
        )
        
        # 添加中文说明
        descriptions = VGroup(
            Text("积的对数 = 对数的和", font="Microsoft YaHei", font_size=24, color=YELLOW_C),
            Text("商的对数 = 对数的差", font="Microsoft YaHei", font_size=24, color=YELLOW_C),
            Text("幂的对数 = 指数×底数对数", font="Microsoft YaHei", font_size=24, color=YELLOW_C),
            Text("不同底数对数的转换", font="Microsoft YaHei", font_size=24, color=YELLOW_C),
            Text("对数与指数的互逆关系", font="Microsoft YaHei", font_size=24, color=YELLOW_C)
        )
        
        # 组合公式和说明
        formula_group = VGroup()
        for formula, desc in zip(formulas, descriptions):
            group = VGroup(formula, desc).arrange(DOWN, buff=0.3)
            formula_group.add(group)
        
        formula_group.arrange(DOWN, buff=0.7, aligned_edge=LEFT).next_to(title_group, DOWN, buff=1)
        
        # 3. 动画展示
        self.play(
            FadeIn(title_group, shift=DOWN, scale=0.9),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 公式逐个显示
        for i, group in enumerate(formula_group):
            self.play(
                LaggedStart(
                    FadeIn(group[0], shift=UP),
                    FadeIn(group[1], shift=DOWN),
                    lag_ratio=0.3
                ),
                run_time=1.2
            )
            
            # 添加公式应用示例
            if i == 0:  # 乘法公式
                example = MathTex(r"\ln(2x) = \ln 2 + \ln x").next_to(group, DOWN, buff=0.4)
                self.play(Write(example), run_time=0.8)
                self.wait(0.5)
                self.play(FadeOut(example))
            
            self.wait(0.3)
        
        # 4. 关键性质总结
        properties = VGroup(
            Text("• 底数a>0且a≠1", font="Microsoft YaHei", font_size=20, color=BLUE_C),
            Text("• 真数必须大于0", font="Microsoft YaHei", font_size=20, color=BLUE_C),
            Text("• logₐ1=0, logₐa=1", font="Microsoft YaHei", font_size=20, color=BLUE_C)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        properties_box = SurroundingRectangle(
            properties, 
            color=BLUE_E, 
            buff=0.5,
            corner_radius=0.2
        ).set_fill(color=BLACK, opacity=0.7)
        
        properties_group = VGroup(properties_box, properties).next_to(formula_group, DOWN, buff=0.2)
        
        self.play(
            Create(properties_box),
            FadeIn(properties, shift=UP),
            run_time=1.5
        )
        self.wait(1)
        self.play(FadeOut(properties_box,properties, shift=UP))
        
        # 5. 自然对数与常用对数
        special_logs = VGroup(
            MathTex(r"\ln x = \log_e x \quad (e \approx 2.71828)").scale(1.1),
            MathTex(r"\lg x = \log_{10} x").scale(1.1)
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(properties_group, DOWN, buff=0.8)
        
        self.play(
            LaggedStart(
                *[Write(log) for log in special_logs],
                lag_ratio=0.7
            ),
            run_time=2
        )
        self.wait(1)
        
        # 6. 版权信息
        copyright = Text("@数学之美 | 对数公式原理与应用",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_A).to_edge(DOWN)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)
        
# 运行命令：manim -pqh --format=png 对数公式.py LogarithmFormulas -r 1920,1080