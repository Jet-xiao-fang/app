from manim import *

config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MovingPointOnSemicircle(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 定义下移距离
        shift_down = DOWN * 1
        
        # 创建完整的半圆形状（包括直径）
        semicircle = VMobject()
        
        # 创建上半圆弧（圆心已经下移）
        arc = Arc(
            radius=3,
            start_angle=0,
            angle=PI,
            arc_center=ORIGIN + shift_down,  # 圆心下移
        )
        
        # 创建底部直径（自动跟随圆心下移）
        diameter = Line(
            start=arc.get_start(),
            end=arc.get_end(),
        )
        
        # 组合弧线和直径
        semicircle.append_points(arc.points)
        semicircle.append_points(diameter.points)
        
        # 设置样式
        semicircle.set_style(
            stroke_color=GREEN,
            fill_opacity=0.3,
            fill_color=BLUE,
            stroke_width=4
        )
        
        # 添加半圆到场景
        self.add(semicircle)
        
        # 添加标题
        title = Tex(r"求$AC+\frac{\sqrt{3}}{3}BC$的最大值?", font_size=46)
        title.next_to(semicircle, UP, buff=1.5)
        self.add(title)
        
        # 添加直径端点A和B（使用arc的起点和终点，已经包含下移）
        point_a = Dot(arc.get_start(), color=RED, radius=0.1)
        point_b = Dot(arc.get_end(), color=RED, radius=0.1)
        label_a = Tex("A", color=RED).next_to(point_a, DOWN)
        label_b = Tex("B", color=RED).next_to(point_b, DOWN)
        
        # 添加圆心O
        center = ORIGIN + shift_down
        dot_o = Dot(center, color=WHITE, radius=0.1)
        label_o = Tex("O", color=WHITE).next_to(dot_o, DOWN, buff=0.2)
        
        # 添加OB半径指示线（虚线）
        ob_line = Line(center, point_b.get_center(), color=RED, stroke_width=2)
        
        # 添加半径标签在OB下方
        r_label = Tex("$r=3$", font_size=42)
        # 计算OB中点并稍微向下偏移
        ob_midpoint = (center + point_b.get_center()) / 2
        r_label.next_to(ob_midpoint, DOWN, buff=0.3)
        
        # 创建动点C（初始位置在A点）
        point_c = Dot(point_a.get_center(), color=RED, radius=0.12)
        
        # 创建AC和BC线段
        ac_line = always_redraw(lambda: DashedLine(
            point_a.get_center(), 
            point_c.get_center(), 
            color=YELLOW, 
            stroke_width=3
        ))
        bc_line = always_redraw(lambda: DashedLine(
            point_b.get_center(), 
            point_c.get_center(), 
            color=GRAY, 
            stroke_width=3
        ))
        
        # 添加圆心、半径标记和端点
        self.add(dot_o, label_o, ob_line, r_label)
        self.add(point_a, label_a, point_b, label_b)
        
        # 添加动点C和线段
        self.add(point_c, ac_line, bc_line)
        
        # 创建动点C的标签
        c_label = Tex("C", color=YELLOW)
        c_label.add_updater(lambda m: m.next_to(point_c, UP))
        self.add(c_label)
        
        # 创建动点C的运动路径（半圆弧，圆心已下移）
        c_path = Arc(
            radius=3,
            start_angle=0,
            angle=PI,
            arc_center=ORIGIN + shift_down,
            color=WHITE,
            stroke_width=2
        )
        
        # 动画序列
        self.play(
            MoveAlongPath(point_c, c_path),
            run_time=4,
            rate_func=linear
        )
        self.play(
            MoveAlongPath(point_c, c_path.reverse_points()),
            run_time=4,
            rate_func=linear
        )
        self.play(
            MoveAlongPath(point_c, c_path),
            run_time=4,
            rate_func=linear
        )
        self.wait(3)

# manim -p 几何半圆.py MovingPointOnSemicircle