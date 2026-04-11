from manim import *

class PythagoreanProof(Scene):
    def construct(self):
        # 1. 标题
        title = Tex("Pythagorean Theorem").to_edge(UP)
        formula = MathTex("a^2", "+", "b^2", "=", "c^2").next_to(title, DOWN)
        self.play(Write(title), Write(formula))
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(formula))

        # 2. 画三角形 (简化示例：硬编码一个3-4-5比例三角形)
        # 为了让代码直观，这里假设 A 在原点
        A = np.array([-2, -1, 0])
        B = np.array([ 1, -1, 0])
        C = np.array([-2,  1, 0])
        
        triangle = Polygon(A, B, C, color=WHITE)
        right_angle = RightAngle(Line(A, C), Line(A, B), length=0.3) # 需要 from manim import RightAngle
        
        # 标注 a, b, c
        a_label = MathTex("a").next_to(Line(A, B).get_center(), DOWN)
        b_label = MathTex("b").next_to(Line(A, C).get_center(), LEFT)
        c_label = MathTex("c").next_to(Line(B, C).get_center(), UR)
        
        self.play(Create(triangle), Create(right_angle), Write(a_label), Write(b_label), Write(c_label))
        self.wait()

        # 3. 构建正方形 (这里需要根据实际几何计算，逻辑较复杂，仅示意)
        # 边 a 的正方形
        square_a = Square(side_length=abs(B[0]-A[0])).move_to(Line(A, B).get_center() + DOWN * 0.5)
        square_a.set_fill(BLUE, opacity=0.3)
        
        self.play(Create(square_a))
        self.wait(2)
        
# manim -pqh 图文作品.py PythagoreanProof