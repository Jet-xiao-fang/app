from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantLogarithmicFormulas(Scene):
    def construct(self):
        
        # 1. 创建标题
        title = Text("10个对数公式", 
                    font_size=48,
                    color=YELLOW).to_edge(UP, buff=1.5)
        
        # 2. 创建所有对数公式列表（每行一个公式）
        formulas = [
            MathTex(r"\log_b(xy) = \log_b x + \log_b y"),  # 1. 对数乘法公式
            MathTex(r"\log_b\left(\frac{x}{y}\right) = \log_b x - \log_b y"),  # 2. 对数除法公式
            MathTex(r"\log_b(x^a) = a \cdot \log_b x"),  # 3. 对数幂公式
            MathTex(r"\log_b b = 1"),  # 4. 底数对数
            MathTex(r"\log_b 1 = 0"),  # 5. 1的对数
            MathTex(r"b^{\log_b x} = x"),  # 6. 对数与指数的互逆关系
            MathTex(r"\log_b a = \frac{1}{\log_a b}"),  # 7. 倒数关系
            MathTex(r"\log_b a = \frac{\log_c a}{\log_c b}"),  # 8. 换底公式
            MathTex(r"\log_b x = \frac{\ln x}{\ln b}"),  # 9. 自然对数表达式
            MathTex(r"\log_b x = \frac{\log_k x}{\log_k b}")  # 10. 一般换底公式
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("对数乘法公式", font="Microsoft YaHei", font_size=18, color=BLUE),  # 1
            Text("对数除法公式", font="Microsoft YaHei", font_size=18, color=BLUE),  # 2
            Text("对数幂公式", font="Microsoft YaHei", font_size=18, color=BLUE),  # 3
            Text("底数对数", font="Microsoft YaHei", font_size=18, color=RED),  # 4
            Text("1的对数", font="Microsoft YaHei", font_size=18, color=RED),  # 5
            Text("对数与指数的互逆关系", font="Microsoft YaHei", font_size=18, color=RED),  # 6
            Text("倒数关系", font="Microsoft YaHei", font_size=18, color=PINK),  # 7
            Text("换底公式", font="Microsoft YaHei", font_size=18, color=GREEN),  # 8
            Text("自然对数表达式", font="Microsoft YaHei", font_size=18, color=GREEN),  # 9
            Text("一般换底公式", font="Microsoft YaHei", font_size=18, color=GREEN)  # 10
        ]
        
        # 3. 调整公式大小（保持与原模板相同的缩放逻辑）
        for i, formula in enumerate(formulas):
            if i in [1, 7, 8]:  # 较长的公式
                formula.scale(0.8)
            elif i in [0, 2, 3, 4, 5, 6, 9]:  # 中等长度
                formula.scale(0.9)
            else:
                formula.scale(0.8)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=48) for i in range(10)]
        
        # 5. 创建完整的公式行（序号+公式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建公式和中文的组合
            formula_group = VGroup(formulas[i], chinese_texts[i]).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.2)
            formula_rows.append(row)
        
        # 6. 创建垂直布局（所有公式行垂直排列）
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # 7. 整体布局（标题+所有行）
        all_rows.next_to(title, DOWN, buff=2).to_edge(LEFT, buff=0.1)  # 左侧留出空间给序号
        
        # 8. 调整位置确保在屏幕内
        if all_rows.get_bottom()[1] < -6.5:
            all_rows.scale(0.9)
            all_rows.next_to(title, DOWN, buff=0.3)
        
        # 9. 动画展示
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)
        
        # 逐个展示公式行
        for i in range(10):
            self.play(
                Write(indices[i]),
                Write(formulas[i]),
                FadeIn(chinese_texts[i], shift=UP*0.3),
                run_time=2
            )
            self.wait(0.2)
    
        self.wait(2)
        
# 运行命令：manim -p  对数公式.py ImportantLogarithmicFormulas