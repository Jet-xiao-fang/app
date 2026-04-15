from manim import *
import numpy as np


config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ConeVolumeProof(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 1. 标题和开场动画
        title = Text("圆锥体积的微积分证明", 
                     font="Source Han Sans CN", 
                     font_size=40,
                     weight=BOLD,
                     color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        
        # 添加介绍文本
        intro_text = VGroup(
            Text("圆锥体积公式:", font="Source Han Sans CN", font_size=28, color=YELLOW),
            MathTex(r"V = \frac{1}{3} \pi r^2 h", font_size=36, color=YELLOW)
        ).arrange(RIGHT, buff=0.5)
        intro_text.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_text)
        self.play(FadeIn(intro_text))
        self.wait(1)
        
        # 添加证明说明
        proof_desc = Text("我们将通过切割圆锥和积分的方法证明这个公式", 
                          font="Source Han Sans CN", 
                          font_size=28,
                          color=BLUE_A).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(proof_desc)
        self.play(Write(proof_desc))
        self.wait(1)
        
        # 2. 创建三维圆锥
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
        
        # 3. 切割动画
        self.begin_ambient_camera_rotation(rate=0.15)
        
        # 添加切割说明 - 修改部分
        cut_desc = Text("将圆锥切割为许多薄圆盘", 
                       font="Source Han Sans CN", 
                       font_size=28,
                       color=BLUE_A).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(cut_desc)
        self.play(
            ReplacementTransform(proof_desc, cut_desc),
        )
        self.wait(0.5)
        
        # 创建切割圆盘组
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
        
        # 显示切割动画
        self.play(
            FadeOut(cone),
            LaggedStart(*[FadeIn(disc) for disc in discs], lag_ratio=0.05),
            run_time=2
        )
        self.wait(0.5)
        
        # 4. 展示代表性圆盘
        # 选择一个中间的圆盘作为代表
        sample_disc = discs[15].copy()
        sample_disc.set_fill(color=RED, opacity=0.9)
        self.play(
            discs.animate.set_opacity(0.3),
            FadeIn(sample_disc),
            run_time=1
        )
        
        # 添加圆盘说明 - 优化位置
        disc_desc = VGroup(
            Text("每个薄圆盘:", font="Source Han Sans CN", font_size=28, color=RED),
            MathTex(r"\text{厚度} = dx", font_size=36, color=RED),
            MathTex(r"\text{半径} = r(x)", font_size=36, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT)
        disc_desc.to_corner(UL)  # 移到左上角避免重叠
        self.add_fixed_in_frame_mobjects(disc_desc)
        self.play(FadeIn(disc_desc))
        self.wait(1)
        
        # 5. 展示半径的变化关系
        # 相似三角形图示 - 优化位置和大小
        sim_triangle = Polygon(
            [0, 0, 0], [1.5, 0, 0], [1.5, 1.2, 0],  # 缩小尺寸
            color=PINK, fill_opacity=0.3
        ).next_to(disc_desc, DOWN, buff=0.2)

        # 添加标签
        tri_labels = VGroup(
            MathTex(r"r", font_size=28).next_to(sim_triangle, RIGHT, buff=0.1),
            MathTex(r"h", font_size=28).next_to(sim_triangle, DOWN, buff=0.1),
            MathTex(r"x", font_size=28).move_to(sim_triangle.get_center() + LEFT*0.4 + UP*0.4)
        )
        
        # 比例公式
        ratio_formula = MathTex(
            r"r(x) = r \cdot \frac{x}{h}",
            font_size=36,
            color=YELLOW
        ).next_to(sim_triangle, DOWN, buff=0.7)
        
        # 添加相似三角形说明 - 优化位置
        sim_desc = Text("根据相似三角形关系:", 
                        font="Source Han Sans CN", 
                        font_size=28,
                        color=BLUE_A).next_to(ratio_formula, DOWN, buff=0.5).scale(0.5)
        
        all_2d = VGroup(sim_triangle, tri_labels, ratio_formula, sim_desc)
        self.add_fixed_in_frame_mobjects(all_2d)
        
        self.play(
            FadeIn(sim_triangle),
            FadeIn(tri_labels),
            Write(ratio_formula),
            Write(sim_desc),
            run_time=1.5
        )
        self.wait(1)
        
        # 6. 积分公式推导
        # 添加积分说明 - 修改部分
        integral_desc = Text("将所有圆盘的体积相加(积分):", 
                             font="Source Han Sans CN", 
                             font_size=28,
                             color=BLUE_A).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(integral_desc)
        self.play(
            ReplacementTransform(cut_desc, integral_desc),
        )
        self.wait(0.5)
        
        # 显示积分公式 - 优化位置
        integral_tex = MathTex(
            r"V = \int_{0}^{h} \pi \left[ r(x) \right]^2 \, dx",
            font_size=36
        ).next_to(integral_desc, UP, buff=0.3)  # 放在说明上方
        self.add_fixed_in_frame_mobjects(integral_tex)
        self.play(FadeIn(integral_tex))
        self.wait(1)
        
        # 代入半径关系 - 优化位置
        substituted_tex = MathTex(
            r"V = \int_{0}^{h} \pi \left( r \cdot \frac{x}{h} \right)^2 \, dx",
            font_size=36
        ).move_to(integral_tex)  # 保持在同一位置
        self.add_fixed_in_frame_mobjects(substituted_tex)
        self.play(Transform(integral_tex, substituted_tex))
        self.wait(1)
        
        # 7. 计算结果动画 - 优化布局
        # 添加计算说明
        calc_desc = Text("计算积分:", 
                        font="Source Han Sans CN", 
                        font_size=28,
                        color=BLUE_A).to_edge(UP).shift(DOWN*1.5)  # 放在顶部下方
        self.add_fixed_in_frame_mobjects(calc_desc)
        self.play(FadeIn(calc_desc))
        
        # 分步展示计算过程 - 优化位置和间距
        steps = VGroup(
            MathTex(r"V = \int_{0}^{h} \pi \left( r \cdot \frac{x}{h} \right)^2 \, dx", 
                    font_size=36),
            MathTex(r"V = \frac{\pi r^2}{h^2} \int_0^h x^2 \, dx", 
                    font_size=36),
            MathTex(r"V = \frac{\pi r^2}{h^2} \cdot \frac{h^3}{3}", 
                    font_size=36),
            MathTex(r"V = \frac{1}{3} \pi r^2 h", 
                    font_size=36, color=YELLOW)
        )
        
        # 增加间距并左对齐
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.next_to(calc_desc, DOWN, buff=0.5)
        steps.to_edge(RIGHT)  # 移到左侧避免重叠
        steps.scale(0.8)
        
        self.add_fixed_in_frame_mobjects(steps[0])
        self.play(FadeIn(steps[0]))
        self.wait(0.5)
        
        for i in range(1, len(steps)):
            self.add_fixed_in_frame_mobjects(steps[i])
            self.play(
                TransformFromCopy(steps[i-1], steps[i]),
                run_time=1.5
            )
            self.wait(0.5)
        
        # 8. 最终结果强调 - 优化位置
        final_formula = MathTex(
            r"V_{\text{圆锥}} = \frac{1}{3} \pi r^2 h", 
            color=YELLOW,
            font_size=42
        ).move_to(ORIGIN + UP*1)  # 上移避免与标题重叠
        
        box = SurroundingRectangle(final_formula, buff=0.2, color=RED)
        box.set_fill(BLACK, opacity=0.8)
        
        self.add_fixed_in_frame_mobjects(box, final_formula)
        
        self.play(
            FadeOut(discs),
            FadeOut(sample_disc),
            FadeOut(all_2d),
            FadeOut(integral_tex),
            FadeOut(integral_desc),  # 正确淡出积分说明
            FadeOut(calc_desc),
            FadeOut(steps),
            Create(box),
            Write(final_formula),
            Flash(final_formula, line_length=0.4, flash_radius=1.3),
            run_time=1.5
        )
        self.wait(2)
        
        # 9. 简洁结尾 - 优化位置
        conclusion = VGroup(
            Text("微积分证明完成!", font="Source Han Sans CN", font_size=36, color="#4FEB34"),
            Text("圆锥体积 = 1/3 × 底面积 × 高", font="Source Han Sans CN", font_size=30, color=BLUE_A)
        ).arrange(DOWN, buff=0.5).to_edge(DOWN).shift(UP*0.5)  # 上移避免与屏幕边缘重叠
        
        self.add_fixed_in_frame_mobjects(conclusion)
        self.play(Write(conclusion))
        self.wait(3)
# manim -pqh 体积证明.py ConeVolumeProof