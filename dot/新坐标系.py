from manim import *

class FixedCoordinateSystem(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        
        # 使用 NumberPlane 替代 Axes
        grid = NumberPlane(
            x_range=[0, 8, 1],
            y_range=[-6, 6, 1],
            x_length=8,
            y_length=12,
            background_line_style={
                "stroke_color": "#546E7A",
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={
                "color": "#ECEFF1",
                "stroke_width": 2
            },
            x_axis_config={
                "numbers_to_include": np.arange(0, 9, 2),
                "numbers_with_elongated_ticks": [0, 2, 4, 6, 8]
            },
            y_axis_config={
                "numbers_to_include": np.arange(-6, 7, 2),
                "numbers_with_elongated_ticks": [-6, -4, -2, 0, 2, 4, 6]
            },
            tips=False,
        )
        
        # 添加坐标轴标签
        axis_labels = grid.get_axis_labels(x_label="x", y_label="y")
        
        # 绘制点 (0, 5)
        dot = Dot(grid.c2p(0, 5), color=YELLOW, radius=0.1)
        label = MathTex("(0, 5)", color=YELLOW).next_to(dot, UP)
        
        self.add(grid,axis_labels,dot,label)

# manim -pqh --format=png 新坐标系.py FixedCoordinateSystem -r 1920,1080