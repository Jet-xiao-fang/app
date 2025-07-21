from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class MovingPointOnDC(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 创建正方形
        square = Square(side_length=4, color=BLUE)
        square.set_fill(color=BLUE,opacity=0.5)
        square.move_to(ORIGIN)
        titile = Tex(r"求$CP$的最小值?", color=YELLOW).next_to(square,UP,buff=1.5);
        # 获取顶点坐标
        vertices = [
            square.get_corner(UL),  # 左上A
            square.get_corner(UR),  # 右上B
            square.get_corner(DR),  # 右下C
            square.get_corner(DL)   # 左下D
        ]
        labels = ["A", "B", "C", "D"]
        dots = []
        texts = []
        for idx, (corner, label) in enumerate(zip(vertices, labels)):
            dot = Dot(corner, color=RED)
            if idx == 0:  # A (左下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UL, buff=0.1)
            elif idx == 1:  # B (右下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UR, buff=0.1)
            elif idx == 2:  # C (右上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DR, buff=0.1)
            elif idx == 3:  # D (左上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DL, buff=0.1)

            dots.append(dot)
            texts.append(text)
        width_label = Text("4", color=YELLOW, font_size=36)
        width_label.next_to(square, RIGHT, buff=0.2)
        self.add(titile,width_label,square,*dots, *texts)
        # 创建DC边（从D到C的底边）和CB边（从C到B的右边）
        line_DC = Line(vertices[3], vertices[2],color=BLUE)
        line_CB = Line(vertices[2], vertices[1],color=BLUE)
        self.add(line_DC,line_CB)
        
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
        e_label = MathTex("E", font_size=24).add_updater(
            lambda m: m.next_to(e_dot, UP, buff=0.1)
        )
        f_label = MathTex("F", font_size=24).add_updater(
            lambda m: m.next_to(f_dot, LEFT, buff=0.1)
        )
        
        # 动态连接线AE和DF
        line_ae = always_redraw(lambda: Line(
            vertices[0], e_dot.get_center(),
            color=PURPLE, stroke_width=4
        ))
        
        line_df = always_redraw(lambda: Line(
            vertices[3], f_dot.get_center(),
            color=PURPLE, stroke_width=4
        ))
        
        # 创建点P作为AE和DF的交点
        p_dot = Dot(color=RED, radius=0.1)
        p_label = MathTex("P", color=RED, font_size=36).add_updater(
            lambda m: m.next_to(p_dot, UP, buff=0.1)
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
            p_dot.get_center(), vertices[2],
            color=RED, stroke_width=4
        ))
        
        # 添加所有元素
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
        # 显示跟踪路径
        path = TracedPath(p_dot.get_center, stroke_color=RED, stroke_width=2.5)
        self.add(path)
        self.play(
            t.animate.set_value(1),
            rate_func=linear,
            run_time=6
        )
        self.wait(1)
        
        # 最终聚焦在PC上
        pc_group = VGroup(p_dot, line_pc, p_label)
        self.play(
            pc_group.animate.scale(1.5).shift(UP*0.5),
            run_time=2
        )
        self.wait(2)

# manim -pqh 正方形移动1.py MovingPointOnDC -r 1920,1080