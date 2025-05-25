from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class HarmonicSeriesProof(Scene):
    def construct(self):
        # 初始参数设置
        max_terms = 16  # 最大项数（建议设为2^n，如16=2^4）
        group_colors = [BLUE, GREEN, YELLOW, RED]  # 分组颜色

        # 初始化调和级数
        terms = [1/n for n in range(1, max_terms+1)]
        
        # 创建标题
        title = MathTex(
            r"\text{证明调和级数发散：} 1 + \frac{1}{2} + \frac{1}{3} + \cdots",
            color=YELLOW,
            font_size=36
        ).to_edge(UP)
        self.play(Write(title,run_time = 2))
        self.wait(2)

        # 创建调和级数的项（水平排列）
        # 优化1：动态计算项块尺寸
        term_blocks = VGroup()
        for i in range(max_terms):
            text = Text(f"1/{i+1}", font_size=24)  # 适当减小字体
            # 根据文本尺寸生成自适应矩形框
            rect = SurroundingRectangle(
                text, 
                color=WHITE, 
                fill_opacity=0.5,
                buff=0.15,  # 增加内边距
                stroke_width=2
            )
            block = VGroup(rect, text)
            term_blocks.add(block)
        
         # 优化2：调整排列间距
        term_blocks.arrange(RIGHT, buff=0.2).scale(0.8).shift(UP*1.5)
        self.play(FadeIn(term_blocks))
        self.wait(3)

        # 定义分组逻辑（每组2^k项）
        groups = VGroup()
        current_index = 0

        # 动画：分组并计算每组的和
        for k in range(0, 4):  # 示例分4组（对应max_terms=16）
            num_terms = 2**k if k > 0 else 1
            group = VGroup(*term_blocks[current_index : current_index + num_terms])
            
            # 为每组添加颜色框
            color = group_colors[k % len(group_colors)]
            group_box = SurroundingRectangle(
                group, color=color, buff=0.1, 
                stroke_width=2, fill_opacity=0.2
            )
            
            # 计算当前组的和
            sum_text = MathTex(
                r"\underbrace{> \frac{1}{2}}",
                font_size=24,
                color=color
            ).next_to(group_box, DOWN, buff=0.1)
            
            # 添加组注释
            group_label = MathTex(
                f"\\text{{第{k+1}组：}}",
                f"{num_terms} \\text{{项}}",
                font_size=16,
                color=color
            ).arrange(RIGHT).next_to(group_box, UP, buff=0.1)
            
            # 合并元素
            group_vg = VGroup(group_box, group_label, sum_text)
            groups.add(group_vg)
            
            # 动画：显示分组
            self.play(
                Create(group_box),
                FadeIn(group_label),
                run_time=1
            )
            self.play(Write(sum_text))
            self.wait(2)
            
            current_index += num_terms

        # 动画：显示总和的增长
        sum_expression = MathTex(
            r"H(16) = \sum_{k=1}^{16} \frac{1}{k} > 1 + \frac{1}{2} \times 4 = 3",
            color=RED,
            font_size=36
        ).shift(DOWN*2)
        
        self.play(Write(sum_expression))
        self.wait(3)

        # 结论文本
        conclusion = Tex(
            r"每增加一组，总和至少增加 $\frac{1}{2}$，因此当 $n \to \infty$ 时 $H(n) \to \infty$",
            color=BLUE,
            font_size=32
        ).next_to(sum_expression, DOWN, buff=0.5)
        
        self.play(FadeIn(conclusion))
        self.wait(3)

#   manim -pqh 调和级数证明.py HarmonicSeriesProof -r 1920,1080