from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class RotatingTangentLine(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 创建坐标系（1:1 等比例）
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=6,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
            },
            tips=False,
        ).set_aspect_ratio(1.0)
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(
            Tex("x").set_color(WHITE),
            Tex("y").set_color(WHITE)
        )
        describe = Tex(
            r"$\left( x-2 \right)^{2} + y^{2} = 3$, 求 $\frac{y}{x}$ 的最大值?",
            font_size=42,
            color=YELLOW
        ).next_to(axes, UP, buff=1.5)
        
        # 组合所有元素
        self.add(axes, axis_labels)
        self.play(Write(describe))
        self.wait(0.5)
        
        # 创建圆心在 (2,0) 的点
        center = Dot(point=axes.c2p(2, 0), color=YELLOW)
        center_label = MathTex("C(2,0)", color=WHITE).next_to(center, DR, buff=0.1).scale(0.5)
        
        # 创建半径为 √3 的圆
        circle = Circle(
            radius=np.sqrt(3),
            color=GREEN,
            stroke_width=3
        ).move_to(axes.c2p(2, 0))
        
        self.play(Write(center), Write(center_label))
        self.wait(0.5)
        self.play(Create(circle))
        self.wait(2)
        
        # 创建原点 O
        origin = Dot(axes.c2p(0, 0), color=RED)
        origin_label = MathTex("O(0,0)", color=WHITE).next_to(origin, DL, buff=0.1).scale(0.5)
        self.play(Create(origin), Write(origin_label))
        self.wait(0.5)
        
        # 绘制初始直线 y = -√3 x
        line = Line(
            start=axes.c2p(0, 0),
            end=axes.c2p(1, -np.sqrt(3)),  # 初始终点
            color=RED,
            stroke_width=2.5
        )
        
        # 添加直线标签 y = kx
        line_label = MathTex("y = kx", color=RED).next_to(line, UR, buff=0.1)
        
        self.play(Create(line), Write(line_label))
        self.wait(1)
        
        # 旋转直线，k 从 -√3 到 √3
        def update_line(line, alpha):
            k = -np.sqrt(3) + alpha * 2 * np.sqrt(3)  # k ∈ [-√3, √3]
            
            # 计算直线终点，确保不超出坐标系范围
            x_max = 4  # x 轴最大值
            y_max = 3  # y 轴最大值
            
            # 判断是否优先触达 x 或 y 边界
            if abs(k) > y_max / x_max:
                # 直线较陡，优先触达 y 边界
                y_end = y_max if k > 0 else -y_max
                x_end = y_end / k
            else:
                # 直线较平，优先触达 x 边界
                x_end = x_max
                y_end = k * x_end
            
            new_line = Line(
                start=axes.c2p(0, 0),
                end=axes.c2p(x_end, y_end),
                color=RED,
                stroke_width=2.5
            )
            line.become(new_line)
            # 更新标签位置
            line_label.next_to(new_line, UR, buff=0.1)
        
        self.play(
            UpdateFromAlphaFunc(
                line,
                update_line,
                run_time=4,  # 旋转动画时长
            ),
            UpdateFromAlphaFunc(
                line_label,
                lambda m, a: m.next_to(line, UR, buff=0.1),  # 标签跟随直线
                run_time=4
            )
        )
        self.wait(1)
        max_slope = MathTex(r"\text{最大斜率 } k = \sqrt{3}").to_edge(DOWN,buff=2.5)
        proof_step1 = MathTex(
            r"\text{当直线 } y=kx \text{ 与圆相切时，有唯一交点}",
            r"\text{联立方程解得 } k = \pm\sqrt{3}"
        ).arrange(DOWN).next_to(max_slope, UP, buff=0.5).scale(0.8)
        
        self.play(Write(max_slope))
        self.wait(1)
        self.play(Write(proof_step1))
        self.wait(3)

#    manim -pqh 圆上最大值.py RotatingTangentLine -r 1920,1080