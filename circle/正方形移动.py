from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class MovingPointOnDC(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
         # 1. 创建Tex对象
        tex = Tex(r"求AP:BP的最大值?").to_edge(UP)
        
        # 2. 使用Write动画显示文本
        self.play(Write(tex))
        # 创建正方形
        square = Square(side_length=3, color=WHITE, stroke_width=2.5)
        square.move_to(ORIGIN)
        
        # 获取顶点坐标
        vertices = {
            "A": square.get_corner(UL),  # 左上
            "B": square.get_corner(UR),  # 右上
            "C": square.get_corner(DR),  # 右下
            "D": square.get_corner(DL)   # 左下
        }
        
        # 顶点标签
        labels = VGroup(*[
            MathTex(label, color=WHITE, font_size=28).next_to(
                point, direction, buff=0.18
            ) for label, point, direction in zip(
                ["A", "B", "C", "D"],
                vertices.values(),
                [UL, UR, DR, DL]
            )
        ])
        
        # 创建DC边（从D到C的底边）
        line_DC = Line(vertices["D"], vertices["C"], color=GREY)
        
        # 动态点P系统
        t = ValueTracker(0)
        p_dot = Dot(color=YELLOW, radius=0.08).add_updater(
            lambda m: m.move_to(line_DC.point_from_proportion(t.get_value()))
        )
        p_label = MathTex("P", color=YELLOW, font_size=24).add_updater(
            lambda m: m.next_to(p_dot, UP, buff=0.12)
        )
        
        # 动态连接线AP和BP
        line_ap = always_redraw(lambda: Line(
            vertices["A"], p_dot.get_center(),
            color=BLUE_B, stroke_width=2.5
        ))
        line_bp = always_redraw(lambda: Line(
            vertices["B"], p_dot.get_center(),
            color=GREEN_B, stroke_width=2.5
        ))
        
        # 添加所有元素
        self.add(square, labels, line_DC)
        self.add(p_dot, p_label, line_ap, line_bp)
        
        # 运行动画
        self.play(
            t.animate.set_value(1),
            rate_func=linear,
            run_time=5
        )
        self.play(
            t.animate.set_value(0),
            rate_func=linear,
            run_time=5
        )
        self.play(
            t.animate.set_value(1),
            rate_func=linear,
            run_time=5
        )
        self.wait()

# manim -pqh 正方形移动.py MovingPointOnDC -r 1920,1080