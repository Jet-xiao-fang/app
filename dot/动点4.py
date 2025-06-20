from manim import *
import numpy as np
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-4, 4, 0.5],
            y_range=[-4, 4, 0.5],
            x_length=8,
            y_length=8,
            background_line_style={
                "stroke_color": "#546E7A",
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={"color": "#ECEFF1"},
        )
        titile = Tex("求OB的最小值?",color=BLUE,font_size=56).next_to(axes,UP,buff = 1)
        self.add(titile)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        
        # 点A(2,0)
        A_coords = (2, 0)
        A_point = Dot(axes.c2p(*A_coords), color=RED)
        Label_A = Tex("A").next_to(A_point, LEFT, buff=0.1)
        
        # 圆（圆心在原点，半径1）
        circle = Circle(
            radius=1,
            color=BLUE_C,
            stroke_width=4
        ).move_to(axes.c2p(0, 0))
        
        center_dot = Dot(
            point=circle.get_center(),
            color=RED,
            radius=0.08
        )
        
        # 创建点P（在圆上）
        p_dot = Dot(color=YELLOW).scale(0.8)
        p_label = Tex("P").scale(0.8)
        
        # 创建点B（等腰直角三角形的第三个顶点）
        b_dot = Dot(color=GREEN).scale(0.8)
        b_label = Tex("B").scale(0.8)
        
        # 创建三角形APB（提供初始顶点）
        triangle = Polygon(
            A_point.get_center(),  # 顶点A
            A_point.get_center(),  # 临时顶点P
            A_point.get_center(),  # 临时顶点B
            color=TEAL,
            stroke_width=3
        ).set_fill(TEAL, opacity=0.3)
        
        # 创建OB直线（连接原点O和点B）
        ob_line = Line(origin_point, b_dot.get_center(), color=ORANGE, stroke_width=2.5)
        ob_label = Tex("OB").scale(0.7).set_color(ORANGE)
        
        # 角度跟踪器（控制P点位置）
        theta = ValueTracker(0)
        
        # 更新函数：根据角度更新P、B位置和三角形
        def update_points(m):
            angle = theta.get_value()
            
            # 更新P点位置 (cosθ, sinθ)
            p_x = np.cos(angle)
            p_y = np.sin(angle)
            p_pos = axes.c2p(p_x, p_y)
            p_dot.move_to(p_pos)
            p_label.next_to(p_dot, UR, buff=0.1)
            
            # 计算B点位置（使APB成为等腰直角三角形）
            # 向量PA
            pa_x = 2 - p_x
            pa_y = -p_y  # A点y坐标为0
            
            # 固定使用逆时针旋转：(x, y) -> (-y, x)，代表的是旋转了90度
            pb_x = -pa_y
            pb_y = pa_x
            
            # B点位置 = P点位置 + PB向量
            b_x = p_x + pb_x
            b_y = p_y + pb_y
            b_pos = axes.c2p(b_x, b_y)
            b_dot.move_to(b_pos)
            b_label.next_to(b_dot, UR, buff=0.1)
            
            # 更新三角形顶点（只需3个点）
            triangle.set_points_as_corners([
                A_point.get_center(),  # A点
                p_pos,                 # P点
                b_pos                  # B点
            ])
            
            # 更新OB直线
            ob_line.put_start_and_end_on(origin_point, b_pos)
            
            # 更新OB标签位置（OB线段的中点）
            ob_label.move_to(ob_line.get_center() + np.array([0.2, 0.2, 0]))
        
        # 添加更新器
        p_dot.add_updater(update_points)
        p_label.add_updater(lambda m: m.next_to(p_dot, UR, buff=0.1))
        b_dot.add_updater(update_points)
        b_label.add_updater(lambda m: m.next_to(b_dot, UR, buff=0.1))
        triangle.add_updater(update_points)
        
        # 添加初始元素
        self.add(axes, grid, axis_labels, origin_dot, origin_label, 
                A_point, Label_A, circle, center_dot)
        
        # 添加动态元素
        self.add(p_dot, p_label, b_dot, b_label, triangle, ob_line, ob_label)
        
        # 添加直角标记 - 使用always_redraw避免初始零长度问题
        def create_right_angle():
            line1 = Line(A_point.get_center(), p_dot.get_center())
            line2 = Line(p_dot.get_center(), b_dot.get_center())
            
            # 避免零长度线段
            if line1.get_length() < 0.01 or line2.get_length() < 0.01:
                return VMobject()
                
            return RightAngle(
                line1, line2,
                length=0.2,
                color=YELLOW,
                stroke_width=3
            )
        
        right_angle = always_redraw(create_right_angle)
        self.add(right_angle)
        
        # 初始化位置
        update_points(None)
        
        # 动画：让P点绕圆运动
        self.play(
            theta.animate.set_value(2*PI),
            run_time=12,
            rate_func=linear
        )
        
        # 保持最后一帧
        self.wait(3)


# manim -pqh --format=png 动点4.py ParabolaPlot -r 1920,1080