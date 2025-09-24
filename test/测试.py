from manim import *

class AngleExampleV19(Scene):
    def construct(self):
        # 创建三角形顶点
        A = LEFT * 2 + DOWN
        B = RIGHT * 2 + DOWN
        C = UP * 1.5
        
        # 创建三角形
        triangle = Polygon(A, B, C, color=WHITE)
        
        # 创建角度标记 - 新API
        angle_A = Angle(Line(A, B), Line(A, C), radius=0.5)
        angle_B = Angle(Line(B, A), Line(B, C), radius=0.5)
        angle_C = Angle(Line(C, A), Line(C, B), radius=0.5)
        
        # 添加角度标签
        angle_label_A = MathTex("\\alpha").next_to(angle_A, DL, buff=0.1)
        angle_label_B = MathTex("\\beta").next_to(angle_B, DR, buff=0.1)
        angle_label_C = MathTex("\\gamma").next_to(angle_C, UP, buff=0.1)
        
        self.play(Create(triangle))
        self.play(
            Create(angle_A),
            Create(angle_B),
            Create(angle_C)
        )
        self.play(
            Write(angle_label_A),
            Write(angle_label_B),
            Write(angle_label_C)
        )
        self.wait(3)
        
#   manim -pqh 测试.py AngleExampleV19