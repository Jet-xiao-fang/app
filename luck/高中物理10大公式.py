from manim import *
import random  # 添加 random 模块导入

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantPhysicsFormulas(Scene):
    def construct(self):
        # 设置宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("高中物理必会10大公式", 
                    font_size=48,
                    color=BLUE
                    ).to_edge(UP, buff=1.5)
        # 2. 创建所有物理公式列表
        formulas = [
            MathTex(r"v = v_0 + at"),  # 1. 匀变速直线运动速度公式
            MathTex(r"s = v_0 t + \frac{1}{2}at^2"),  # 2. 匀变速直线运动位移公式
            MathTex(r"F = ma"),  # 3. 牛顿第二定律
            MathTex(r"F = G\frac{m_1 m_2}{r^2}"),  # 4. 万有引力定律
            MathTex(r"W = Fs \cos\theta"),  # 5. 功的计算公式
            MathTex(r"E_k = \frac{1}{2}mv^2"),  # 6. 动能公式
            MathTex(r"F = kx"),  # 7. 胡克定律
            MathTex(r"P = \frac{W}{t}"),  # 8. 功率公式
            MathTex(r"I = \frac{U}{R}"),  # 9. 欧姆定律
            MathTex(r"F = BIL \sin\theta")  # 10. 安培力公式
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("匀变速直线运动速度公式", font="Microsoft YaHei", font_size=24, color=YELLOW),  # 1
            Text("匀变速直线运动位移公式", font="Microsoft YaHei", font_size=24, color=RED),  # 2
            Text("牛顿第二定律", font="Microsoft YaHei", font_size=24, color=RED_C),  # 3
            Text("万有引力定律", font="Microsoft YaHei", font_size=24, color=GREEN),  # 4
            Text("功的计算公式", font="Microsoft YaHei", font_size=24, color=GREEN),  # 5
            Text("动能公式", font="Microsoft YaHei", font_size=24, color=GREEN),  # 6
            Text("胡克定律(弹簧)", font="Microsoft YaHei", font_size=24, color=RED),  # 7
            Text("功率公式", font="Microsoft YaHei", font_size=24, color=RED),  # 8
            Text("欧姆定律", font="Microsoft YaHei", font_size=24, color=BLUE),  # 9
            Text("安培力公式", font="Microsoft YaHei", font_size=24, color=BLUE)  # 10
        ]
        
        # 3. 调整公式大小
        for i, formula in enumerate(formulas):
            formula.scale(0.8 if len(formula.tex_string) > 30 else 1)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=48, color=BLUE) for i in range(10)]
        
        # 5. 创建完整的公式行（序号+公式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建公式和中文的组合
            formula_group = VGroup(formulas[i], chinese_texts[i]).arrange(DOWN, buff=0.3)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.3)
            
            formula_rows.append(row)
        
        # 6. 创建两列布局（每列5个公式）
        left_column = VGroup(*formula_rows[:5]).arrange(DOWN, buff=1, aligned_edge=LEFT).scale(0.8)
        right_column = VGroup(*formula_rows[5:]).arrange(DOWN, buff=1, aligned_edge=LEFT).scale(0.8)
        
        # 7. 将两列并排排列
        columns = VGroup(left_column, right_column).arrange(RIGHT, buff=1.2)
        columns.next_to(title, DOWN, buff=1.5)
        
        # 8. 动画展示
        self.play(Write(title))
        self.wait(0.5)
        
        # 逐个展示公式行（左列从上到下，然后右列从上到下）
        for i in range(5):
            self.play(
                Write(indices[i]),
                Write(formulas[i]),
                FadeIn(chinese_texts[i], shift=UP*0.5),
                run_time=1.5
            )
            self.wait(0.2)
            
        for i in range(5, 10):
            self.play(
                Write(indices[i]),
                Write(formulas[i]),
                FadeIn(chinese_texts[i], shift=UP*0.5),
                run_time=1.5
            )
            self.wait(0.2)
        
        # 9. 添加版权信息和装饰
        copyright = Text("高中物理核心公式 · 物理之美",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=BLUE_E).to_edge(DOWN).shift(UP*2)
        
        self.play(
            FadeIn(copyright, shift=UP),
            run_time=2
        )
        self.wait(3)
        
# manim -p 高中物理10大公式.py ImportantPhysicsFormulas