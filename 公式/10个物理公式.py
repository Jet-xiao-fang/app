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
        title = Text("10个重要物理公式", 
                    font_size=48,
                    color=BLUE
                    ).to_edge(UP, buff=1.5)
        # 2. 创建所有物理公式列表
        formulas = [
            MathTex(r"F = ma"),  # 1. 牛顿第二定律
            MathTex(r"E = mc^2"),  # 2. 质能方程
            MathTex(r"F = G\frac{m_1 m_2}{r^2}"),  # 3. 万有引力定律
            MathTex(r"V = IR"),  # 4. 欧姆定律
            MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}"),  # 5. 高斯定律
            MathTex(r"\Delta S \geqslant \frac{Q}{T}"),  # 6. 热力学第二定律
            MathTex(r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi"),  # 7. 薛定谔方程
            MathTex(r"F = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})"),  # 8. 洛伦兹力
            MathTex(r"\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}"),  # 9. 透镜方程
            MathTex(r"E = h\nu")  # 10. 光子能量
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("牛顿第二定律", font="Microsoft YaHei", font_size=24, color=YELLOW),  # 1
            Text("爱因斯坦质能方程", font="Microsoft YaHei", font_size=24, color=RED),  # 2
            Text("万有引力定律", font="Microsoft YaHei", font_size=24, color=RED_C),  # 3
            Text("欧姆定律", font="Microsoft YaHei", font_size=24, color=GREEN),  # 4
            Text("高斯定律(电磁学)", font="Microsoft YaHei", font_size=24, color=GREEN),  # 5
            Text("热力学第二定律", font="Microsoft YaHei", font_size=24, color=GREEN),  # 6
            Text("薛定谔方程(量子力学)", font="Microsoft YaHei", font_size=24, color=RED),  # 7
            Text("洛伦兹力公式", font="Microsoft YaHei", font_size=24, color=RED),  # 8
            Text("薄透镜方程", font="Microsoft YaHei", font_size=24, color=BLUE),  # 9
            Text("光子能量公式", font="Microsoft YaHei", font_size=24, color=BLUE)  # 10
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
        copyright = Text("物理之美 · 宇宙奥秘",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=BLUE_E).to_edge(DOWN).shift(UP*2)
        
        self.play(
            FadeIn(copyright, shift=UP),
            run_time=2
        )
        self.wait(3)
        
# manim -p 10个物理公式.py ImportantPhysicsFormulas