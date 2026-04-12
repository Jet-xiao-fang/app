from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class MathMultipleChoice(Scene):
    def construct(self):
        # 创建题目
        question_text = MathTex(
            r"\text{设函数 } f(x) = x^3 - 3x^2 + 4, \text{ 则 } f(x) \text{ 的极值情况是：}",
            font_size=36
        )
        question_text.to_edge(UP, buff=0.5)
        
        # 创建选项
        options = VGroup(
            MathTex(r"\text{A. } \text{有一个极大值和一个极小值}", font_size=32),
            MathTex(r"\text{B. } \text{只有极大值}", font_size=32),
            MathTex(r"\text{C. } \text{只有极小值}", font_size=32),
            MathTex(r"\text{D. } \text{没有极值}", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        options.next_to(question_text, DOWN, buff=0.8)
        
        # 显示题目
        self.play(Write(question_text))
        self.wait(1)
        
        # 显示选项
        for option in options:
            self.play(Write(option))
            self.wait(0.5)
        
        self.wait(2)
        
        # 添加解题思路
        solution_text = MathTex(r"\text{提示：求导后分析 } f'(x) = 3x(x-2) \text{ 的符号变化}", font_size=28)
        solution_text.to_edge(DOWN, buff=0.5)
        self.play(Write(solution_text))
        self.wait(3)
        
        # 强调正确答案
        correct_option = options[0]
        self.play(
            correct_option.animate.set_color(GREEN),
            Circumscribe(correct_option, color=GREEN, buff=0.1)
        )
        self.wait(2)

# manim -pqh 问题和答案.py MathMultipleChoice