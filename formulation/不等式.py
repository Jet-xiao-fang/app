from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantInequalities(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("10个重要不等式", 
                    font_size=48,
                    color=YELLOW).to_edge(UP, buff=1)
        
        # 2. 创建所有不等式列表（每行一个不等式）
        inequalities = [
            MathTex(r"\frac{a+b}{2} \geqslant \sqrt{ab} \quad (a,b > 0)"),  # 1. 算术-几何平均不等式
            MathTex(r"\left( \sum_{i=1}^n a_i^2 \right) \left( \sum_{i=1}^n b_i^2 \right) \geqslant \left( \sum_{i=1}^n a_i b_i \right)^2"),  # 2. 柯西-施瓦茨不等式
            MathTex(r"\frac{a_1 + a_2 + \cdots + a_n}{n} \geqslant \sqrt[n]{a_1 a_2 \cdots a_n} \quad (a_i > 0)"),  # 3. n元AM-GM不等式
            MathTex(r"|x + y| \leqslant |x| + |y|"),  # 4. 三角不等式
            MathTex(r"a^2 + b^2 \geqslant 2ab"),  # 5. 基本不等式
            MathTex(r"\frac{1}{a} + \frac{1}{b} \geqslant \frac{4}{a+b} \quad (a,b > 0)"),  # 6. 调和平均不等式
            MathTex(r"\left( \sum_{i=1}^n |a_i + b_i|^p \right)^{1/p} \leqslant \left( \sum_{i=1}^n |a_i|^p \right)^{1/p} + \left( \sum_{i=1}^n |b_i|^p \right)^{1/p}"),  # 7. 闵可夫斯基不等式
            MathTex(r"\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \geqslant \frac{3}{2} \quad (a,b,c > 0)"),  # 8. Nesbitt不等式
            MathTex(r"e^x \geqslant 1 + x \quad (x \in \mathbb{R})"),  # 9. 指数不等式
            MathTex(r"\ln(1+x) \leqslant x \quad (x > -1)")  # 10. 对数不等式
        ]
        
        # 不等式的中文解释
        chinese_texts = [
            Text("算术-几何平均不等式", font="Microsoft YaHei", font_size=18, color=RED),  # 1
            Text("柯西-施瓦茨不等式", font="Microsoft YaHei", font_size=18, color=RED),  # 2
            Text("n元AM-GM不等式", font="Microsoft YaHei", font_size=18, color=BLUE),  # 3
            Text("三角不等式", font="Microsoft YaHei", font_size=18, color=BLUE),  # 4
            Text("基本不等式", font="Microsoft YaHei", font_size=18, color=ORANGE),  # 5
            Text("调和平均不等式", font="Microsoft YaHei", font_size=18, color=ORANGE),  # 6
            Text("闵可夫斯基不等式", font="Microsoft YaHei", font_size=18, color=PURPLE),  # 7
            Text("Nesbitt不等式", font="Microsoft YaHei", font_size=18, color=PURPLE),  # 8
            Text("指数不等式", font="Microsoft YaHei", font_size=18, color=GREEN),  # 9
            Text("对数不等式", font="Microsoft YaHei", font_size=18, color=GREEN)  # 10
        ]
        
        # 3. 调整公式大小（缩小复杂公式）
        for i, formula in enumerate(inequalities):
            if i in [1, 2, 6]:  # 较长的公式
                formula.scale(0.6)
            elif i in [0, 3, 4, 5, 7, 8, 9]:  # 中等长度
                formula.scale(0.8)
            else:
                formula.scale(0.5)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=48) for i in range(10)]
        
        # 5. 创建完整的公式行（序号+公式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建公式和中文的组合
            formula_group = VGroup(inequalities[i], chinese_texts[i]).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.3)
            formula_rows.append(row)
        
        # 6. 创建垂直布局（所有公式行垂直排列）
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        # 7. 整体布局（标题+所有行）
        all_rows.next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1.0)  # 左侧留出空间给序号
        
        # 8. 调整位置确保在屏幕内
        if all_rows.get_bottom()[1] < -6.5:
            all_rows.scale(0.9)
            all_rows.next_to(title, DOWN, buff=0.3)
        
        # 9. 动画展示
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        
        # 逐个展示公式行
        for i in range(10):
            self.play(
                Write(indices[i]),
                Write(inequalities[i]),
                FadeIn(chinese_texts[i], shift=UP*0.3),
                run_time=1.5
            )
            self.wait(0.2)
        self.wait(1)
        
# 运行命令：manim -pqh 不等式.py ImportantInequalities