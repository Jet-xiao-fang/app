from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ConeVolumeProof(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"

        # ================== 1. 标题与介绍（顶部居中） ==================
        title = Text("圆锥体积的微积分证明", 
                     font="Source Han Sans CN", 
                     font_size=40,
                     weight=BOLD,
                     color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.add_fixed_in_frame_mobjects(title)

        intro_text = VGroup(
            Text("圆锥体积公式:", font="Source Han Sans CN", font_size=28, color=YELLOW),
            MathTex(r"V = \frac{1}{3} \pi r^2 h", font_size=36, color=YELLOW)
        ).arrange(RIGHT, buff=0.5)
        intro_text.next_to(title, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(intro_text)
        self.play(FadeIn(intro_text))
        self.wait(0.8)

        proof_desc = Text("我们将通过切割圆锥和积分的方法证明这个公式", 
                          font="Source Han Sans CN", 
                          font_size=28,
                          color=BLUE_A)
        proof_desc.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(proof_desc)
        self.play(Write(proof_desc))
        self.wait(1)

        # ================== 2. 创建三维圆锥 ==================
        cone_height = 3
        cone_base_radius = 1.5
        cone = Cone(
            direction=UP,
            height=cone_height,
            base_radius=cone_base_radius,
            resolution=(24, 36),
            fill_color=BLUE_D,
            fill_opacity=0.8,
            stroke_width=0
        )
        cone.rotate(PI/2, RIGHT, about_point=ORIGIN)
        cone.move_to(ORIGIN)

        self.set_camera_orientation(phi=65*DEGREES, theta=-30*DEGREES)
        self.play(Create(cone), run_time=1.5)
        self.wait(0.5)

        # ================== 3. 切割动画 ==================
        self.begin_ambient_camera_rotation(rate=0.1)  # 降低旋转速度，更好观察

        cut_desc = Text("将圆锥切割为许多薄圆盘", 
                       font="Source Han Sans CN", 
                       font_size=28,
                       color=BLUE_A)
        cut_desc.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(cut_desc)
        self.play(ReplacementTransform(proof_desc, cut_desc))
        self.wait(0.5)

        # 创建圆盘组
        discs = Group()
        heights = np.linspace(0, cone_height, 30)
        for i, h in enumerate(heights[1:], start=1):
            ratio = (cone_height - h) / cone_height
            r = cone_base_radius * ratio
            disc = Circle(
                radius=r,
                fill_color=interpolate_color(BLUE_A, GREEN, i/len(heights)),
                fill_opacity=0.7,
                stroke_width=0.1,
                stroke_color=WHITE
            )
            disc.stretch(0.3, 0)
            disc.stretch(ratio * 0.8, 1)
            disc.rotate(PI/2, RIGHT)
            prop = h / cone_height
            point = cone.get_top() * (1 - prop) + cone.get_bottom() * prop
            disc.move_to(point)
            discs.add(disc)

        self.play(FadeOut(cone), LaggedStart(*[FadeIn(d) for d in discs], lag_ratio=0.05), run_time=2)
        self.wait(0.5)

        # ================== 4. 代表性圆盘说明（左上角） ==================
        sample_disc = discs[15].copy()
        sample_disc.set_fill(color=RED, opacity=0.9)
        self.play(discs.animate.set_opacity(0.3), FadeIn(sample_disc), run_time=1)

        # 左侧面板：圆盘参数说明 + 相似三角形示意
        disc_desc = VGroup(
            Text("每个薄圆盘:", font="Source Han Sans CN", font_size=26, color=RED),
            MathTex(r"\text{厚度} = dx", font_size=32, color=RED),
            MathTex(r"\text{半径} = r(x)", font_size=32, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        disc_desc.to_corner(UL, buff=0.6)
        self.add_fixed_in_frame_mobjects(disc_desc)
        self.play(FadeIn(disc_desc))

        # 相似三角形图示（左侧，位于圆盘说明下方）
        sim_triangle = Polygon(
            [0, 0, 0], [1.2, 0, 0], [1.2, 1.0, 0],
            color=PINK, fill_opacity=0.3
        )
        tri_labels = VGroup(
            MathTex(r"r", font_size=26).next_to(sim_triangle, RIGHT, buff=0.1),
            MathTex(r"h", font_size=26).next_to(sim_triangle, DOWN, buff=0.1),
            MathTex(r"x", font_size=26).move_to(sim_triangle.get_center() + LEFT*0.3 + UP*0.3)
        )
        ratio_formula = MathTex(r"r(x) = r \cdot \frac{x}{h}", font_size=32, color=YELLOW)
        sim_desc = Text("根据相似三角形关系:", font="Source Han Sans CN", font_size=24, color=BLUE_A)

        sim_group = VGroup(sim_triangle, tri_labels, ratio_formula, sim_desc).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        sim_group.next_to(disc_desc, DOWN, buff=0.4, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(sim_group)
        self.play(FadeIn(sim_group), run_time=1.5)
        self.wait(1)

        # ================== 5. 积分推导（右侧区域） ==================
        integral_desc = Text("将所有圆盘的体积相加(积分):", 
                             font="Source Han Sans CN", 
                             font_size=28,
                             color=BLUE_A)
        integral_desc.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(integral_desc)
        self.play(ReplacementTransform(cut_desc, integral_desc))

        # 积分公式（右侧上方）
        integral_tex = MathTex(
            r"V = \int_{0}^{h} \pi \left[ r(x) \right]^2 \, dx",
            font_size=34
        )
        integral_tex.to_edge(RIGHT, buff=1.0).to_edge(UP, buff=1.5)
        self.add_fixed_in_frame_mobjects(integral_tex)
        self.play(FadeIn(integral_tex))
        self.wait(1)

        substituted_tex = MathTex(
            r"V = \int_{0}^{h} \pi \left( r \cdot \frac{x}{h} \right)^2 \, dx",
            font_size=34
        )
        substituted_tex.move_to(integral_tex)
        self.add_fixed_in_frame_mobjects(substituted_tex)
        self.play(Transform(integral_tex, substituted_tex))
        self.wait(1)

        # 分步计算（右侧，积分公式下方）
        calc_title = Text("计算积分:", font="Source Han Sans CN", font_size=26, color=BLUE_A)
        calc_title.next_to(integral_tex, DOWN, buff=0.5, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(calc_title)
        self.play(FadeIn(calc_title))

        steps = VGroup(
            MathTex(r"V = \int_{0}^{h} \pi \left( r \cdot \frac{x}{h} \right)^2 \, dx", font_size=30),
            MathTex(r"V = \frac{\pi r^2}{h^2} \int_0^h x^2 \, dx", font_size=30),
            MathTex(r"V = \frac{\pi r^2}{h^2} \cdot \frac{h^3}{3}", font_size=30),
            MathTex(r"V = \frac{1}{3} \pi r^2 h", font_size=34, color=YELLOW)
        )
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(calc_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(steps[0])
        self.play(FadeIn(steps[0]))
        for i in range(1, len(steps)):
            self.add_fixed_in_frame_mobjects(steps[i])
            self.play(TransformFromCopy(steps[i-1], steps[i]), run_time=1.2)
            self.wait(0.4)

        # ================== 6. 最终结果强调（中央） ==================
        # 停止相机旋转，聚焦最终公式
        self.stop_ambient_camera_rotation()

        final_formula = MathTex(
            r"V_{\text{圆锥}} = \frac{1}{3} \pi r^2 h", 
            color=YELLOW,
            font_size=46
        )
        final_formula.move_to(ORIGIN + UP*0.5)
        box = SurroundingRectangle(final_formula, buff=0.25, color=RED, corner_radius=0.1)
        box.set_fill(BLACK, opacity=0.7)

        # 清理不必要的元素
        self.play(
            FadeOut(discs),
            FadeOut(sample_disc),
            FadeOut(sim_group),
            FadeOut(disc_desc),
            FadeOut(integral_tex),
            FadeOut(integral_desc),
            FadeOut(calc_title),
            FadeOut(steps),
            *[FadeOut(mob) for mob in [cut_desc, proof_desc]],  # 清除底部文字
            run_time=1.2
        )
        self.add_fixed_in_frame_mobjects(box, final_formula)
        self.play(
            Create(box),
            Write(final_formula),
            Flash(final_formula, line_length=0.5, flash_radius=1.5),
            run_time=1.5
        )
        self.wait(2)

        # ================== 7. 简洁结尾 ==================
        conclusion = VGroup(
            Text("微积分证明完成!", font="Source Han Sans CN", font_size=36, color="#4FEB34"),
            Text("圆锥体积 = 1/3 × 底面积 × 高", font="Source Han Sans CN", font_size=30, color=BLUE_A)
        ).arrange(DOWN, buff=0.5)
        conclusion.to_edge(DOWN, buff=0.8)
        self.add_fixed_in_frame_mobjects(conclusion)
        self.play(Write(conclusion))
        self.wait(3)
        
# manim -pqh 体积证明.py ConeVolumeProof