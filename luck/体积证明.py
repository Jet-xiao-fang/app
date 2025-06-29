from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class DetailedConeVolumeProof(Scene):
    def construct(self):
        # 标题和介绍
        title = Text("圆锥体积公式推导", font_size=48, color=YELLOW)
        subtitle = Text("使用微积分方法", font_size=36, color=BLUE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(
            title.animate.to_edge(UP),
            subtitle.animate.to_edge(UP).shift(DOWN*0.8),
            run_time=1
        )
        
        # 创建圆锥示意图
        cone_height = 4
        cone_width = 3
        apex = UP * cone_height + DOWN * 0.5
        base_left = LEFT * cone_width/2 + DOWN * 0.5
        base_right = RIGHT * cone_width/2 + DOWN * 0.5
        
        # 圆锥轮廓
        base_line = Line(base_left, base_right, color=BLUE, stroke_width=4)
        left_side = Line(base_left, apex, color=BLUE, stroke_width=4)
        right_side = Line(base_right, apex, color=BLUE, stroke_width=4)
        
        cone_group = VGroup(base_line, left_side, right_side)
        cone_group.center().shift(DOWN*0.5)
        
        # 高度标注
        height_line = DashedLine(base_left, base_left + UP*cone_height, color=RED)
        height_label = MathTex("h", color=RED).next_to(height_line, LEFT)
        
        # 半径标注
        radius_line = Line(ORIGIN, base_right, color=GREEN)
        radius_brace = Brace(radius_line, DOWN, color=GREEN)
        radius_label = MathTex("r", color=GREEN).next_to(radius_brace, DOWN)
        
        # 坐标系标注
        z_axis = Arrow(LEFT*cone_width, RIGHT*cone_width, color=WHITE, buff=0)
        z_label = MathTex("z").next_to(z_axis, RIGHT)
        
        self.play(Create(cone_group), run_time=1.5)
        self.wait(0.5)
        self.play(Create(height_line), Write(height_label))
        self.wait(0.5)
        self.play(GrowFromCenter(radius_brace), Write(radius_label))
        self.wait(0.5)
        self.play(Create(z_axis), Write(z_label))
        self.wait(1)
        
        # 相似三角形说明
        sim_triangle_text = Text("相似三角形原理", font_size=30, color=YELLOW).to_edge(UP).shift(DOWN*1.5)
        sim_explanation = MathTex(
            "\\frac{r(z)}{r} = \\frac{h - z}{h}",
            "\\Rightarrow", 
            "r(z) = r\\left(1 - \\frac{z}{h}\\right)"
        ).next_to(sim_triangle_text, DOWN)
        
        self.play(Write(sim_triangle_text))
        self.wait(1)
        self.play(Write(sim_explanation[0]))
        self.wait(2)
        self.play(Write(sim_explanation[1:]))
        self.wait(2)
        
        # 切片过程
        n_slices = 20
        dz = cone_height / n_slices
        slices = VGroup()
        
        for i in range(n_slices):
            z = i * dz
            radius = cone_width/2 * (1 - z/cone_height)
            slice = Rectangle(
                width=radius*2,
                height=dz,
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_color=BLUE_E,
                stroke_width=1
            )
            slice.move_to([0, z + dz/2 - cone_height/2, 0])
            slices.add(slice)
        
        slice_title = Text("将圆锥分成无数薄片", font_size=32, color=YELLOW).to_edge(UP).shift(DOWN*1.5)
        self.play(Transform(sim_triangle_text, slice_title), FadeOut(sim_explanation))
        self.play(Create(slices), run_time=3)
        self.wait(1)
        
        # 选择典型切片
        sample_slice = slices[10].copy()
        sample_slice.set_fill(YELLOW, opacity=0.8)
        sample_slice.set_stroke(RED, width=3)
        
        # 标注切片参数
        current_z = ValueTracker(10 * dz)
        z_value = always_redraw(lambda: 
            DecimalNumber(current_z.get_value(), num_decimal_places=2)
            .next_to(sample_slice, LEFT, buff=0.1)
        )
        
        radius_value = always_redraw(lambda: 
            DecimalNumber(cone_width/2 * (1 - current_z.get_value()/cone_height), 
                          num_decimal_places=2)
            .next_to(sample_slice, RIGHT, buff=0.1)
        )
        
        # 切片标注
        radius_indicator = Line(
            sample_slice.get_center(),
            sample_slice.get_right(),
            color=GREEN
        )
        
        dz_indicator = Line(
            sample_slice.get_top(),
            sample_slice.get_bottom(),
            color=RED
        )
        
        dz_brace = Brace(dz_indicator, LEFT, color=RED)
        dz_label = MathTex("dz", color=RED).next_to(dz_brace, LEFT)
        
        r_brace = Brace(radius_indicator, DOWN, color=GREEN)
        r_label = MathTex("r(z)", color=GREEN).next_to(r_brace, DOWN)
        
        self.play(
            Transform(slices[10], sample_slice),
            Create(radius_indicator),
            Create(dz_indicator),
            GrowFromCenter(dz_brace),
            Write(dz_label),
            GrowFromCenter(r_brace),
            Write(r_label),
            Write(z_value),
            Write(radius_value),
            run_time=2
        )
        
        # 展示z值变化
        self.play(
            current_z.animate.set_value(15 * dz),
            slices[10].animate.move_to([0, 15 * dz + dz/2 - cone_height/2, 0]),
            run_time=3,
            rate_func=there_and_back
        )
        
        # 薄片体积说明
        volume_text = Text("每个薄片的体积", font_size=32, color=YELLOW).to_edge(UP).shift(DOWN*1.5)
        volume_formula = MathTex(
            "dV = \\pi", "[r(z)]^2", "dz"
        ).next_to(volume_text, DOWN)
        volume_formula[1].set_color(GREEN)
        volume_formula[2].set_color(RED)
        
        self.play(
            Transform(slice_title, volume_text),
            Write(volume_formula),
            run_time=1.5
        )
        self.wait(2)
        
        # 积分概念说明
        integral_text = Text("将所有薄片体积相加（积分）", font_size=32, color=YELLOW).to_edge(UP).shift(DOWN*1.5)
        integral_formula = MathTex(
            "V = \\int_0^h dV = \\int_0^h \\pi [r(z)]^2 dz"
        ).next_to(integral_text, DOWN)
        
        self.play(
            Transform(volume_text, integral_text),
            Transform(volume_formula, integral_formula),
            run_time=1.5
        )
        self.wait(2)
        
        # 详细积分推导
        derivation_title = Text("积分计算过程", font_size=36, color=YELLOW).to_edge(UP)
        
        derivation_steps = VGroup(
            MathTex("V = \\int_0^h \\pi \\left[r \\left(1 - \\frac{z}{h}\\right)\\right]^2 dz"),
            MathTex("= \\pi r^2 \\int_0^h \\left(1 - \\frac{z}{h}\\right)^2 dz"),
            MathTex("= \\pi r^2 \\int_0^h \\left(1 - \\frac{2z}{h} + \\frac{z^2}{h^2}\\right) dz"),
            MathTex("= \\pi r^2 \\left[ z - \\frac{z^2}{h} + \\frac{z^3}{3h^2} \\right]_0^h"),
            MathTex("= \\pi r^2 \\left[ \\left(h - \\frac{h^2}{h} + \\frac{h^3}{3h^2}\\right) - (0) \\right]"),
            MathTex("= \\pi r^2 \\left[ h - h + \\frac{h}{3} \\right]"),
            MathTex("= \\pi r^2 \\cdot \\frac{h}{3}"),
            MathTex("= \\frac{1}{3} \\pi r^2 h", color=GREEN)
        )
        
        # 布局推导步骤
        derivation_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        derivation_steps.scale(0.9).next_to(derivation_title, DOWN, buff=0.5)
        
        # 逐步显示推导过程
        self.play(
            FadeOut(cone_group),
            FadeOut(slices),
            FadeOut(radius_indicator),
            FadeOut(dz_indicator),
            FadeOut(dz_brace),
            FadeOut(dz_label),
            FadeOut(r_brace),
            FadeOut(r_label),
            FadeOut(z_value),
            FadeOut(radius_value),
            Transform(integral_text, derivation_title),
            FadeOut(volume_formula),
            run_time=1.5
        )
        
        self.wait(1)
        
        # 创建步骤框
        step_boxes = VGroup()
        for step in derivation_steps:
            box = SurroundingRectangle(step, color=BLUE, buff=0.2)
            step_boxes.add(box)
        
        # 逐步显示推导
        for i, step in enumerate(derivation_steps):
            if i == 0:
                self.play(Write(step), Create(step_boxes[i]))
            else:
                self.play(Transform(derivation_steps[i-1].copy(), step), Create(step_boxes[i]))
            
            # 特别解释关键步骤
            if i == 2:
                expand_text = Text("展开平方项", font_size=28, color=YELLOW).next_to(step, RIGHT)
                self.play(Write(expand_text))
                self.wait(1)
                self.play(FadeOut(expand_text))
            
            if i == 3:
                integral_text = Text("逐项积分", font_size=28, color=YELLOW).next_to(step, RIGHT)
                self.play(Write(integral_text))
                self.wait(1)
                self.play(FadeOut(integral_text))
            
            if i == 4:
                eval_text = Text("代入上下限", font_size=28, color=YELLOW).next_to(step, RIGHT)
                self.play(Write(eval_text))
                self.wait(1)
                self.play(FadeOut(eval_text))
            
            if i == 5:
                simplify_text = Text("简化表达式", font_size=28, color=YELLOW).next_to(step, RIGHT)
                self.play(Write(simplify_text))
                self.wait(1)
                self.play(FadeOut(simplify_text))
            
            self.wait(1.5 if i < len(derivation_steps)-1 else 3)
        
        # 突出最终公式
        final_formula = derivation_steps[-1].copy()
        final_formula.scale(1.5).move_to(ORIGIN)
        final_box = SurroundingRectangle(final_formula, color=GREEN, buff=0.5, stroke_width=5)
        
        self.play(
            FadeOut(derivation_steps[:-1]),
            FadeOut(step_boxes),
            Transform(derivation_steps[-1], final_formula),
            Create(final_box),
            run_time=2
        )
        
        # 最终结论
        conclusion = Text("圆锥体积公式", font_size=40, color=YELLOW).next_to(final_formula, UP, buff=1)
        self.play(Write(conclusion))
        self.wait(3)
        
        # 记忆提示
        cylinder_text = Text("圆柱体积: ", font_size=30).to_edge(DOWN)
        cylinder_formula = MathTex("V_{\\text{圆柱}} = \\pi r^2 h").next_to(cylinder_text, RIGHT)
        cone_text = Text("圆锥体积: ", font_size=30, color=GREEN).next_to(cylinder_text, DOWN)
        cone_formula = MathTex("V_{\\text{圆锥}} = \\frac{1}{3} \\pi r^2 h", color=GREEN).next_to(cone_text, RIGHT)
        
        self.play(
            Write(cylinder_text),
            Write(cylinder_formula),
            run_time=1
        )
        self.wait(1)
        self.play(
            Write(cone_text),
            Write(cone_formula),
            run_time=1
        )
        self.wait(3)

# 渲染命令: manim -pqh --format=png 体积证明.py DetailedConeVolumeProof -r 1920,1080