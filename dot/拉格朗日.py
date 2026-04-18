from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class RectangleABCD(Scene):
    def construct(self):
        
        self.camera.background_color = "#0F0F1A"
        
        # 放大矩形尺寸到6×4
        rect = Rectangle(width=6, height=4, color=BLUE, fill_opacity=0.3)
        # 增大标签字体并调整位置
        width_label = MathTex("3",color=YELLOW).scale(0.8).next_to(rect, UP, buff=0.3)
        height_label = MathTex("2",color=YELLOW).scale(0.8).next_to(rect, RIGHT, buff=0.3)
        tex = Tex(r"当$PE+2PD$最小时，\\求$BP$的长", color=YELLOW).next_to(rect ,UP,buff=1.5)
        self.add(tex)
        # 顶点坐标定义（按比例放大）
        A = np.array([-3, 2, 0])
        B = np.array([-3, -2, 0])
        C = np.array([3, -2, 0])
        D = np.array([3, 2, 0])
        E = np.array([-3, 0, 0])  # E点位于AD中点

        # 顶点标记和标签（增大字体）
        points = VGroup(
            Dot(D, color=RED, radius=0.08),
            Dot(E, color=RED, radius=0.08)
        )
        
        vertex_labels = VGroup(
            MathTex("A").scale(0.7).next_to(A, UP+LEFT, buff=0.15),
            MathTex("B").scale(0.7).next_to(B, DOWN+LEFT, buff=0.15),
            MathTex("C").scale(0.7).next_to(C, DOWN+RIGHT, buff=0.15),
            MathTex("D").scale(0.7).next_to(D, UP+RIGHT, buff=0.15),
            MathTex("E").scale(0.7).next_to(E, LEFT, buff=0.15)
        )

        # 动点P及其连接线
        P = Dot(B, color=YELLOW, radius=0.1)  # 初始位置在B点
        
        # 添加P的标签 - 使用always_redraw使其跟随P移动
        P_label = always_redraw(
            lambda: MathTex("P").scale(0.7)
            .next_to(P, DOWN, buff=0.15)
        )
        
        # 动态更新线段
        EP = always_redraw(lambda: Line(
            E, P.get_center(), 
            color=YELLOW, 
            stroke_width=4  # 加粗线条
        ))
        
        PD = always_redraw(lambda: Line(
            P.get_center(), D, 
            color=RED, 
            stroke_width=4  # 加粗线条
        ))

        # 添加线段标签
        EP_label = always_redraw(
            lambda: MathTex("EP").scale(0.6)
            .next_to(EP.point_from_proportion(0.5), LEFT, buff=0.1)
            
        )
        
        PD_label = always_redraw(
            lambda: MathTex("PD").scale(0.6)
            .next_to(PD.point_from_proportion(0.5), DOWN, buff=0.1)
            
        )
        pd_line = always_redraw(lambda: Line(B,P.get_center(),color=RED,stroke_width=4))

        # 创建BC边路径（加粗）
        bc_path = Line(B, C, color=GREY, stroke_width=3, stroke_opacity=0.5)

        # 添加初始元素
        self.add(rect, width_label, height_label, vertex_labels, points, bc_path,pd_line)

        self.wait(0.5)
        
        # 添加动态元素
        self.play(
            FadeIn(P, scale=0.5),
            FadeIn(P_label),
            Create(EP),
            Create(PD),
            FadeIn(EP_label),
            FadeIn(PD_label)
        )
        self.wait(0.5)

        # 动点P的移动动画（优化路径）
        self.play(
            MoveAlongPath(P, bc_path),  # 沿路径移动更自然
            run_time=6,
            rate_func=linear
        )
        
        # 反向移动动画
        self.play(
            MoveAlongPath(P, bc_path.reverse_points()),  # 沿原路径返回
            run_time=6,
            rate_func=smooth
        )
        
        self.wait(2)

# manim -p  拉格朗日.py RectangleABCD

