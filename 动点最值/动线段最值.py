from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class CosTaylorApproximation(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 坐标系配置
        axes = Axes(
            x_range=[-3, 6, 1],
            y_range=[-2, 4, 1],
            x_length=9,
            y_length=6,
            axis_config={"color": "#ECEFF1", "stroke_width": 3},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y")) 
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DL, buff=0.1)
        tex = Tex(r"$PA+2PB$的最小值？", color=YELLOW).next_to(axes,UP,buff=1.5)
        self.add(axes,origin_dot,axis_labels,origin_label,tex)
        
        A=Dot(axes.c2p(0,1),color=RED)
        a_label=MathTex("A").next_to(A,LEFT,buff=0.1)
        B=Dot(axes.c2p(3,2),color=RED)
        b_label=MathTex("B").next_to(B,RIGHT,buff=0.1)
        self.add(A,a_label,B,b_label)
        
        P = Dot(axes.c2p(0,0),color=YELLOW)
        p_label=always_redraw(lambda: MathTex("P",color=PINK).next_to(P,DOWN,buff=0.1))
        AP=always_redraw(lambda: Line(A.get_center(),P.get_center(),color=GREEN,stroke_width=4))
        BP=always_redraw(lambda: Line(B.get_center(),P.get_center(),color=GREEN,stroke_width=4))
        self.add(P,p_label,AP,BP)
        self.play(
            P.animate.move_to(axes.c2p(4, 0)),
            run_time=4,
            rate_func=linear
        )
        self.play(
            P.animate.move_to(axes.c2p(-1, 0)),
            run_time=4,
            rate_func=linear
        )
        self.play(
            P.animate.move_to(axes.c2p(3, 0)),
            run_time=4,
            rate_func=linear
        )
        self.wait(3)
        

#   manim -p 动线段最值.py CosTaylorApproximation