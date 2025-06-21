from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantFormulas(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("10个必会的不定积分公式", 
                    font="Microsoft YaHei",
                    font_size=30,
                    color=BLUE).to_edge(UP, buff=1.5)
        
        # 2. 创建所有公式列表（每行一个公式）
        formulas = [
            MathTex(r"\int x^n \,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)"),  # 1. 幂函数不定积分
            MathTex(r"\int e^x \, dx = e^x + C"),  # 2. 自然指数函数不定积分
            MathTex(r"\int \sin x \, dx = -\cos x + C"),  # 3. 正弦函数不定积分
            MathTex(r"\int \cos x \, dx = \sin x + C"),  # 4. 余弦函数不定积分
            MathTex(r"\int (f(x) + g(x)) \, dx = \int f(x) \, dx + \int g(x) \, dx"),  # 5. 不定积分的线性性质
            MathTex(r"\int \frac{1}{x} \,dx = \ln |x| + C"),  # 6. 倒数积分
            MathTex(r"\int a^x \,dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)"),  # 7. 指数函数不定积分
            MathTex(r"\int \tan x \,dx = -\ln |\cos x| + C = \ln |\sec x| + C"),  # 8. 正切函数积分
            MathTex(r"\int \cot x \,dx = \ln |\sin x| + C"),  # 9. 余切函数积分
            MathTex(r"\int \frac{1}{\sqrt{a^2 - x^2}} \,dx = \arcsin \frac{x}{a} + C \quad (a > 0)")  # 10. 平方差积分
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("幂函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 1
            Text("自然指数函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 2
            Text("正弦函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 3
            Text("余弦函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 4
            Text("不定积分的线性性质", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 5
            Text("倒数积分", font="Microsoft YaHei", font_size=16, color=GREEN),  # 6
            Text("指数函数不定积分", font="Microsoft YaHei", font_size=16, color=GREEN),  # 7
            Text("正切函数积分", font="Microsoft YaHei", font_size=16, color=GREEN),  # 8
            Text("余切函数积分", font="Microsoft YaHei", font_size=16, color=GREEN),  # 9
            Text("平方差积分", font="Microsoft YaHei", font_size=16, color=GREEN)  # 10
        ]
        
        # 3. 调整公式大小（缩小复杂公式）
        for i, formula in enumerate(formulas):
            if i in [0, 4, 7, 9]:  # 较长的公式
                formula.scale(0.6)
            else:
                formula.scale(0.7)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=48) for i in range(10)]
        
        # 5. 创建完整的公式行（序号+公式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建公式和中文的组合
            formula_group = VGroup(formulas[i], chinese_texts[i]).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.3)
            formula_rows.append(row)
        
        # 6. 创建垂直布局（所有公式行垂直排列）
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # 7. 整体布局（标题+所有行）
        all_rows.next_to(title, DOWN, buff=0.8).to_edge(LEFT, buff=1.0)  # 左侧留出空间给序号
        
        # 8. 调整位置确保在屏幕内
        if all_rows.get_bottom()[1] < -6.5:
            all_rows.scale(0.9)
            all_rows.next_to(title, DOWN, buff=0.3)
        
        # 9. 动画展示
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # 逐个展示公式行
        for i in range(10):
            self.play(
                Write(indices[i]),
                Write(formulas[i]),
                FadeIn(chinese_texts[i], shift=UP*0.3),
                run_time=1.0
            )
            self.wait(0.1)
        
        # 10. 添加版权信息
        copyright = Text("数学之美",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_B).to_edge(DOWN).shift(UP*0.2)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)

# 运行命令：manim -pqh --format=png 不定积分.py ImportantFormulas -r 1920,1080