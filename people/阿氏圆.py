from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class GridExample(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 定义点A、B、C的坐标
        A = np.array([-2.5, 1.5, 0])
        B = np.array([-2.5, -1.5, 0])  # AB = 3
        C = np.array([3.5, -1.5, 0])  # BC = 6

        # 创建顶点
        point_A = Dot(A, color=RED)
        point_B = Dot(B, color=RED)
        point_C = Dot(C, color=RED)

        # 创建顶部标签
        label_A = MathTex("A",color=YELLOW).next_to(point_A, UL, buff=0.1)
        label_B = MathTex("B",color=YELLOW).next_to(point_B, DL, buff=0.1)
        label_C = MathTex("C",color=YELLOW).next_to(point_C, RIGHT, buff=0.1)

        # 创建三角形
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_color=BLUE, fill_opacity=0.5)

        self.play(Create(triangle_ABC))
        self.wait(0.5)
        title = Tex(r"求$PA+\frac{1}{3}PC$的最小值？", font_size=48, color=YELLOW).next_to(triangle_ABC,UP,buff=1.5)
        self.add(title)
        self.wait(0.5)
        # 将元素添加到场景中
        self.play(Create(point_A), Create(point_B), Create(point_C), 
                  Write(label_A), Write(label_B), Write(label_C),run_time=1.5)

        # 显示直角符号
        right_angle = RightAngle(Line(B, A), Line(B, C), length=0.4, quadrant=(1, 1),color=PINK)

        self.add(right_angle)
        
        circle = Circle(
            radius=1.5,
            stroke_width = 5,
            color=BLUE
        ).set_fill(GREEN).set_opacity(0.5)
        circle.move_to(point_B)
        self.play(Create(circle))
        
        p = Dot(point=circle.point_at_angle(45 * DEGREES),color=RED)
        label_p = always_redraw(lambda: Tex("P").next_to(p,DOWN,buff=0.05).scale(0.7))
        line_ap = always_redraw(lambda: Line(point_A.get_center(),p.get_center(),stroke_width=4,color=YELLOW))
        line_pc = always_redraw(lambda: Line(p.get_center(),point_C.get_center(),stroke_width=4,color=ORANGE))
        
        self.add(p,label_p,line_ap,line_pc)
        
        self.play(
            MoveAlongPath(p,circle),
            run_time = 6,
            rate_func=linear
        )
        self.play(
            MoveAlongPath(p,circle),
            run_time = 6,
            rate_func=linear
        )
        
        self.wait(2)
        
# manim -pqh 阿氏圆.py GridExample