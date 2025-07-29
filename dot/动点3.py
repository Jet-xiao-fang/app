from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-3, 5, 1],
            x_length=16,
            y_length=8,
            
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0).scale(0.8)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))  # 使用MathTex
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        
        # 抛物线绘制
        parabola = axes.plot(
            lambda x: x**2 / -8,
            color=GREEN,
            stroke_width=4
        )
        # 替换原有parabola_label定义
        parabola_label = axes.get_graph_label(
            graph=parabola,
            label=MathTex(r"y =-\dfrac{1}{4}x^2", color=GREEN).scale(0.8),
            x_val=3,  # 指定x=3处的标签位置
            direction=DOWN+LEFT,
            buff=0.4,
            dot=False  # 不显示定位点
        )
        tex = Tex(r"求$AP^{2}+BP^{2}$的最小值？", color=YELLOW).next_to(axes,UP,buff=1)
        # 添加到场景
        self.add(axes, axis_labels, origin_dot, origin_label,parabola,parabola_label,tex)
        # 正确写法（Axes坐标系转换）
        A_coords = (-4, -2)  # 数学坐标系中的坐标
        A_point = Dot(axes.c2p(*A_coords), color=RED)  # 转换到场景坐标系
        Label_A = Tex("A").next_to(A_point, LEFT, buff=0.1)
        B_coords = (4, -2)  # 数学坐标系中的坐标
        B_point = Dot(axes.c2p(*B_coords), color=RED)  # 转换到场景坐标系
        Label_B = Tex("B").next_to(B_point, RIGHT, buff=0.1)
        
        self.add(A_point,Label_A,B_point,Label_B)

        circle = Circle(
            radius= 1*0.8,
            color= BLUE_C,
            stroke_width = 4
        ).move_to(axes.c2p(0,2))

        # 创建圆心点
        center_dot = Dot(
         point=circle.get_center(),  # 获取圆心位置
         color=RED,  # 设置为红色以便明显
         radius=0.08  # 点的大小
        )

        self.add(circle,center_dot)

        # 初始点 P 放在圆的右侧（相当于角度 0）
        P = Dot(
            point=circle.point_at_angle(0),  # 初始位置在 0 弧度（右侧）
            color=RED,
            radius=0.08
        )

        # 可选：添加标签 P
        # label_p = Tex("P").next_to(P, UP, buff=0.1)
        # P也要跟随这变化
        label_p = always_redraw(lambda: Tex("P").next_to(P, UP, buff=0.15))

        AP = always_redraw(lambda: DashedLine(
            A_point.get_center(), 
            P.get_center(),
            color=RED_C,
            stroke_width=2.5
        ))
        BP = always_redraw(lambda: DashedLine(
            B_point.get_center(),
            P.get_center(),
            color=BLUE_C,
            stroke_width=2.5
        ))
        self.play(
            Create(P),
            Write(label_p),
            Create(AP),
            Create(BP),
            run_time = 1.5
        )
         # 轨迹跟踪（网页6的抛物线绘制扩展）
        trace = TracedPath(P.get_center, dissipating_time=1, stroke_color=YELLOW)
        self.add(trace)  # 添加轨迹追踪

        # 让点 P 沿圆运动
        self.play(
            MoveAlongPath(P, circle),
            run_time=6,
            rate_func=linear
        )
        self.play(
            MoveAlongPath(P, circle),
            run_time=6,
            rate_func=linear
        )
        
        self.wait(2)

# manim -pqh --format=png 动点3.py ParabolaPlot -r 1920,1080