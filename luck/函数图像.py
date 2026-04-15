from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class ConeVolumeProof(Scene):
    def construct(self):

        
        # 定义函数
        def func(x):
            return 0.5 * x**2 - 2 * x - 6
        
        # 创建坐标系 - 移除 scale(0.9)
        axes = Axes(
            x_range=[-2, 6, 1],
            y_range=[-8, 2, 1],
            x_length=8,
            y_length=10,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False
        ).set_aspect_ratio(1.0).shift(DOWN*0.5)  # 向下移动0.5单位使整体居中
        title = Tex(r"求$AF$的最小值？", 
                   font_size=48, color=YELLOW)
        title.next_to(axes,UP,buff=1.5)
        # 添加坐标标签
        # 添加坐标轴标签
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        origin_label = Tex("O", font_size=24).next_to(axes.c2p(0,0), DL, SMALL_BUFF)
        
        self.add(axes,x_label,y_label,title)
        
        
        
        # 创建函数图像
        graph = axes.plot(func, color=GREEN)
        
        # 添加函数标签
        #func_label = MathTex("y = 0.5x^{2} - 2x - 6").next_to(graph, UR, buff=0.2)
        func_label=axes.get_graph_label(
            graph=graph,
            label=MathTex(r"y = 0.5x^{2} - 2x - 6").scale(0.8),
            x_val=3,  # 指定x=3处的标签位置
            direction=DOWN,
            buff=0.5,
            dot=False  # 不显示定位点
        ).set_color(RED)
        
        root1 = Dot(axes.c2p(-2, 0), color=YELLOW)
        root2 = Dot(axes.c2p(6, 0), color=YELLOW)
        root1_label = MathTex("A",color=BLUE).next_to(root1, DOWN)
        root2_label = MathTex("B",color=BLUE).next_to(root2, DOWN)
         # 添加圆心标记
        center = Dot(axes.c2p(0, -6), color=RED)
        center_label = MathTex("C",color=BLUE).next_to(center, LEFT,buff=0.1)
        
        circle = Circle(
            radius=2,
            color=YELLOW,
            stroke_width=3
        ).move_to(axes.c2p(0,-6))
        
        self.play(Create(graph), Write(func_label),Create(circle))
        self.play(FadeIn(root1), FadeIn(root2), 
                 Write(root1_label), Write(root2_label),
                 Write(center), Write(center_label))
        
        self.wait(0.5)
                # 创建点E在圆上运动
        e_dot = Dot(color=PURPLE)
        e_label = MathTex("E", color=BLUE).scale(0.8)
        
        # 创建BE线段
        be_line = always_redraw(lambda: Line(
            root2.get_center(),
            e_dot.get_center(),
            color=BLUE,
            stroke_width=2
        ))
        
        # 创建F点（BE的中点）
        f_dot = Dot(color=ORANGE)
        f_label = MathTex("F", color=BLUE).scale(0.8)
        f_dot.add_updater(lambda m: m.move_to(
            (root2.get_center() + e_dot.get_center())/2
        ))
        f_label.add_updater(lambda m: m.next_to(f_dot, UR, buff=0.1))
        
        # 创建AF线段
        af_line = always_redraw(lambda: Line(
            root1.get_center(),
            f_dot.get_center(),
            color=RED,
            stroke_width=2
        ))
        
        # 添加所有元素
        self.add(be_line, e_dot, e_label, f_dot, f_label, af_line)
        
        # 让E点绕圆运动
        def update_e(mob, alpha):
            angle = alpha * 2 * PI  # 完整的一圈
            mob.move_to(circle.point_at_angle(angle))
            e_label.next_to(mob, UR, buff=0.1)
        
        # 创建动画
        self.play(
            MoveAlongPath(
                e_dot, circle,
                rate_func=linear,
                run_time=12
            ),
            UpdateFromAlphaFunc(
                e_dot, update_e,
                rate_func=linear,
                run_time=12
            ),
        )
        
        self.wait(2)
        
# 运行命令: manim -p 函数图像.py ConeVolumeProof