from manim import *

class manimModule(Scene):
    def construct(self):
            self.camera.background_color = "#263238"
            axes = Axes(
                x_range=[-8, 8, 1],
                y_range=[-2, 6, 1],
                x_length=16,
                y_length=8,
                
                axis_config={"color": "#ECEFF1", "stroke_width": 2},
                tips=False,
            ).set_aspect_ratio(1.0)
            
            grid = NumberPlane(
                x_range=[-8, 8, 0.5],
                y_range=[-2, 6, 0.5],
                background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
                axis_config={"color": "#ECEFF1"},
                x_length=16,
                y_length=8
                
            )
            
            axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))  # 使用MathTex
            origin_point = axes.c2p(0, 0)
            origin_dot = Dot(point=origin_point).scale(0.8)
            origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

            self.add(axes,grid,axis_labels,origin_dot,origin_label)

# manim -pqh --format=png test.py manimModule -r 1920,1080