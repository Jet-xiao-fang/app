from manim import *
from manim.utils.space_ops import line_intersection

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MovingPointOnDC(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        tex = Tex(r"求: CP的最小值?", color=BLUE).to_edge(UP)
        self.play(Write(tex))
        
        # 创建正方形
        square = Square(side_length=4, color=WHITE, stroke_width=2.5)
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
        
        # 创建DC边（从D到C的底边）和CB边（从C到B的右边）
        line_DC = Line(vertices["D"], vertices["C"], color=GREY)
        line_CB = Line(vertices["C"], vertices["B"])
        
        # 动态点系统
        t = ValueTracker(0)
        
        # 点E在DC上移动
        e_dot = Dot(color=YELLOW, radius=0.08).add_updater(
            lambda m: m.move_to(line_DC.point_from_proportion(t.get_value()))
        )
        
        # 点F在CB上移动
        f_dot = Dot(color=YELLOW_C, radius=0.08).add_updater(
            lambda m: m.move_to(line_CB.point_from_proportion(t.get_value()))
        )
        
        # E和F的标签
        e_label = MathTex("E", color=YELLOW, font_size=24).add_updater(
            lambda m: m.next_to(e_dot, UP, buff=0.12)
        )
        f_label = MathTex("F", color=YELLOW, font_size=24).add_updater(
            lambda m: m.next_to(f_dot, LEFT, buff=0.12)
        )
        
        # 动态连接线AE和DF
        line_ae = always_redraw(lambda: Line(
            vertices["A"], e_dot.get_center(),
            color=BLUE_B, stroke_width=2.5
        ))
        
        line_df = always_redraw(lambda: Line(
            vertices["D"], f_dot.get_center(),
            color=BLUE_B, stroke_width=2.5
        ))
        
        # 创建点P作为AE和DF的交点
        p_dot = Dot(color=RED, radius=0.1)
        p_label = MathTex("P", color=RED, font_size=24).add_updater(
            lambda m: m.next_to(p_dot, UR, buff=0.12)
        )
        
        # 更新点P的位置（作为AE和DF的交点）
        def update_p_dot(m):
            try:
                # 计算两条线的交点
                intersection = line_intersection(
                    [line_ae.get_start(), line_ae.get_end()],
                    [line_df.get_start(), line_df.get_end()]
                )
                m.move_to(intersection)
            except:
                # 如果无法计算交点（如两线平行），保持原位
                pass
        p_dot.add_updater(update_p_dot)
        
        # 创建连接线PC
        line_pc = always_redraw(lambda: Line(
            p_dot.get_center(), vertices["C"],
            color=GREEN, stroke_width=2.5
        ))
        
        # 添加所有元素
        self.add(square, labels, line_DC, line_CB)
        self.add(e_dot, f_dot, e_label, f_label, line_ae, line_df)
        self.add(p_dot, p_label, line_pc)
        
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
        
        # 添加注释解释点P
        explanation = Tex("P: AE和DF的交点", color=YELLOW).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # 放大P点移动部分
        self.play(
            t.animate.set_value(0),
            rate_func=linear,
            run_time=3
        )
        
        # 显示跟踪路径
        path = TracedPath(p_dot.get_center, stroke_color=RED, stroke_width=2.5)
        self.add(path)
        self.play(
            t.animate.set_value(1),
            rate_func=linear,
            run_time=10
        )
        self.wait(2)
        
        # 最终聚焦在PC上
        pc_group = VGroup(p_dot, line_pc, p_label)
        self.play(
            pc_group.animate.scale(1.5).shift(UP*0.5),
            run_time=2
        )
        
        # 添加最终文本
        final_text = Tex("观察CP长度的变化", color=GREEN).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(3)
        
        # 淡出所有内容
        self.play(*[FadeOut(mob) for mob in self.mobjects])

# manim -pqh 正方形移动1.py MovingPointOnDC -r 1920,1080