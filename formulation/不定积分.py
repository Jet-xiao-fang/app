from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantFormulas(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        # 1. 创建标题
        title = Text("10个必会的不定积分公式", 
                    font="Microsoft YaHei",
                    font_size=30,
                    color=BLUE)
        
        # 2. 创建公式列表 (左边列)
        formulas_left = [
            MathTex(r"\int x^n \,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)"),  # 幂函数不定积分
            MathTex(r"\int e^x \, dx = e^x + C"),  # 指数函数不定积分
            MathTex(r"\int \sin x \, dx = -\cos x + C"),  # 正弦函数不定积分
            MathTex(r"\int \cos x \, dx = \sin x + C"),  # 余弦函数不定积分
            MathTex(r"\int (f(x) + g(x)) \, dx = \int f(x) \, dx + \int g(x) \, dx"),  # 不定积分的线性性质
        ]
        
        # 左边公式的中文解释
        chinese_left = [
            Text("幂函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),
            Text("自然指数函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),
            Text("正弦函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),
            Text("余弦函数不定积分", font="Microsoft YaHei", font_size=16, color=YELLOW),
            Text("不定积分的线性性质", font="Microsoft YaHei", font_size=16, color=YELLOW)
        ]
        
        # 3. 创建公式列表 (右边列)
        formulas_right = [
            MathTex(r"\int \frac{1}{x} \,dx = \ln |x| + C"),  # 倒数积分
            MathTex(r"\int a^x \,dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)"),  # 指数函数不定积分
            MathTex(r"\int \tan x \,dx = -\ln |\cos x| + C = \ln |\sec x| + C \\"),  # 正切与余切积分
            MathTex(r"\int \cot x \,dx = \ln |\sin x| + C"),  # 正切与余切积分
            MathTex(r"\int \frac{1}{\sqrt{a^2 - x^2}} \,dx = \arcsin \frac{x}{a} + C \quad (a > 0) \\")  # 平方差与平方和积分
        ]
        
        # 右边公式的中文解释
        chinese_right = [
            Text("倒数积分", font="Microsoft YaHei", font_size=16, color=GREEN),
            Text("指数函数不定积分", font="Microsoft YaHei", font_size=16, color=GREEN),
            Text("正切函数积分", font="Microsoft YaHei", font_size=16, color=GREEN),
            Text("余切函数积分", font="Microsoft YaHei", font_size=16, color=GREEN),
            Text("平方差积分", font="Microsoft YaHei", font_size=16, color=GREEN)
        ]
        
        # 4. 调整公式大小（缩小复杂公式）
        for formula in formulas_left + formulas_right:
            formula.scale(0.5 if len(formula.tex_string) > 30 else 0.8)
        
        # 5. 创建公式+中文的组合
        formula_groups_left = []
        for i in range(5):
            group = VGroup(formulas_left[i], chinese_left[i]).arrange(DOWN, buff=0.2)
            formula_groups_left.append(group)
        
        formula_groups_right = []
        for i in range(5):
            group = VGroup(formulas_right[i], chinese_right[i]).arrange(DOWN, buff=0.2)
            formula_groups_right.append(group)
        
        # 6. 创建公式列布局
        col1 = VGroup(*formula_groups_left).arrange(
            DOWN, buff=0.3, aligned_edge=LEFT
        )
        
        col2 = VGroup(*formula_groups_right).arrange(
            DOWN, buff=0.3, aligned_edge=LEFT
        )
        
        # 7. 水平排列两列公式
        columns = VGroup(col1, col2).arrange(
            RIGHT, buff=1.2, aligned_edge=ORIGIN
        )
        
        # 8. 创建整体布局 - 整体向上移动0.3单位
        layout = VGroup(title, columns).arrange(
            DOWN, buff=0.2  # 减少标题与公式的间距
        ).to_edge(UP).shift(UP*0.1)  # 整体向上移动
        
        # 9. 添加序号标记
        indices_left = [Tex(f"{i+1}.", font_size=28).next_to(formula_groups_left[i], LEFT) for i in range(5)]
        indices_right = [Tex(f"{i+6}.", font_size=28).next_to(formula_groups_right[i], LEFT) for i in range(5)]
        
        col1_with_index = VGroup(*[VGroup(indices_left[i], formula_groups_left[i]) for i in range(5)])
        col2_with_index = VGroup(*[VGroup(indices_right[i], formula_groups_right[i]) for i in range(5)])
        
        # 10. 重新布局
        columns = VGroup(col1_with_index, col2_with_index).arrange(
            RIGHT, buff=2.0, aligned_edge=UP
        )
        layout = VGroup(title, columns).arrange(
            DOWN, buff=0.2
        ).to_edge(UP)  # 再次确保整体向上移动
        
        # 11. 检查并压缩空间
        if columns.get_bottom()[1] < -5:  # 如果内容太低
            layout.shift(UP * 0.5)  # 再向上移动
            title.scale(0.95)  # 稍微缩小标题
            columns.scale(0.95)  # 稍微缩小公式
        
        # 14. 动画展示
       
        self.play(Write(title), run_time=1.5)
    
        self.wait(0.5)
        
        # 15. 逐个展示公式（先左后右交替）
        for i in range(5):
            # 展示左边公式和中文
            self.play(
                Write(indices_left[i]), 
                Write(formulas_left[i]),
                FadeIn(chinese_left[i], shift=UP*0.5),
                run_time=1.5
            )
            self.wait(0.2)
            
            # 展示右边公式和中文
            self.play(
                Write(indices_right[i]), 
                Write(formulas_right[i]),
                FadeIn(chinese_right[i], shift=UP*0.5),
                run_time=1.5
            )
            self.wait(0.2)
        
        # 16. 添加金色边框
        golden_box = SurroundingRectangle(
            columns, 
            color=GOLD, 
            buff=0.3, 
            stroke_width=3
        )
        self.play(Create(golden_box), run_time=2)
        
        # 17. 添加版权信息（位置上移）
        copyright = Text("数学之美",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_B).to_edge(DOWN).shift(UP*0.2)  # 版权信息上移
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)

# 运行命令：manim -pqh --format=png 不定积分.py ImportantFormulas -r 1920,1080