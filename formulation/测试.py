from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class test(Scene):
    def construct(self):
        # Tex 支持中文较简单
        chinese_tex = Tex(r"物理学中的牛顿定律: $F = ma$")

        # MathTex 需要复杂配置
        chinese_math = MathTex(
            r"\text{物理学中的牛顿定律: } F = mb"
        )
        math = MathTex(r"E = ", r"m", r"c^2")
        math.set_color_by_tex("m", RED)  # 仅将m设为红色
        # MathTex - 自动进入数学模式，适合纯数学表达式
        math_ex = MathTex(r"\int_a^b f(x) dx = F(b) - F(a)")

        # Tex - 保持在文本模式，适合文字为主的标题
        text_ex = Tex(r"物理学: $\int_a^b f(x) dx$ 是积分定义")
        
        
        # MathTex 的多行对齐
        multi_line = MathTex(
        r"\begin{aligned} " 
        r"F &= ma \\ "
        r"v &= u + at "
        r"\end{aligned}"
        )

        # Tex 的多行需要手动处理
        # tex_multi = Tex(r"""
        # Line 1 \\ 
        # $\text{Line 2} \\ 
        # \text{Line 3}$
        # """, alignment="")
        
        self.add(multi_line)