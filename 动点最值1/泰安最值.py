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
        
        # 坐标轴配置
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "color": "#ECEFF1", 
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 28
            },
            tips=False,
        ).set_aspect_ratio(1.0)

        coordinate_system = VGroup(axes)
        
        title = Tex("求$OM$的最大值?", color=YELLOW, font_size=52).next_to(coordinate_system, UP, buff=1.5)
        self.add(title)
        
        axis_labels = axes.get_axis_labels(
            MathTex("x").next_to(axes.x_axis.get_right(), DOWN, buff=0.3),
            MathTex("y").next_to(axes.y_axis.get_top(), LEFT, buff=0.3)
        )

        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        # 创建圆（圆心B(0,2)，半径1）
        circle = Circle(
            radius=1,
            color=RED,
            stroke_width=4
        ).move_to(axes.c2p(0, 2))
        
        # 点A(2,0)
        A_coords = (2, 0)
        A_point = Dot(axes.c2p(*A_coords), color=RED)
        Label_A = Tex("A", font_size=28).next_to(A_point, UP, buff=0.1)
        
        # 点B(0,2)
        B_coords = (0, 2)
        B_point = Dot(axes.c2p(*B_coords), color=RED)
        Label_B = Tex("B", font_size=28).next_to(B_point, RIGHT, buff=0.1)
        
        # 动点P初始位置（在圆上）
        P_initial = axes.c2p(0, 3)  # 圆上一点 (0,3)
        P_dot = Dot(P_initial, color=BLUE).scale(0.8)
        P_label = Tex("P", font_size=32).next_to(P_dot, UP, buff=0.1)
        
        # 初始线段
        AP_line = Line(A_point.get_center(), P_initial, color=YELLOW, stroke_width=2)
        BP_line = Line(B_point.get_center(), P_initial, color=YELLOW, stroke_width=2)
        
        # 计算PA中点M
        M_initial = (A_point.get_center() + P_initial) / 2
        M_dot = Dot(M_initial, color=ORANGE).scale(0.6)
        M_label = Tex("M", font_size=32).next_to(M_dot, UR, buff=0.1)
        OM_line = Line(origin_point, M_initial, color=BLUE, stroke_width=3)

        # 轨迹跟踪
        m_trace = TracedPath(M_dot.get_center, stroke_color=YELLOW, stroke_width=3, stroke_opacity=0.7)
        
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
            AP_line,
            BP_line,
            M_dot, 
            M_label, 
            OM_line,
        )
        
        # 更新函数
        def update_all(mob=None):
            # 更新AP线
            AP_line.become(Line(A_point.get_center(), P_dot.get_center(), color=YELLOW, stroke_width=2))
            # 更新BP线
            BP_line.become(Line(B_point.get_center(), P_dot.get_center(), color=YELLOW, stroke_width=2))
            # 更新M点（PA中点）
            new_M = (A_point.get_center() + P_dot.get_center()) / 2
            M_dot.move_to(new_M)
            M_label.next_to(M_dot, UR, buff=0.1)
            # 更新OM线
            OM_line.become(Line(origin_point, new_M, color=BLUE, stroke_width=3))
        
        # 将P点添加到圆上（确保旋转中心是圆心B）
        P_dot.add_updater(lambda d: d.move_to(circle.point_at_angle(
            angle_of_vector(d.get_center() - B_point.get_center())
        )))
        
        # 第一圈动画（不显示轨迹）
        self.play(
            Rotate(
                P_dot, 
                about_point=B_point.get_center(),  # 围绕圆心B旋转
                angle=2 * PI,
                run_time=5,
                rate_func=linear
            ),
            Rotate(
                P_label,
                about_point=B_point.get_center(),
                angle=2 * PI,
                run_time=5,
                rate_func=linear
            ),
            UpdateFromFunc(AP_line, update_all),
            UpdateFromFunc(BP_line, update_all),
            UpdateFromFunc(M_dot, update_all),
            UpdateFromFunc(M_label, update_all),
            UpdateFromFunc(OM_line, update_all)
        )
        
        # 第二圈开始时添加轨迹
        self.add(m_trace)
        
        # 继续运动两圈（显示轨迹）
        self.play(
            Rotate(
                P_dot, 
                about_point=B_point.get_center(),
                angle=4 * PI,  # 再转两圈
                run_time=8,
                rate_func=linear
            ),
            Rotate(
                P_label,
                about_point=B_point.get_center(),
                angle=4 * PI,
                run_time=8,
                rate_func=linear
            ),
            UpdateFromFunc(AP_line, update_all),
            UpdateFromFunc(BP_line, update_all),
            UpdateFromFunc(M_dot, update_all),
            UpdateFromFunc(M_label, update_all),
            UpdateFromFunc(OM_line, update_all)
        )
        self.wait(3)
# manim -p 泰安最值.py CleanParabolaPlot