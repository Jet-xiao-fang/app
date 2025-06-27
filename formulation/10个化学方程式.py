from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantChemistryEquations(Scene):
    def construct(self):
        # 设置宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("10个重要化学方程式", 
                    font_size=48,
                    color=BLUE
                    ).to_edge(UP, buff=1.0)
        
        # 2. 创建所有化学方程式列表
        formulas = [
            MathTex(r"2H_2 + O_2 \rightarrow 2H_2O"),  # 1. 水的生成
            MathTex(r"2H_2O \xrightarrow{\text{电解}} 2H_2 + O_2"),  # 2. 水的电解
            MathTex(r"CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O"),  # 3. 甲烷燃烧
            MathTex(r"6CO_2 + 6H_2O \xrightarrow{\text{光}} C_6H_{12}O_6 + 6O_2"),  # 4. 光合作用
            MathTex(r"C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O"),  # 5. 呼吸作用
            MathTex(r"HCl + NaOH \rightarrow NaCl + H_2O"),  # 6. 中和反应
            MathTex(r"Zn + H_2SO_4 \rightarrow ZnSO_4 + H_2"),  # 7. 锌与酸反应
            MathTex(r"CaCO_3 \xrightarrow{\Delta} CaO + CO_2"),  # 8. 石灰石分解
            MathTex(r"N_2 + 3H_2 \xrightarrow{\text{高温高压}} 2NH_3"),  # 9. 合成氨
            MathTex(r"NaCl + H_2SO_4 \rightarrow NaHSO_4 + HCl")  # 10. 盐与酸反应
        ]
        
        # 方程的中文解释
        chinese_texts = [
            Text("水的生成(燃烧反应)", font="Microsoft YaHei", font_size=22, color=YELLOW),  # 1
            Text("水的电解(氧化还原反应)", font="Microsoft YaHei", font_size=22, color=YELLOW),  # 2
            Text("甲烷燃烧(放热反应)", font="Microsoft YaHei", font_size=22, color=YELLOW),  # 3
            Text("光合作用(能量转化)", font="Microsoft YaHei", font_size=22, color=GREEN),  # 4
            Text("呼吸作用(氧化反应)", font="Microsoft YaHei", font_size=22, color=GREEN),  # 5
            Text("中和反应(pH变化)", font="Microsoft YaHei", font_size=22, color=GREEN),  # 6
            Text("金属置换反应", font="Microsoft YaHei", font_size=22, color=RED),  # 7
            Text("分解反应(热分解)", font="Microsoft YaHei", font_size=22, color=RED),  # 8
            Text("哈伯法合成氨", font="Microsoft YaHei", font_size=22, color=BLUE),  # 9
            Text("复分解反应", font="Microsoft YaHei", font_size=22, color=BLUE)  # 10
        ]
        
        # 3. 调整方程式大小（整体调小以适应屏幕）
        for formula, text in zip(formulas, chinese_texts):
            formula.scale(0.85)
            text.scale(0.9)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=32, color=BLUE) for i in range(10)]
        
        # 5. 创建完整的方程式行（序号+方程式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建方程式和中文的组合
            formula_group = VGroup(formulas[i], chinese_texts[i]).arrange(DOWN, buff=0.15)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.3)
            formula_rows.append(row)
        
        # 6. 将所有行垂直排列（调整为每行间隔稍小）
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        all_rows.scale(0.85).next_to(title, DOWN, buff=0.3)  # 减少间距
        
        # 7. 调整整个组的位置确保完全可见
        all_rows.center().to_edge(UP, buff=2.0)
        
        # 8. 动画展示
        self.play(Write(title))
        self.wait(0.5)
        
        # 一次性显示所有方程（前5个用FadeIn，后5个用Write）
        animations = []
        for i, row in enumerate(formula_rows):
            if i < 5:
                animations.append(FadeIn(row, shift=UP*0.3))
            else:
                animations.append(Write(row))
        
        # 执行动画
        self.play(
            LaggedStart(*animations, lag_ratio=0.3),
            run_time=15
        )
        self.wait(0.5)
        
        # 9. 添加版权信息（位置稍作调整）
        copyright = Text("@爱物理的小方",
                        font="Microsoft YaHei",
                        font_size=36,
                        color=RED_C).to_edge(DOWN, buff=1.2)
        
        self.play(
            FadeIn(copyright, shift=UP),
            run_time=2
        )
        self.wait(3)