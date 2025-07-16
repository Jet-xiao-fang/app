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
        A = np.array([-3, 2, 0])
        B = np.array([-3, -2, 0])  # AB = 4
        C = np.array([3, -2, 0])  # BC = 6

        # 创建顶点
        point_A = Dot(A, color=BLUE)
        point_B = Dot(B, color=BLUE)
        point_C = Dot(C, color=BLUE)

        # 创建顶部标签
        label_A = Text("A").next_to(point_A, UL, buff=0.1)
        label_B = Text("B").next_to(point_B, DL, buff=0.1)
        label_C = Text("C").next_to(point_C, RIGHT, buff=0.1)

        # 创建三角形
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_color=BLUE, fill_opacity=0.5)

        self.play(Create(triangle_ABC))
        self.wait(0.5)
        title = Tex(r"求$PC+\sqrt{2}PA$的最小值？", font_size=48, color=YELLOW).next_to(triangle_ABC,UP,buff=1.5)
        self.add(title)
        # 将元素添加到场景中
        self.add(point_A, point_B, point_C, label_A, label_B, label_C)

        # 显示直角符号
        right_angle = RightAngle(Line(B, A), Line(B, C), length=0.4, quadrant=(1, 1))

        self.play(Create(right_angle))

        point_p = Dot(point_B.get_center(), color=RED)
        line_bc = Line(point_B.get_center(), point_C.get_center())
        line_ap = always_redraw(
            lambda: DashedLine(point_A.get_center(), point_p.get_center(), color=GREEN, stroke_width=4))
        line_pc = always_redraw(lambda: Line(point_p.get_center(), point_C.get_center(), color=YELLOW, stroke_width=4))
        label_p = always_redraw(lambda: Text("P", color=PURPLE).next_to(point_p, DOWN, buff=0.1))

        self.add(line_ap, line_pc, label_p)

        # 来回运动：先正向，再反向
        duration = 6
        # 正向
        self.play(
            MoveAlongPath(
                point_p,
                line_bc,
                run_time=duration,
                rate_func=linear
            )
        )
        # 反向
        self.play(
            MoveAlongPath(
                point_p,
                line_bc,
                run_time=duration,
                rate_func=lambda t: linear(1 - t)  # 向回动画
            )
        )
        self.wait(3)
        
# manim -pqh --format=png 三角形.py GridExample -r 1920,1080