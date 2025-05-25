from manim import *

class ParabolaPlot(Scene):  
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = WHITE
        
        # 创建坐标系（1:1 等比例）
        axes = Axes(
            x_range=[-4, 4, 1],  # x轴范围：-4到4，步长1
            y_range=[-3, 3, 1],  # y轴范围：-3到3，步长1
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
            x_range=[-4, 4, 0.5],  # 细网格间隔0.5
            y_range=[-3, 3, 0.5],
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
        
        # 验证等比例：绘制正圆和对角线
        circle = Circle(radius=2, color=BLUE, stroke_width=4)
        diag_line = Line(start=axes.c2p(-3,-3), end=axes.c2p(3,3), color=RED)
        # 创建抛物线 y = x²
        parabola = axes.plot(
            lambda x: x**2, 
            x_range=[-1.5, 1.5],  # x范围稍小于坐标轴范围
            color=GREEN,
            stroke_width=3
        )
        
        # 添加方程标签
        equation = MathTex("y = x^2", color=GREEN).next_to(parabola, UR, buff=0.2)
        
        # 组合所有元素
        self.add(grid, axes, axis_labels, circle, diag_line,equation,parabola)
        
        # 显示坐标原点标记
        origin_dot = Dot(color=BLACK).scale(0.8)
        origin_label = Tex("O", color=BLACK).next_to(origin_dot, DR, buff=0.1)
        self.add(origin_dot, origin_label)

#  manim -pqh --format=png 绘制曲线.py ParabolaPlot -r 1920,1080
