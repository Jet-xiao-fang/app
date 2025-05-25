from manim import *

class ParabolaPlot(Scene):  
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = WHITE
        
        # 创建坐标系（1:1 等比例）
        axes = Axes(
            x_range=[0, 4, 1],  # x轴范围：-4到4，步长1
            y_range=[0, 3, 1],  # y轴范围：-3到3，步长1
            x_length=8,          # 物理长度8单位
            y_length=6,          # 物理长度6单位
            axis_config={
                "color": BLACK,
                "stroke_width": 2,
            },
            tips=False,          # 不显示箭头
        ).set_aspect_ratio(1.0)  # 强制1:1宽高比
        
        # 添加网格系统（比默认网格更精细）
        grid = NumberPlane(
            x_range=[0, 4, 0.5],  # 细网格间隔0.5
            y_range=[0, 3, 0.5],
            background_line_style={
                "stroke_color": GREY_B,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={"color": BLACK},
            x_length=8,
            y_length=6
        )
        
        # 添加坐标标签
        axis_labels = axes.get_axis_labels(
            Tex("x").set_color(BLACK),
            Tex("y").set_color(BLACK)
        )
        
        # 组合所有元素
        self.add(grid, axes, axis_labels)
        
        # 获取坐标系的实际原点坐标
        origin_point = axes.c2p(0, 0)  # 将逻辑坐标(0,0)转换为场景坐标
        # 创建原点标记
        origin_dot = Dot(point=origin_point, color=BLACK).scale(0.8)
        origin_label = Tex("O", color=BLACK).next_to(origin_dot, DR, buff=0.1)

        self.add(origin_dot, origin_label)

                # 动画实现部分
        a_y = ValueTracker(1)  # A点初始y坐标

        # 动态计算B点坐标（根据勾股定理）
        def get_b_x():
            y = a_y.get_value()
            x = np.sqrt(2**2 - y**2)  # 根据AB=2计算x坐标
            return x

        # 创建动态点
        point_a = always_redraw(lambda: Dot(
            point=axes.c2p(0, a_y.get_value()),
            color=RED
        ))
        point_b = always_redraw(lambda: Dot(
            point=axes.c2p(get_b_x(), 0),
            color=BLUE
        ))

        # 创建动态连线
        line_ab = always_redraw(lambda: Line(
            start=point_a.get_center(),
            end=point_b.get_center(),
            color=GREEN,
            stroke_width=4
        ))

        # 添加标签
        label_a = always_redraw(lambda: Tex("A", color=RED).next_to(point_a, LEFT))
        label_b = always_redraw(lambda: Tex("B", color=BLUE).next_to(point_b, DOWN))

        # 添加长度标注
        length_label = always_redraw(lambda: DecimalNumber(2, color=GREEN)
            .next_to(line_ab.get_center(), UP, buff=0.1))

        # 组合元素
        self.add(point_a, point_b, line_ab, label_a, label_b, length_label)

        # 运行动画
        for _ in range(3):
            self.play(
                a_y.animate.set_value(2),  # A点从y=1移动到y=2
                run_time=3,                # 单程3秒
                rate_func=smooth  # 往返运动
            )
            self.play(
                a_y.animate.set_value(1),  # A点从y=1移动到y=2
                run_time=3,                # 单程3秒
                rate_func=smooth  # 往返运动
            )
        self.wait()

# manim -pqh 数学滑梯模型.py ParabolaPlot -r 1920,1080


