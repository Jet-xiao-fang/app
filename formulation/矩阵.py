from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MatrixProperties(Scene):
    def construct(self):
        # 星空背景
        stars = VGroup(*[Dot(point=[np.random.uniform(-7,7), 
                                  np.random.uniform(-4,4),
                                  0], 
                          radius=np.random.uniform(0.01,0.03),
                          color=BLUE_E) for _ in range(200)])
        self.add(stars)
        
        # 标题设计
        title = Tex("矩阵的重要性质", font_size=36, color="#FFD700")
        title_box = SurroundingRectangle(title, color=WHITE, buff=0.3, corner_radius=0.2)
        title_group = VGroup(title_box, title)
        title_group.to_edge(UP)
        self.add(title_group)

        # 1. 矩阵乘法结合律演示
        self.show_associative_property(stars, title_group)
        
        # 2. 矩阵乘法分配律演示
        self.show_distributive_property(stars, title_group)
        
        # 3. 行列式的几何意义
        self.show_determinant_meaning(stars, title_group)

    def show_associative_property(self, stars, title_group):
                # 简化版结合律演示
        # 创建三个小矩阵
        A = Matrix([[1, 2], [3, 4]]).set_color(BLUE).scale(0.8)
        B = Matrix([[2, 0], [1, 2]]).set_color(GREEN).scale(0.8)
        C = Matrix([[1, 1], [0, 1]]).set_color(YELLOW).scale(0.8)
        
        # 设置位置
        matrices = VGroup(A, B, C).arrange(RIGHT, buff=0.5).shift(UP)
        times1 = MathTex("\\times").next_to(A, RIGHT)
        times2 = MathTex("\\times").next_to(B, RIGHT)
        
        # 创建表达式组
        left_expr = MathTex("(AB)C").scale(1.2).shift(LEFT*3 + UP)
        right_expr = MathTex("A(BC)").scale(1.2).shift(RIGHT*3 + UP)
        equals = MathTex("=").scale(1.2).shift(UP)
        
        # 计算结果
        result = Matrix([[5, 4], [13, 10]]).set_color(PURPLE).scale(0.9)
        result.next_to(equals, DOWN*3)
        
        # 动画展示
        self.play(FadeIn(matrices), Write(times1), Write(times2))
        self.wait()
        
        # 展示表达式
        self.play(
            TransformFromCopy(VGroup(A, B), left_expr),
            TransformFromCopy(VGroup(B, C), right_expr),
            Write(equals)
        )
        self.wait()
        
        # 展示结果
        self.play(Write(result))
        self.wait()
        
        # 添加说明文本
        explanation = Tex("结合律: $(AB)C = A(BC)$", font_size=32, color=YELLOW)
        explanation.next_to(result, DOWN)
        self.play(Write(explanation))
        self.wait(2)
        
        # 清除当前场景（保留星空和标题）
        to_remove = [mob for mob in self.mobjects if mob not in [stars, title_group]]
        self.play(*[FadeOut(mob) for mob in to_remove])

    def show_distributive_property(self, stars, title_group):
                # 简化版分配律演示
        # 创建矩阵
        A = Matrix([[2, 0], [1, 3]]).set_color(BLUE).scale(0.8)
        B = Matrix([[1, 1], [0, 2]]).set_color(GREEN).scale(0.8)
        C = Matrix([[0, 2], [1, 0]]).set_color(YELLOW).scale(0.8)
        
        # 设置位置
        group = VGroup(A, B, C).arrange(RIGHT, buff=0.5).shift(UP)
        plus = MathTex("+").next_to(B, RIGHT)
        times = MathTex("\\times").next_to(A, RIGHT)
        
        # 创建表达式组
        left_expr = MathTex("A(B+C)").scale(1.2).shift(LEFT*3 + UP)
        right_expr = MathTex("AB + AC").scale(1.2).shift(RIGHT*3 + UP)
        equals = MathTex("=").scale(1.2).shift(UP)
        
        # 计算结果
        result = Matrix([[2, 4], [3, 7]]).set_color(PURPLE).scale(0.9)
        result.next_to(equals, DOWN*3)
        
        # 动画展示
        self.play(FadeIn(group), Write(plus), Write(times))
        self.wait()
        
        # 展示表达式
        self.play(
            TransformFromCopy(VGroup(A, B, C), left_expr),
            TransformFromCopy(VGroup(A, B, C), right_expr),
            Write(equals)
        )
        self.wait()
        
        # 展示结果
        self.play(Write(result))
        self.wait()
        
        # 添加说明文本
        explanation = Tex("分配律: $A(B+C) = AB + AC$", font_size=32, color=YELLOW)
        explanation.next_to(result, DOWN)
        self.play(Write(explanation))
        self.wait(2)
        
        # 清除当前场景（保留星空和标题）
        to_remove = [mob for mob in self.mobjects if mob not in [stars, title_group]]
        self.play(*[FadeOut(mob) for mob in to_remove])

    def show_determinant_meaning(self, stars, title_group):
        # 创建坐标系
        plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-3, 3],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        self.play(Create(plane))
        
        # 创建单位正方形 - 明确指定为2D点（z=0）
        square = Polygon([0,0,0], [1,0,0], [1,1,0], [0,1,0], color=GREEN, fill_opacity=0.5)
        self.play(Create(square))
        
        # 添加标签
        area_text = MathTex("\\text{面积} = 1", font_size=32).next_to(square, RIGHT)
        self.play(Write(area_text))
        self.wait()
        
        # 创建变换矩阵
        matrix_2d = np.array([[2, 0.5], [0.5, 2]])
        det_value = np.linalg.det(matrix_2d)
        
        # 在场景中显示的矩阵
        display_matrix = Matrix([[2, 0.5], [0.5, 2]]).set_color(YELLOW)
        display_matrix.to_corner(UP+RIGHT)
        det_text = MathTex(f"\\det = {det_value:.2f}", font_size=32).next_to(display_matrix, DOWN)
        self.play(Write(display_matrix), Write(det_text))
        self.wait()
        
        # 应用线性变换 - 创建3x3变换矩阵
        transform_matrix = np.array([
            [2, 0.5, 0],  # x' = 2x + 0.5y + 0z
            [0.5, 2, 0],  # y' = 0.5x + 2y + 0z
            [0, 0, 1]     # z' = 0x + 0y + 1z
        ])
        
        transformed_square = square.copy()
        
        # 计算变换后的面积
        new_area_text = MathTex(fr"\text{{面积}} = {det_value:.2f}", font_size=32)
        
        # 应用变换动画
        self.play(
            transformed_square.animate.apply_matrix(transform_matrix),
            area_text.animate.become(new_area_text).move_to(transformed_square.get_center() + RIGHT)
        )
        self.wait(2)
        
        # 添加说明
        explanation = Tex("行列式表示线性变换的面积缩放因子", font_size=32, color=YELLOW)
        explanation.next_to(transformed_square, DOWN*2)
        self.play(Write(explanation))
        self.wait(2)

# manim -pqh 矩阵.py MatrixProperties -r 1920,1080