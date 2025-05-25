from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class SqrtCalculation(Scene):
    def construct(self):
        # 初始标题
        title = Tex(r"计算 $\sqrt{96 \times 97 \times 98 \times 99 + 1}$", font_size=36)
        self.play(Write(title,run_time = 2)) # 放慢标题出现速度
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # 步骤1：四个连续整数
        step1 = Tex(
            r"设四个连续整数为 $n, n+1, n+2, n+3$，其中 $n=96$",
            font_size=30
        )
        step1.next_to(title, DOWN, buff=0.5)
        self.play(Write(step1,run_time = 2)) # 更慢写入
        self.wait(3) # 关键步骤延迟等待时间

        # 步骤2：表达式转换
        expr_original = MathTex(
            r"n(n+1)(n+2)(n+3) + 1",
            substrings_to_isolate=["n", "+1"]
        )
        expr_original.set_color_by_tex("n", YELLOW)
        expr_original.next_to(step1, DOWN, buff=0.8)
        self.play(Write(expr_original))
        self.wait(2)

        # 步骤3：展开为二次多项式
        expr_transform = MathTex(
            r"= (n^2 + 3n)(n^2 + 3n + 2) + 1",
            substrings_to_isolate=["n^2 + 3n"]
        )
        expr_transform.next_to(expr_original, DOWN, buff=0.5)
        self.play(Write(expr_transform))
        self.wait(3)

        # 步骤4：替换为x(x+2) + 1
        x_def = MathTex(r"x = n^2 + 3n", font_size=30)
        x_def.next_to(expr_transform, DOWN, buff=0.8)
        x_def.set_color(BLUE)
        self.play(Write(x_def))
        self.wait(2)

        expr_x = MathTex(r"x(x + 2) + 1 = x^2 + 2x + 1", font_size=30)
        expr_x.next_to(x_def, DOWN, buff=0.5)
        self.play(Write(expr_x))
        self.wait(2)

        # 步骤5：转换为完全平方
        square = MathTex(r"= (x + 1)^2", font_size=30)
        square.next_to(expr_x, DOWN, buff=0.5)
        self.play(Write(square))
        self.wait(2)

        # 步骤6：代入x的表达式
        final_expr = MathTex(
            r"= (n^2 + 3n + 1)^2",
            font_size=30
        )
        final_expr.next_to(square, DOWN, buff=0.5)
        self.play(Write(final_expr))
        self.wait(3)

        # 清空画面，聚焦计算部分
        self.play(
            FadeOut(step1),
            FadeOut(expr_original),
            FadeOut(expr_transform),
            FadeOut(x_def),
            FadeOut(expr_x),
            FadeOut(square),
            final_expr.animate.move_to(ORIGIN).scale(1.5)
        )
        self.wait(2)

        # 代入n=96的具体计算
        calc_n = MathTex(
            r"n = 96 &\Rightarrow n^2 + 3n + 1 \\",
            r"&= 96^2 + 3 \times 96 + 1 \\",
            r"&= 9216 + 288 + 1 \\",
            r"&= 9505",
            font_size=30
        )
        calc_n.next_to(final_expr, DOWN, buff=1)
        self.play(Write(calc_n))
        self.wait(3)

        # 最终结果
        result = MathTex(r"\sqrt{96 \times 97 \times 98 \times 99 + 1} = 9505", font_size=36)
        result.set_color(GREEN)
        self.play(FadeOut(title), FadeOut(final_expr), FadeOut(calc_n))
        self.play(Write(result))
        self.wait(4)

# manim -pqh 推导运算.py SqrtCalculation -r 1920,1080
