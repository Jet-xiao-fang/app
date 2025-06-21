from manim import *
import math
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
            x_range=[-6, 6, 1],
            y_range=[0, 6, 1],
            x_length=12,
            y_length=6,
            
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-6, 6, 0.5],
            y_range=[0, 6, 0.5],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1"},
            x_length=12,
            y_length=6
            
        )

        # 将坐标轴和网格组合为一个整体
        coordinate_system  = VGroup(axes,grid)
        # 整体向上移动 1.5 单位（可根据需求调整数值）
        coordinate_system.shift(UP * 0.5)
        titile = Tex("求OE的最大值?",color=YELLOW,font_size=56).next_to(coordinate_system,UP,buff = 1)
        self.add(titile)
        
        axis_labels = coordinate_system[0].get_axis_labels(MathTex("x"), MathTex("y"))  # 使用MathTex
        origin_point = coordinate_system[0].c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        # 创建半径为2的上半圆，圆心在原点
        semicircle = Arc(
            radius=1,          # 半径改为2
            start_angle=0,     # 从右侧开始（0弧度）
            angle=2*PI,          # 画180°（上半圆）
            color=RED,
            arc_center=coordinate_system[0].c2p(3, 0),  # 直接指定圆心坐标
            stroke_width=4
        )
        A_coords = (3, 0)  # 数学坐标系中的坐标
        A_point = Dot(coordinate_system[0].c2p(*A_coords), color=RED)  # 转换到场景坐标系
        Label_A = Tex("A").next_to(A_point, DOWN, buff=0.1)

        B_coords = (0, 4)  # 数学坐标系中的坐标
        B_point = Dot(coordinate_system[0].c2p(*B_coords), color=RED)  # 转换到场景坐标系
        Label_B = Tex("B").next_to(B_point, LEFT, buff=0.1)

        
        # 动点P的初始位置（右侧端点）
        P = coordinate_system[0].c2p(2, 0)  # 圆心(3,0) + 半径(2,0)
        P_dot = Dot(P, color=BLUE).scale(0.8)
        # 初始连接线段BP
        BP_line = Line(B_point.get_center(), P, color=YELLOW, stroke_width=2)
        # 中点E的初始位置
        E = (B_point.get_center() + P) / 2  # 向量相加取中点
        E_dot = Dot(E, color=ORANGE).scale(0.6)
        E_label = Tex("E").next_to(E_dot, RIGHT, buff=0.1)
        # 初始连接线段OE
        OE_line = Line(origin_point, E, color=BLUE, stroke_width=2)

        #添加初始元素
        self.add(coordinate_system,
                 axis_labels, 
                 origin_dot, 
                 origin_label,
                 semicircle,
                 Label_A,
                 A_point,
                 B_point,
                 Label_B,
                 P_dot,
                 BP_line, E_dot, OE_line)
        
        self.play(
            Rotate(
                P_dot, # 旋转的对象
                about_point= A_point.get_center(),
                angle= 2 * 2 * PI,
                run_time = 12,
                rate_functions = linear

            ),
            UpdateFromFunc(BP_line,lambda line: line.put_start_and_end_on(
                B_point.get_center(),P_dot.get_center()
            )),
            UpdateFromFunc(E_dot,lambda dot: dot.move_to(
                (B_point.get_center()+P_dot.get_center())/2
            )),
            # 新增：动态更新E标签
            UpdateFromFunc(E_label, lambda label: label.next_to(E_dot, RIGHT, buff=0.1)),
            UpdateFromFunc(OE_line,lambda line: line.put_start_and_end_on(
                origin_dot.get_center(),E_dot.get_center()
            )),
            run_time = 12
        )
        self.wait(2)

        
        
      
# manim -pqh 全圆.py ParabolaPlot -r 1920,1080