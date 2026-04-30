from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantTrigonometricFormulas(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("10个三角函数公式", 
                    font_size=48,
                    color=YELLOW).to_edge(UP, buff=1.5)
        
        # 2. 创建所有三角函数公式列表
        formulas = [
            MathTex(r"\sin^2 \theta + \cos^2 \theta = 1"),  # 1. 毕达哥拉斯恒等式
            MathTex(r"\sin(\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta"),  # 2. 正弦和差公式
            MathTex(r"\cos(\alpha \pm \beta) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta"),  # 3. 余弦和差公式
            MathTex(r"\tan(\alpha \pm \beta) = \frac{\tan \alpha \pm \tan \beta}{1 \mp \tan \alpha \tan \beta}"),  # 4. 正切和差公式
            MathTex(r"\sin 2\theta = 2 \sin \theta \cos \theta"),  # 5. 正弦倍角公式
            MathTex(r"\cos 2\theta = \cos^2 \theta - \sin^2 \theta"),  # 6. 余弦倍角公式
            MathTex(r"\tan 2\theta = \frac{2 \tan \theta}{1 - \tan^2 \theta}"),  # 7. 正切倍角公式
            MathTex(r"\sin \frac{\theta}{2} = \pm \sqrt{\frac{1 - \cos \theta}{2}}"),  # 8. 正弦半角公式
            MathTex(r"\cos \frac{\theta}{2} = \pm \sqrt{\frac{1 + \cos \theta}{2}}"),  # 9. 余弦半角公式
            MathTex(r"\sin \theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}, \quad \cos \theta = \frac{e^{i\theta} + e^{-i\theta}}{2}")  # 10. 欧拉公式
        ]
        
        # 公式的中文解释
        chinese_texts = [
            Text("毕达哥拉斯恒等式", font="Microsoft YaHei", font_size=16, color=BLUE),  # 1
            Text("正弦和差公式", font="Microsoft YaHei", font_size=16, color=GREEN),  # 2
            Text("余弦和差公式", font="Microsoft YaHei", font_size=16, color=GREEN),  # 3
            Text("正切和差公式", font="Microsoft YaHei", font_size=16, color=GREEN),  # 4
            Text("正弦倍角公式", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 5
            Text("余弦倍角公式", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 6
            Text("正切倍角公式", font="Microsoft YaHei", font_size=16, color=YELLOW),  # 7
            Text("正弦半角公式", font="Microsoft YaHei", font_size=16, color=PINK),  # 8
            Text("余弦半角公式", font="Microsoft YaHei", font_size=16, color=PINK),  # 9
            Text("欧拉公式表示", font="Microsoft YaHei", font_size=16, color=RED)  # 10
        ]
        
        # 3. 调整公式大小（根据长度缩放）
        for i, formula in enumerate(formulas):
            if i in [1, 2, 3, 9]:  # 较长的公式
                formula.scale(0.5)
            elif i in [0, 4, 5, 6, 7, 8]:  # 中等长度
                formula.scale(0.7)
            else:
                formula.scale(0.6)
        
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
        all_rows = VGroup(*formula_rows).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        # 7. 整体布局（标题+所有行）
        all_rows.next_to(title, DOWN, buff=2).to_edge(LEFT, buff=1.0)  # 左侧留出空间给序号
        
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
                run_time=1.5
            )
            self.wait(0.2)
        
        # 10. 添加版权信息
        copyright = Text("数学之美",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY_B).to_edge(DOWN).shift(UP*0.2)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)

# 运行命令：manim -p 三角函数公式.py ImportantTrigonometricFormulas