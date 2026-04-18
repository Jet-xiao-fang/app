from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class AnimateSquareWithAPBP(Scene):
    def construct(self):
         # 设置背景为深空蓝
        self.camera.background_color = "#0F0F1A"
        # 配置参数
        side_length = 5
        half = side_length / 2
        fill_color = "#1F2430"
        
        # 顶点坐标（中心在原点）
        A = [-half, -half, 0]  # 左下
        B = [half, -half, 0]   # 右下
        C = [half, half, 0]     # 右上
        D = [-half, half, 0]    # 左上

        # 绘制带填充色的正方形
        square = Polygon(A, B, C, D, 
                        color=WHITE,
                        fill_color=fill_color,
                        fill_opacity=1)
        self.add(square)
        titile = Tex("求AP+BP最小值",color=BLUE).next_to(square,UP,buff = 1.5)
        self.add(titile)

        # 顶点标签配置
        label_conf = {
            "A": {"direction": DOWN, "buff": 0.2},
            "B": {"direction": DOWN, "buff": 0.2},
            "C": {"direction": RIGHT, "buff": 0.2},
            "D": {"direction": LEFT, "buff": 0.2},
        }
        for text, pos in zip(["A", "B", "C", "D"], [A, B, C, D]):
            conf = label_conf[text]
            label = Tex(text).next_to(pos, conf["direction"], buff=conf["buff"])
            self.add(label)

        # 创建E点（AD中点）
        E_point = midpoint(np.array(A), np.array(D))
        E = Dot(E_point, color=YELLOW)
        label_E = Tex("E").next_to(E, LEFT, buff=0.2)
        self.add(E, label_E)

        # 绘制线段CE
        line_ce = Line(C, E_point, color=BLUE)
        self.add(line_ce)

        # 动态元素
        t = ValueTracker(0)
        
        # 动点P及其标签
        dot_p = always_redraw(lambda: Dot(
            color=RED,
            radius=0.08
        ).move_to(line_ce.point_from_proportion(t.get_value())))
        
        label_p = always_redraw(lambda: Tex("P").scale(0.8).next_to(
            dot_p, UR, buff=0.1
        ))

        # AP和BP连线（实时更新）
        line_ap = always_redraw(lambda: Line(
            A, dot_p.get_center(),
            color=GREEN_B,
            stroke_width=2
        ))
        
        line_bp = always_redraw(lambda: Line(
            B, dot_p.get_center(),
            color=GREEN_B,
            stroke_width=2
        ))

        # 添加所有动态元素
        self.add(line_ap, line_bp, dot_p, label_p)

        # 运行动画（P点往返移动）
        self.play(
            t.animate.set_value(1),
            run_time=8,
            rate_func=there_and_back
        )
        self.wait(4)

# manim -p 将军饮马.py AnimateSquareWithAPBP