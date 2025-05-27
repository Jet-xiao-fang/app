from manim import *
from util import create_point_with_label

class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-2, 6, 1],
            x_length=12,
            y_length=8,
            
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-6, 6, 0.5],
            y_range=[-2, 6, 0.5],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1"},
            x_length=12,
            y_length=8
            
        )

        # 将坐标轴和网格组合为一个整体
        coordinate_system  = VGroup(axes,grid)
        # 整体向上移动 1.5 单位（可根据需求调整数值）
        # coordinate_system.shift(UP * 0.5)
        
        axis_labels = coordinate_system[0].get_axis_labels(MathTex("x"), MathTex("y"))  # 使用MathTex
        origin_point = coordinate_system[0].c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        # 创建半径为2的上半圆，圆心在原点
        semicircle = Arc(
            radius=1,          # 半径改为2
            start_angle=0,     # 从右侧开始（0弧度）
            angle=4*PI,          # 画180°（上半圆）
            color=RED,
            arc_center=coordinate_system[0].c2p(4, 0),  # 直接指定圆心坐标
            stroke_width=1
        )
        # 创建直线 y = x + 4
        line = coordinate_system[0].plot(
            lambda x: x + 4,          # 函数表达式
            color=GREEN,             # 直线颜色
            stroke_width=3            # 线宽
        )

        # 添加直线标签（可选）
        # line_label = MathTex("y = x + 4").next_to(line, DR, buff=0.2).set_color(YELLOW)
        line_label = MathTex("y=x+4").move_to(coordinate_system[0].c2p(-0.5,3.5)).set_color(YELLOW).shift(UL * 0.8)
        self.add(coordinate_system,axis_labels,origin_dot,origin_label,semicircle,line,line_label)

        # point_A = (4,0)
        # A = Dot(coordinate_system[0].c2p(*point_A),color=RED)
        # Label_A = Tex("A").next_to(A, UP, buff=0.1)
        # 使用工具函数创建点A(4,0)
        point_A = create_point_with_label(coordinate_system[0], (4, 0), "A", 
                                          color=RED,name_scale=0.5,coord_scale=0.5)
        self.add(point_A)


         # 计算从P点到圆A的切点Q（只保留上半圆切点）
        def get_upper_tangent_point(p):
            """返回直线y=x+4上点p到圆A的上半圆切点Q"""
            C = np.array([4, 0])  # 圆心
            r = 1                 # 半径
            P = np.array(axes.p2c(p))  # 将P点坐标转换为数学坐标
            
            # 向量PC
            PC = C - P
            dist_PC = np.linalg.norm(PC)
            
            # 如果没有交点（点在圆内）
            if dist_PC < r:
                return axes.c2p(4, 1)  # 返回圆顶默认点
            
            # 计算切点（使用几何公式）
            angle = np.arccos(r/dist_PC)
            tangent_length = np.sqrt(dist_PC**2 - r**2)
            
            # 旋转向量PC得到两个切点方向
            rot_matrix1 = np.array([[np.cos(angle), -np.sin(angle)],
                                  [np.sin(angle), np.cos(angle)]])
            rot_matrix2 = np.array([[np.cos(-angle), -np.sin(-angle)],
                                  [np.sin(-angle), np.cos(-angle)]])
            
            dir_vector1 = rot_matrix1.dot(PC) * (r/dist_PC)
            dir_vector2 = rot_matrix2.dot(PC) * (r/dist_PC)
            
            Q1 = C + dir_vector1
            Q2 = C + dir_vector2
            
            # 只返回y坐标为正的切点
            if Q1[1] > 0:
                return axes.c2p(*Q1)
            else:
                return axes.c2p(*Q2)

        # 创建动点P和相关的动态元素
        p_start = axes.c2p(-2, 2)  # 起点
        p_end = axes.c2p(2, 6)     # 终点
        
        p_dot = Dot(color=BLUE).move_to(p_start)
        p_label = Tex("P").next_to(p_dot, UR, buff=0.1).scale(0.5)
        
        # 创建切点Q（只考虑上半圆）
        q_dot = Dot(color=PURPLE)
        q_label = Tex("Q").next_to(q_dot, UR, buff=0.1).scale(0.5)
        
        # 创建切线PQ
        tangent_line = Line(color=YELLOW, stroke_width=2)
        
        # 添加所有动态元素
        self.add(p_dot, p_label, q_dot, q_label, tangent_line)

        # 更新函数（只更新上半圆切点）
        def update_tangent(mob):
            q_point = get_upper_tangent_point(p_dot.get_center())
            q_dot.move_to(q_point)
            q_label.next_to(q_dot, UR, buff=0.1)
            tangent_line.put_start_and_end_on(
                p_dot.get_center(), q_point
            )

        # 添加更新器
        p_dot.add_updater(lambda m: update_tangent(m))
        
        # 执行动画
        self.play(
            p_dot.animate.move_to(p_end),
            rate_func=there_and_back,
            run_time=12
        )
        
        # 移除更新器
        p_dot.remove_updater(lambda m: update_tangent(m))
        
        self.wait(2)
        
      
# manim -pqh --format=png 背景图.py ParabolaPlot -r 1920,1080