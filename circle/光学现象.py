from manim import *
import numpy as np  # 需要导入numpy进行数学计算
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class LightRefraction(Scene):
    def construct(self):
        # 设置场景
        self.camera.background_color = "#1e1e1e"
        
        # 创建标题
        title = Text("光的折射现象", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建介质分界面（水面）
        water_surface = Line(LEFT*5, RIGHT*5, color=BLUE)
        water_surface.set_stroke(width=3)
        self.play(Create(water_surface))
        self.wait(0.5)
        
        # 添加介质标签
        air_label = Text("空气 (n≈1.0)", font_size=24).next_to(water_surface, UP, buff=1)
        water_label = Text("水 (n≈1.33)", font_size=24).next_to(water_surface, DOWN, buff=1)
        self.play(FadeIn(air_label), FadeIn(water_label))
        self.wait(0.5)
        
        # 创建法线（垂直于界面）
        normal = DashedLine(UP*2, DOWN*2, color=GRAY)
        normal.set_stroke(width=2)
        self.play(Create(normal))
        self.wait(0.5)
        
        # 创建入射光线
        incident_start = UP*1.5 + LEFT*3
        incident_end = ORIGIN
        incident_ray = Arrow(
            start=incident_start,
            end=incident_end,
            color=RED,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        # 计算折射角度（斯涅尔定律） - 修复括号问题
        n1 = 1.0
        n2 = 1.33
        incident_angle = 45 * DEGREES
        refracted_angle = np.arcsin((n1 * np.sin(incident_angle)) / n2)  # 修复括号问题
        
        # 创建折射光线
        refracted_end = incident_end + np.array([
            np.sin(refracted_angle),
            -np.cos(refracted_angle),
            0
        ]) * 3
        
        refracted_ray = Arrow(
            start=incident_end,
            end=refracted_end,
            color=YELLOW,
            buff=0,
            stroke_width=5,
            tip_length=0.2
        )
        
        # 绘制光线
        self.play(GrowArrow(incident_ray))
        self.play(GrowArrow(refracted_ray))
        self.wait(1)
        
        # 添加角度标注
        # 入射角
        incident_arc = Arc(
            radius=0.8,
            start_angle=270 * DEGREES,
            angle=-incident_angle,
            color=RED
        )
        incident_angle_label = MathTex(r"\theta_i", color=RED).next_to(incident_arc, LEFT, buff=0.1)
        
        # 折射角
        refracted_arc = Arc(
            radius=0.8,
            start_angle=270 * DEGREES,
            angle=refracted_angle,
            color=YELLOW
        )
        refracted_angle_label = MathTex(r"\theta_r", color=YELLOW).next_to(refracted_arc, RIGHT, buff=0.1)
        
        # 添加角度标注
        self.play(
            Create(incident_arc),
            Write(incident_angle_label),
            Create(refracted_arc),
            Write(refracted_angle_label)
        )
        self.wait(1)
        
        # 添加斯涅尔定律公式
        law_text = MathTex(
            r"n_1 \sin \theta_i = n_2 \sin \theta_r",
            font_size=36,
            color=GREEN
        )
        law_text.next_to(title, DOWN)
        law_box = SurroundingRectangle(law_text, color=GREEN, buff=0.2)
        
        self.play(
            Write(law_text),
            Create(law_box)
        )
        self.wait(2)
        
        # 添加解释文本
        explanation = Text(
            "光从光疏介质进入光密介质时，折射角小于入射角",
            font_size=28,
            color=BLUE_B
        )
        explanation.next_to(water_surface, DOWN, buff=2.5)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # 创建多束光线展示不同入射角
        angles = [30, 45, 60]
        colors = [PINK, ORANGE, PURPLE]
        
        for angle, color in zip(angles, colors):
            # 入射光线
            angle_rad = angle * DEGREES
            ref_angle = np.arcsin((n1 * np.sin(angle_rad)) / n2)  # 同样修复括号问题
            
            new_incident_start = incident_end + np.array([
                -np.sin(angle_rad) * 3,
                np.cos(angle_rad) * 3,
                0
            ])
            
            new_incident_ray = Arrow(
                start=new_incident_start,
                end=incident_end,
                color=color,
                buff=0,
                stroke_width=4,
                tip_length=0.15
            )
            
            # 折射光线
            new_refracted_end = incident_end + np.array([
                np.sin(ref_angle),
                -np.cos(ref_angle),
                0
            ]) * 3
            
            new_refracted_ray = Arrow(
                start=incident_end,
                end=new_refracted_end,
                color=color,
                buff=0,
                stroke_width=4,
                tip_length=0.15
            )
            
            self.play(
                GrowArrow(new_incident_ray),
                GrowArrow(new_refracted_ray),
                run_time=0.7
            )
            self.wait(0.3)
        
        # 最终等待
        self.wait(2)
        
        # 淡出所有元素
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
#  manim -pqh 光学现象.py LightRefraction -r 1920,1080