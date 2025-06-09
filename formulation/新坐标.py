from manim import *
# config.frame_height = 16
# config.frame_width = 9
# config.pixel_height = 1080
# config.pixel_width = 608
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CirclePropertiesDemo(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#263238"
        
        # 创建等比例坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加精细网格
        grid = NumberPlane(
            x_range=[-4, 4, 0.5],
            y_range=[-3, 3, 0.5],
            background_line_style={
                "stroke_color": GREY_B,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={"color": WHITE},
            x_length=8,
            y_length=6
        )
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(
            Tex("x").set_color(WHITE),
            Tex("y").set_color(WHITE)
        )
        
        # 创建圆（半径=2）
        circle = Circle(radius=2, color=BLUE, stroke_width=4)
        
        # 圆心标记
        center = Dot(color=WHITE).scale(0.8)
        center_label = Tex("O", color=WHITE).next_to(center, DR, buff=0.1)
        
        # 组合基本元素
        self.add(grid, axes, axis_labels, circle, center, center_label)
        self.wait(1)
        
        # ===== 演示圆的性质 =====
        
        # 3. 切线与圆心关系
        self.tangent_properties(circle, center)
        
        # 4. 圆周角定理
        self.inscribed_angle_theorem(circle, center)
    
    def tangent_properties(self, circle, center):
        """演示切线与圆心的关系"""
        title = Tex("性质1: 切线与半径的关系", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # 创建切点
        tangent_point = circle.point_at_angle(3*PI/4)
        tangent_dot = Dot(tangent_point, color=YELLOW)
        
        # 创建切线
        tangent_dir = tangent_point - center.get_center()
        tangent_normal = np.array([-tangent_dir[1], tangent_dir[0], 0])
        tangent_line = Line(
            tangent_point - tangent_normal*1.5,
            tangent_point + tangent_normal*1.5,
            color=GREEN,
            stroke_width=3
        )
        
        # 创建半径
        radius = Line(center.get_center(), tangent_point, color=RED, stroke_width=2.5)
        
        # 标记直角
        right_angle = RightAngle(
            tangent_line, radius,
            length=0.3, color=BLUE_C,
            quadrant=(-1,1)
        )
        
        # 公式
        formula = MathTex(
            r"\text{切线} \perp \text{半径}",
            color=PURPLE
        ).next_to(circle, RIGHT, buff=1)
        
        # 动画展示
        self.play(FadeIn(tangent_dot))
        self.play(Create(tangent_line))
        self.play(Create(radius))
        self.play(Create(right_angle))
        self.play(Write(formula))
        
        # 说明文本
        explanation = Tex(
            r"圆的切线与经过切点的半径垂直",
            font_size=28,
            color=GREEN
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 清理场景
        self.play(
            FadeOut(tangent_dot),
            FadeOut(tangent_line),
            FadeOut(radius),
            FadeOut(right_angle),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(title)
        )
    
    def inscribed_angle_theorem(self, circle, center):
        """演示圆周角定理"""
        title = Tex("性质2: 圆周角定理", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # 创建弧上的点
        A = Dot(circle.point_at_angle(PI/6), color=GREEN)
        B = Dot(circle.point_at_angle(PI/2), color=GREEN)
        C = Dot(circle.point_at_angle(5*PI/4), color=GREEN)
        
        # 创建弦
        AB = Line(A.get_center(), B.get_center(), color=BLUE, stroke_width=2)
        BC = Line(B.get_center(), C.get_center(), color=BLUE, stroke_width=2)
        AC = Line(A.get_center(), C.get_center(), color=BLUE, stroke_width=2)
        
        # 创建圆心角
        OA = Line(center.get_center(), A.get_center(), color=RED, stroke_width=2)
        OB = Line(center.get_center(), B.get_center(), color=RED, stroke_width=2)
        OC = Line(center.get_center(), C.get_center(), color=RED, stroke_width=2)
        
        # 标记圆心角
        center_angle = Angle(
            OA, OB, radius=0.5, color=YELLOW, other_angle=True
        )
        center_label = MathTex(r"\theta", color=YELLOW).next_to(center_angle, UR, buff=0.1)
        
        # 标记圆周角
        circum_angle = Angle(
            AC, BC, radius=0.7, color=PURPLE
        )
        circum_label = MathTex(r"\phi", color=PURPLE).next_to(circum_angle, UR, buff=0.15)
        
        # 公式
        formula = MathTex(
            r"\phi = \frac{1}{2}\theta",
            color=ORANGE
        ).next_to(circle, RIGHT, buff=1)
        
        # 动画展示
        self.play(
            FadeIn(A),
            FadeIn(B),
            FadeIn(C)
        )
        self.play(
            Create(AB),
            Create(BC),
            Create(AC),
            Create(OA),
            Create(OB),
            Create(OC)
        )
        self.play(
            Create(center_angle),
            Write(center_label),
            Create(circum_angle),
            Write(circum_label)
        )
        self.play(Write(formula))
        
        # 说明文本
        explanation = Tex(
            r"圆周角等于其所对圆心角的一半",
            font_size=28,
            color=GREEN
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(Write(explanation))
        self.wait(3)