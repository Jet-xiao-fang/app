from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class SeniorHighMathFormulas(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("高中数学核心公式", 
                    font_size=48,
                    color=YELLOW).to_edge(UP, buff=1)
        
        # 2. 创建所有高中数学公式列表（符合中国教学大纲）
        formulas = [
            MathTex(r"f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) - f(x)}{\Delta x}"),  # 导数定义
            MathTex(r"\int_a^b f(x) \,dx = F(b) - F(a)"),  # 微积分基本定理
            MathTex(r"e^{i\pi} + 1 = 0"),  # 欧拉公式
            MathTex(r"\sin(\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta"),  # 正弦和角公式
            MathTex(r"\cos(\alpha \pm \beta) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta"),  # 余弦和角公式
            MathTex(r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \theta"),  # 向量点积
            MathTex(r"\frac{d}{dx} e^x = e^x"),  # 指数函数导数
            MathTex(r"\sum_{k=1}^n k = \frac{n(n+1)}{2}"),  # 等差数列求和
            MathTex(r"S_n = \frac{a_1(1-q^n)}{1-q}"),  # 等比数列求和
            MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1")  # 椭圆标准方程
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("导数定义", font="Microsoft YaHei", font_size=24, color=BLUE),  
            Text("微积分基本定理", font="Microsoft YaHei", font_size=24, color=GREEN),  
            Text("欧拉公式", font="Microsoft YaHei", font_size=24, color=YELLOW),  
            Text("正弦和角公式", font="Microsoft YaHei", font_size=24, color=PINK),  
            Text("余弦和角公式", font="Microsoft YaHei", font_size=24, color=ORANGE),  
            Text("向量点积公式", font="Microsoft YaHei", font_size=24, color=PURPLE),  
            Text("指数函数导数", font="Microsoft YaHei", font_size=24, color=TEAL),  
            Text("等差数列求和", font="Microsoft YaHei", font_size=24, color=LIGHT_BROWN),  
            Text("等比数列求和", font="Microsoft YaHei", font_size=24, color=MAROON),  
            Text("椭圆标准方程", font="Microsoft YaHei", font_size=24, color=GOLD)  
        ]
        
        # 3. 调整公式大小（根据长度缩放）
        for i, formula in enumerate(formulas):
            if i in [0, 3, 4]:  # 较长的公式
                formula.scale(0.7)
            elif i in [2, 5, 9]:  # 中等长度公式
                formula.scale(0.8)
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
        all_rows.next_to(title, DOWN, buff=1.0).to_edge(LEFT, buff=2.0)  # 左侧留出空间给序号
        
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
        
        self.wait(3)

# 运行命令：manim -pqh --format=png 高中数学.py SeniorHighMathFormulas