from manim import *

class ParabolaPlot(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-4, 4, 0.5],
            y_range=[-3, 3, 0.5],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1"},
            x_length=8,
            y_length=6
        )
        
        axis_labels = axes.get_axis_labels(Tex("x"), Tex("y"))
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)
        
        # 创建圆并设置样式
        circle = Circle(
            radius=3,  # 半径为3，对应方程中的9
            color=YELLOW,
            stroke_width=3
        ).move_to(origin_point)  # 确保圆心在坐标原点
        
        # 添加到场景
        self.add(grid, axes, axis_labels, origin_dot, origin_label, circle)

# manim -pqh --format=png 模板.py ParabolaPlot -r 1920,1080