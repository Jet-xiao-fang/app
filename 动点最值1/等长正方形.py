from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class MathSymbolsScene(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        rectangle = Rectangle(width=4, height=4, color=BLUE)
        rectangle.set_fill(color=BLUE, opacity=0.3)
        titile = Tex("求$BM$的最小值？",color=YELLOW).next_to(rectangle,UP,buff = 1.5)
        corners = [
            rectangle.get_corner(DL),  # 左下 (A)
            rectangle.get_corner(DR),  # 右下 (B)
            rectangle.get_corner(UR),  # 右上 (C)
            rectangle.get_corner(UL)  # 左上 (D)
        ]
        self.add(titile)
        labels = ["A", "B", "C", "D"]
        dots = []
        texts = []
        for idx, (corner, label) in enumerate(zip(corners, labels)):
            dot = Dot(corner, color=RED)
            if idx == 0:  # A (左下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DL, buff=0.1)
            elif idx == 1:  # B (右下)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, DR, buff=0.1)
            elif idx == 2:  # C (右上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UR, buff=0.1)
            elif idx == 3:  # D (左上)
                text = Text(label, color=WHITE, font_size=24).next_to(dot, UL, buff=0.1)

            dots.append(dot)
            texts.append(text)
        length_label = Text("4", color=YELLOW, font_size=20)
        length_label.next_to(rectangle, DOWN, buff=0.2)

        width_label = Text("4", color=YELLOW, font_size=20)
        width_label.next_to(rectangle, RIGHT, buff=0.2)

        self.add(length_label, width_label)

        self.add(rectangle, *dots, *texts)
        # 点P
        dot_P = Dot(color=GREEN).move_to(rectangle.get_corner(DL))
        
        # 点Q
        dot_Q = Dot(color=YELLOW).move_to(rectangle.get_corner(UL))
           
        self.add(dot_P, dot_Q,)
        
        value_tracker = ValueTracker(0)
        
        line_AD = Line(rectangle.get_corner(DL), rectangle.get_corner(UL), color=BLUE)
        line_DC = Line(rectangle.get_corner(UL), rectangle.get_corner(UR), color=BLUE)
        self.add(line_AD, line_DC)
        
        dot_P.add_updater(lambda m: m.move_to(line_AD.point_from_proportion(value_tracker.get_value()))) 
        dot_P_label = always_redraw(lambda: Tex("P", color=WHITE, font_size=24)
                                    .next_to(dot_P, LEFT, buff=0.1))
        self.add(dot_P_label)      
        dot_Q.add_updater(lambda m: m.move_to(line_DC.point_from_proportion(value_tracker.get_value())))  
        dtot_Q_label = always_redraw(lambda: Tex("Q", color=WHITE, font_size=24)
                                    .next_to(dot_Q, UP, buff=0.1))  
        self.add(dtot_Q_label)
        
        line_PQ = always_redraw(lambda: Line(dot_P.get_center(), dot_Q.get_center(),
                                             color=GREEN, stroke_width=4))
        self.add(line_PQ) 
        
        # 线段PQ的中点M
        dot_M = always_redraw(lambda: Dot(color=YELLOW).move_to(line_PQ.get_center())) 
        dot_M_label = always_redraw(lambda: Tex("M", color=WHITE, font_size=24)
                                    .next_to(dot_M, DOWN, buff=0.1))
        line_BM = always_redraw(lambda: Line(rectangle.get_corner(DR), 
                                             dot_M.get_center(), color=YELLOW, stroke_width=4))
        self.add(dot_M, dot_M_label, line_BM)
        self.play(value_tracker.animate.set_value(0.8), run_time=5, rate_func=linear) 
        self.play(value_tracker.animate.set_value(0.2), run_time=5, rate_func=linear)      

        

        self.wait(3)
        


# manim -p 等长正方形.py MathSymbolsScene
