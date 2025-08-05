from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class JuniorHighMathFormulas(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("基础不定积分公式", 
                    font_size=36,
                    color=YELLOW).to_edge(UP, buff=1)
        
        # 2. 创建所有不定积分公式列表
        formulas = [
            MathTex(r"\int x^n \,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)"),  # 幂函数积分
            MathTex(r"\int e^x \,dx = e^x + C"),  # 指数函数积分
            MathTex(r"\int \frac{1}{x} \,dx = \ln |x| + C"),  # 倒数积分
            MathTex(r"\int \sin x \,dx = -\cos x + C"),  # 正弦积分
            MathTex(r"\int \cos x \,dx = \sin x + C"),  # 余弦积分
            MathTex(r"\int \sec^2 x \,dx = \tan x + C"),  # 正割平方积分
            MathTex(r"\int \csc^2 x \,dx = -\cot x + C"),  # 余割平方积分
            MathTex(r"\int \sec x \tan x \,dx = \sec x + C"),  # 正割正切积分
            MathTex(r"\int \frac{1}{1+x^2} \,dx = \arctan x + C"),  # 反正切积分
            MathTex(r"\int \frac{1}{\sqrt{1-x^2}} \,dx = \arcsin x + C")  # 反正弦积分
        ]
        size=20
        # 公式的中文解释
        chinese_texts = [
            Text("幂函数积分", font="Microsoft YaHei", font_size=size, color=BLUE),  
            Text("指数函数积分", font="Microsoft YaHei", font_size=size, color=GREEN),  
            Text("倒数积分", font="Microsoft YaHei", font_size=size, color=YELLOW),  
            Text("正弦积分", font="Microsoft YaHei", font_size=size, color=PINK),  
            Text("余弦积分", font="Microsoft YaHei", font_size=size, color=ORANGE),  
            Text("正割平方积分", font="Microsoft YaHei", font_size=size, color=PURPLE),  
            Text("余割平方积分", font="Microsoft YaHei", font_size=size, color=TEAL),  
            Text("正割正切积分", font="Microsoft YaHei", font_size=size, color=LIGHT_BROWN),  
            Text("反正切积分", font="Microsoft YaHei", font_size=size, color=MAROON),  
            Text("反正弦积分", font="Microsoft YaHei", font_size=size, color=GOLD)  
        ]
        
        # 3. 调整公式大小（根据长度缩放）
        for i, formula in enumerate(formulas):
            if i in [0, 8, 9]:  # 较长的公式
                formula.scale(0.7)
            elif i in [3, 4, 5, 6, 7]:  # 中等长度公式
                formula.scale(0.85)
            else:
                formula.scale(0.9)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=36) for i in range(10)]
        
        # 5. 创建完整的公式行（序号+公式+中文解释）
        formula_rows = []
        for i in range(10):
            # 创建公式和中文的组合
            formula_group = VGroup(formulas[i], chinese_texts[i]).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], formula_group).arrange(RIGHT, buff=0.3)
            formula_rows.append(row)
        
        # 6. 创建垂直布局（所有公式行垂直排列）
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        # 7. 整体布局（标题+所有行）
        all_rows.next_to(title, DOWN, buff=0.3).to_edge(LEFT, buff=1.0)  # 左侧留出空间给序号
        
        # 8. 调整位置确保在屏幕内
        if all_rows.get_bottom()[1] < -6.5:
            all_rows.scale(0.9)
            all_rows.next_to(title, DOWN, buff=0.5)
        
        # 9. 动画展示
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)
        
        # 逐个展示公式行
        for i in range(10):
            self.play(
                Write(indices[i]),
                Write(formulas[i]),
                FadeIn(chinese_texts[i], shift=UP*0.3),
                run_time=1.5
            )
            self.wait(0.2)
        
        # 10. 添加版权信息
        copyright = Text("微积分基础公式",
                        font="Microsoft YaHei",
                        font_size=30,
                        color=GREY_B).to_edge(DOWN).shift(UP*0.2)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)
        
# manim -pqh 不定积分.py JuniorHighMathFormulas -r 1080,1920