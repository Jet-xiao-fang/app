from manim import *
import math

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
            x_range=[-1, 5, 1],  # 保留少量负半轴
            y_range=[-1, 6, 1],  # 保留少量负半轴
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

        # 移除网格，只保留坐标轴
        coordinate_system = VGroup(axes)
        
        titile = Tex("求$OE$的最大值?", color=YELLOW, font_size=52).next_to(coordinate_system, UP, buff=1.5)
        self.add(titile)
        
        # 优化标签位置（将x标签放在右侧，y标签放在顶部）
        axis_labels = axes.get_axis_labels(
            MathTex("x").next_to(axes.x_axis.get_right(), DOWN, buff=0.3),
            MathTex("y").next_to(axes.y_axis.get_top(), LEFT, buff=0.3)
        )

        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        # 创建完整的圆（半径为1）
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

        # 不显示轨迹跟踪（只在最后显示）
        # 存储E点的路径用于最后绘制
        e_points = []

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
            OE_line
        )
        
        # 更新函数，记录E点位置但不显示轨迹
        def update_e_position():
            e_position = E_dot.get_center()
            e_points.append(e_position)
        
        # 动画效果
        self.play(
            Rotate(
                P_dot, 
                about_point=A_point.get_center(),
                angle=2 * PI,  # 改为只旋转一圈
                run_time=8,     # 缩短时间
                rate_func=linear
            ),
            Rotate(
                P_label,
                about_point=A_point.get_center(),
                angle=2 * PI,
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
        
        # 思考问题：E点的轨迹是什么？
        question = Tex("E点的轨迹是什么形状?", color=YELLOW, font_size=48)
        question.move_to(titile).to_edge(UP)
        self.play(ReplacementTransform(titile, question))
        self.wait(2)
        
        # 显示轨迹曲线（橙色虚线）
        e_trace = VMobject()
        e_trace.set_points_smoothly(e_points)
        e_trace.set_style(
            stroke_color=ORANGE,
            stroke_width=3,
            stroke_opacity=0.7
        )
        
        # 将实线轨迹转换为虚线轨迹
        e_trace = DashedVMobject(e_trace, num_dashes=60)
        self.play(Create(e_trace), run_time=2)
        
        # 找出最大值时的位置
        max_pos = axes.c2p(1.8, 2.4)  # 数学上的最大值点
        max_dot = Dot(max_pos, color=GREEN, radius=0.1)
        max_label = MathTex(r"E_{\max}", font_size=40, color=GREEN).next_to(max_dot, UL, buff=0.2)
        max_value = MathTex(r"|OE_{\max}|=3.0", font_size=36, color=GREEN).next_to(max_dot, UR, buff=0.5)
        
        # 显示最大值点和标注
        self.play(
            FadeIn(max_dot),
            Write(max_label),
            run_time=1.5
        )
        
        # 强调最大值位置
        self.play(
            Indicate(max_dot, scale_factor=2, color=GREEN),
            Flash(max_dot, color=GREEN, flash_radius=0.5),
            Write(max_value)
        )
        
        # 最终总结
        conclusion = Tex("E点轨迹是一个圆，圆心为(1.5,2)，半径为0.5", font_size=38, color=GOLD)
        conclusion.next_to(question, DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        # 画出理论轨迹圆
        theoretical_circle = Circle(
            radius=0.5,
            color=GOLD,
            stroke_width=3,
            stroke_opacity=0.5
        ).move_to(axes.c2p(1.5, 2))
        theoretical_circle = DashedVMobject(theoretical_circle, num_dashes=40)
        
        center_dot = Dot(axes.c2p(1.5, 2), color=PINK, radius=0.08)
        center_label = MathTex(r"(1.5, 2)", font_size=30, color=PINK).next_to(center_dot, DOWN, buff=0.1)
        
        self.play(
            Create(theoretical_circle),
            FadeIn(center_dot),
            Write(center_label),
            run_time=2
        )
        
        self.wait(5)

# 使用命令：manim -pqh 全圆1.py CleanParabolaPlot -r 1920,1080