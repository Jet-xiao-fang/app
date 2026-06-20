from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CleanParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 坐标轴配置：y轴比x轴稍长
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 6, 1],
            x_length=6,
            y_length=7,
            axis_config={
                "color": "#ECEFF1", 
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 28
            },
            tips=False,
        ).set_aspect_ratio(1.0)

        coordinate_system = VGroup(axes)
        
        title = Tex("求$OE$的最大值?", color=YELLOW, font_size=52).next_to(coordinate_system, UP, buff=1.5)
        self.add(title)
        
        axis_labels = axes.get_axis_labels(
            MathTex("x").next_to(axes.x_axis.get_right(), DOWN, buff=0.3),
            MathTex("y").next_to(axes.y_axis.get_top(), LEFT, buff=0.3)
        )

        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        # 创建圆（半径为1）
        circle = Circle(
            radius=1,
            color=RED,
            stroke_width=4
        ).move_to(axes.c2p(3, 0))
        
        # 点A(3,0)
        A_coords = (3, 0)
        A_point = Dot(axes.c2p(*A_coords), color=RED)
        Label_A = Tex("A", font_size=32).next_to(A_point, DOWN, buff=0.1)
        
        # 点B(0,4)
        B_coords = (0, 4)
        B_point = Dot(axes.c2p(*B_coords), color=RED)
        Label_B = Tex("B", font_size=32).next_to(B_point, LEFT, buff=0.1)
        
        # 动点P初始位置
        P = axes.c2p(4, 0)  # 从(4,0)开始
        P_dot = Dot(P, color=BLUE).scale(0.8)
        P_label = Tex("P", font_size=32).next_to(P_dot, DOWN, buff=0.1)
        
        # 初始线段
        BP_line = Line(B_point.get_center(), P, color=YELLOW, stroke_width=2)
        E = (B_point.get_center() + P) / 2
        E_dot = Dot(E, color=ORANGE).scale(0.6)
        E_label = Tex("E", font_size=32).next_to(E_dot, UR, buff=0.1)
        OE_line = Line(origin_point, E, color=BLUE, stroke_width=3)

        # 轨迹跟踪（初始不添加到场景）
        e_trace = TracedPath(E_dot.get_center, stroke_color=ORANGE, stroke_width=3, stroke_opacity=0.7)
        
        # 添加初始元素
        self.add(
            coordinate_system,
            axis_labels, 
            origin_dot, 
            origin_label,
            circle,
            Label_A,
            A_point,
            B_point,
            Label_B,
            P_dot,
            P_label,
            BP_line, 
            E_dot, 
            E_label, 
            OE_line,
        )
        
        # 第一圈动画（不显示轨迹）
        self.play(
            Rotate(
                P_dot, 
                about_point=A_point.get_center(),
                angle=2 * PI,
                run_time=4,
                rate_func=linear
            ),
            Rotate(
                P_label,
                about_point=A_point.get_center(),
                angle=2 * PI,
                run_time=4,
                rate_func=linear
            ),
            UpdateFromFunc(BP_line, lambda line: line.put_start_and_end_on(
                B_point.get_center(), P_dot.get_center()
            )),
            UpdateFromFunc(E_dot, lambda dot: dot.move_to(
                (B_point.get_center() + P_dot.get_center())/2
            )),
            UpdateFromFunc(E_label, lambda label: label.next_to(E_dot, UR, buff=0.1)),
            UpdateFromFunc(OE_line, lambda line: line.put_start_and_end_on(
                origin_dot.get_center(), E_dot.get_center()
            )),
            run_time=4
        )
        
        # 第二圈开始时添加轨迹
        self.add(e_trace)
        
        # 继续运动两圈（显示轨迹）
        self.play(
            Rotate(
                P_dot, 
                about_point=A_point.get_center(),
                angle=4 * PI,  # 再转两圈
                run_time=8,
                rate_func=linear
            ),
            Rotate(
                P_label,
                about_point=A_point.get_center(),
                angle=4 * PI,
                run_time=8,
                rate_func=linear
            ),
            UpdateFromFunc(BP_line, lambda line: line.put_start_and_end_on(
                B_point.get_center(), P_dot.get_center()
            )),
            UpdateFromFunc(E_dot, lambda dot: dot.move_to(
                (B_point.get_center() + P_dot.get_center())/2
            )),
            UpdateFromFunc(E_label, lambda label: label.next_to(E_dot, UR, buff=0.1)),
            UpdateFromFunc(OE_line, lambda line: line.put_start_and_end_on(
                origin_dot.get_center(), E_dot.get_center()
            )),
            run_time=8
        )
        
        self.wait(3)  
# manim -p 全圆.py CleanParabolaPlot