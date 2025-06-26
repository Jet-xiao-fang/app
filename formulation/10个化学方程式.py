from manim import *
import random  # 添加 random 模块导入

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantChemistryEquations(Scene):  # 修改类名为化学方程
    def construct(self):
        # 设置宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("10个重要化学方程式", 
                    font_size=48,
                    color=BLUE
                    ).to_edge(UP, buff=1.5)
        
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
            Text("水的生成(燃烧反应)", font="Microsoft YaHei", font_size=24, color=YELLOW),  # 1
            Text("水的电解(氧化还原反应)", font="Microsoft YaHei", font_size=24, color=YELLOW),  # 2
            Text("甲烷燃烧(放热反应)", font="Microsoft YaHei", font_size=24, color=YELLOW),  # 3
            Text("光合作用(能量转化)", font="Microsoft YaHei", font_size=24, color=GREEN),  # 4
            Text("呼吸作用(氧化反应)", font="Microsoft YaHei", font_size=24, color=GREEN),  # 5
            Text("中和反应(pH变化)", font="Microsoft YaHei", font_size=24, color=GREEN),  # 6
            Text("金属置换反应", font="Microsoft YaHei", font_size=24, color=RED),  # 7
            Text("分解反应(热分解)", font="Microsoft YaHei", font_size=24, color=RED),  # 8
            Text("哈伯法合成氨", font="Microsoft YaHei", font_size=24, color=BLUE),  # 9
            Text("复分解反应", font="Microsoft YaHei", font_size=24, color=BLUE)  # 10
        ]
        
        # 3. 调整方程式大小（根据需要调整）
        for formula in formulas:
            formula.scale(0.8)  # 整体调小以适应复杂方程式
            
        # 特殊调整长方程式
        formulas[3].scale(0.7)  # 光合作用
        formulas[8].scale(0.75)  # 合成氨
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=48, color=BLUE) for i in range(10)]
        
        # 5. 创建完整的方程式行（序号+方程式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建方程式和中文的组合
            formula_group = VGroup(formulas[i], chinese_texts[i]).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.3)
            
            # 添加背景框
            box = SurroundingRectangle(row, color=BLUE_D, buff=0.3, corner_radius=0.2)
            box.set_fill(BLACK, opacity=0.6)
            box.set_stroke(width=2)
            
            # 将背景框和内容组合
            formula_rows.append(VGroup(box, row))
        
        # 6. 创建两列布局（每列5个方程式）
        left_column = VGroup(*formula_rows[:5]).arrange(DOWN, buff=0.8, aligned_edge=LEFT).scale(0.8)
        right_column = VGroup(*formula_rows[5:]).arrange(DOWN, buff=0.8, aligned_edge=LEFT).scale(0.8)
        
        # 7. 将两列并排排列
        columns = VGroup(left_column, right_column).arrange(RIGHT, buff=0.5)
        columns.next_to(title, DOWN, buff=1.0)
        
        # 8. 动画展示
        self.play(Write(title))
        self.wait(0.5)
        
        # 逐个展示方程式行（左列从上到下，然后右列从上到下）
        for i in range(5):
            self.play(
                Write(formula_rows[i], shift=UP*0.5),
                run_time=1.5
            )
            self.wait(0.1)
            
        for i in range(5, 10):
            self.play(
                Write(formula_rows[i], shift=UP*0.5),
                run_time=1.5
            )
            self.wait(0.1)
        
        # 9. 添加版权信息和装饰
        copyright = Text("化学之美 · 万物之源",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=BLUE_E).to_edge(DOWN).shift(UP*1.5)
        
        self.play(
            FadeIn(copyright, shift=UP),
            run_time=2
        )
        self.wait(3)
        
# # manim -pqh 10个化学方程式.py ImportantChemistryEquations -r 1920,1080