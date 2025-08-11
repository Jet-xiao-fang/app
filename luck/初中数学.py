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
        title = Text("初中数学核心公式", 
                    font_size=48,
                    color=YELLOW).to_edge(UP, buff=1.5)
        
        # 2. 创建所有初中数学公式列表
        formulas = [
            MathTex(r"a^2 + b^2 = c^2"),  # 勾股定理
            MathTex(r"(a + b)^2 = a^2 + 2ab + b^2"),  # 完全平方公式
            MathTex(r"a^2 - b^2 = (a + b)(a - b)"),  # 平方差公式
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),  # 二次方程求根公式
            MathTex(r"a^3 + b^3 = (a + b)(a^2 - ab + b^2)"),  # 立方和公式
            MathTex(r"a^3 - b^3 = (a - b)(a^2 + ab + b^2)"),  # 立方差公式
            MathTex(r"\frac{a}{b} = \frac{c}{d} \Rightarrow ad = bc"),  # 比例性质
            MathTex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}"),  # 两点距离
            MathTex(r"y = kx + b"),  # 一次函数
            MathTex(r"y = ax^2 + bx + c")  # 二次函数
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("勾股定理", font="Microsoft YaHei", font_size=24, color=BLUE),  
            Text("完全平方公式", font="Microsoft YaHei", font_size=24, color=GREEN),  
            Text("平方差公式", font="Microsoft YaHei", font_size=24, color=YELLOW),  
            Text("二次方程求根公式", font="Microsoft YaHei", font_size=24, color=PINK),  
            Text("立方和公式", font="Microsoft YaHei", font_size=24, color=ORANGE),  
            Text("立方差公式", font="Microsoft YaHei", font_size=24, color=PURPLE),  
            Text("比例基本性质", font="Microsoft YaHei", font_size=24, color=TEAL),  
            Text("平面两点距离公式", font="Microsoft YaHei", font_size=24, color=LIGHT_BROWN),  
            Text("一次函数表达式", font="Microsoft YaHei", font_size=24, color=MAROON),  
            Text("二次函数表达式", font="Microsoft YaHei", font_size=24, color=GOLD)  
        ]
        
        # 3. 调整公式大小（根据长度缩放）
        for i, formula in enumerate(formulas):
            if i == 3:  # 二次方程求根公式较长
                formula.scale(0.7)
            elif i == 7:  # 两点距离公式
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
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # 7. 整体布局（标题+所有行）
        all_rows.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=2.0)  # 左侧留出空间给序号
        
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
        copyright = Text("初中数学核心知识点",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_B).to_edge(DOWN).shift(UP*0.2)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)

# 运行命令：manim -pqh --format=png 初中数学.py JuniorHighMathFormulas
