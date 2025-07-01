from manim import *
import numpy as np

config.background_color = "#1F2430"
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ConeVolumeProof(ThreeDScene):
    def construct(self):
        # 1. 标题和开场
        title = Text("圆锥体积的微积分证明", 
                     font="Source Han Sans CN", 
                     font_size=40,
                     weight=BOLD,
                     color=WHITE).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        
        formula = MathTex(r"V = \frac{1}{3} \pi r^2 h", font_size=40, color=YELLOW)
        formula.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(FadeIn(title), FadeIn(formula))
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
            stroke_width=1.0
        )
        cone.rotate(PI/2, RIGHT, about_point=ORIGIN)
        cone.move_to(ORIGIN)
        
        self.set_camera_orientation(phi=65*DEGREES, theta=-30*DEGREES)
        self.play(Create(cone), run_time=1.5)
        self.wait(1)
        
        # 3. 切割动画
        self.begin_ambient_camera_rotation(rate=0.1)
        
        # 添加切割说明（固定在屏幕上）
        cut_desc = Text("将圆锥切割为许多薄圆盘", 
                       font="Source Han Sans CN", 
                       font_size=28,
                       color=BLUE_A).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(cut_desc)
        self.play(Write(cut_desc))
        self.wait(0.5)
        
        discs = Group()
        heights = np.linspace(0, cone_height, 30)
        
        for i, h in enumerate(heights[1:], start=1):
            ratio = (cone_height - h) / cone_height
            r = cone_base_radius * ratio
            
            disc = Circle(
                radius=r,
                fill_color=interpolate_color(BLUE_A, GREEN, i/len(heights)),
                fill_opacity=0.7,
                stroke_width=0.5,
                stroke_color=WHITE
            )
            disc.stretch(0.01, 0)  # 非常薄的圆盘
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
        self.wait(1)
        
        # 4. 相似三角形关系展示（固定在屏幕上）
        sim_desc = Text("根据相似三角形关系:", 
                        font="Source Han Sans CN", 
                        font_size=28,
                        color=BLUE_A).to_corner(UL)
        self.add_fixed_in_frame_mobjects(sim_desc)
        self.play(FadeIn(sim_desc))
        
        # 相似三角形图示
        sim_triangle = Polygon(
            [0, 0, 0], [1.5, 0, 0], [1.5, 1.2, 0], 
            color=PINK, fill_opacity=0.3
        ).to_corner(UL).shift(DOWN)
        
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
        
        self.add_fixed_in_frame_mobjects(sim_triangle, tri_labels, ratio_formula)
        self.play(
            FadeIn(sim_triangle),
            FadeIn(tri_labels),
            Write(ratio_formula),
            run_time=1
        )
        self.wait(2)
        
        # 5. 积分公式推导（固定在屏幕上）
        integral_desc = Text("将所有圆盘的体积相加(积分):", 
                             font="Source Han Sans CN", 
                             font_size=28,
                             color=BLUE_A).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(integral_desc)
        self.play(Transform(cut_desc, integral_desc))
        self.wait(0.5)
        
        integral_tex = MathTex(
            r"V = \int_{0}^{h} \pi \left[ r \cdot \frac{x}{h} \right]^2 \, dx",
            font_size=36
        ).next_to(integral_desc, UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(integral_tex)
        self.play(Write(integral_tex))
        self.wait(2)
        
        # 6. 计算结果（固定在屏幕上）
        calc_desc = Text("计算积分:", 
                        font="Source Han Sans CN", 
                        font_size=28,
                        color=BLUE_A).to_corner(UR)
        self.add_fixed_in_frame_mobjects(calc_desc)
        self.play(FadeIn(calc_desc))
        
        # 分步展示计算过程
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
        
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.next_to(calc_desc, DOWN, buff=0.5)
        steps.to_edge(RIGHT)
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
        
        # 7. 最终结果强调
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=70*DEGREES, theta=-30*DEGREES)
        
        final_formula = MathTex(
            r"V_{\text{圆锥}} = \frac{1}{3} \pi r^2 h", 
            color=YELLOW,
            font_size=42
        ).move_to(ORIGIN)
        
        box = SurroundingRectangle(final_formula, buff=0.2, color=RED)
        self.add_fixed_in_frame_mobjects(box, final_formula)
        self.play(
            FadeOut(discs),
            FadeOut(sim_triangle),
            FadeOut(tri_labels),
            FadeOut(ratio_formula),
            FadeOut(integral_tex),
            FadeOut(integral_desc),
            FadeOut(calc_desc),
            FadeOut(steps),
            Create(box),
            Write(final_formula),
            run_time=1.5
        )
        self.wait(2)
        
        # 8. 简洁结尾
        conclusion = Text("微积分证明完成!", 
                         font="Source Han Sans CN", 
                         font_size=36, 
                         color="#4FEB34").next_to(final_formula, DOWN, buff=0.7)
        
        self.add_fixed_in_frame_mobjects(conclusion)
        self.play(Write(conclusion))
        self.wait(3)