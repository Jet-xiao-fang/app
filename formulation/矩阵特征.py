from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class EigenValueDemo(Scene):
    def construct(self):
        # 星空背景
        stars = VGroup(*[Dot(point=[np.random.uniform(-7,7), 
                                  np.random.uniform(-4,4),
                                  0], 
                          radius=np.random.uniform(0.01,0.03),
                          color=BLUE_E) for _ in range(200)])
        self.add(stars)
        
        # 标题设计
        title = Tex("矩阵的特征值与特征向量", font_size=36, color="#FFD700").to_edge(UP)

        self.add(title)
        
        # 特征值定义
        self.show_definition()
        self.clear_screen(stars, title)
        
        # 特征向量演示
        self.show_eigen_vector(stars, title)
        
    
    def clear_screen(self, stars, title):
        """清除当前场景（保留星空和标题）"""
        to_remove = [mob for mob in self.mobjects if mob not in [stars, title]]
        self.play(*[FadeOut(mob) for mob in to_remove])
    
    def show_definition(self):
        """展示特征值与特征向量的数学定义"""
        # 特征值定义公式
        definition = MathTex(
            r"A\vec{x} = \lambda\vec{x}",
            font_size=42,
            color=YELLOW
        )
        definition.shift(UP)
        
        # 解释文本
        explanation = VGroup(
            Tex(r"其中：", font_size=32),
            MathTex(r"A: \text{矩阵}", font_size=32),
            MathTex(r"\vec{x}: \text{特征向量} (\neq \vec{0})", font_size=32),
            MathTex(r"\lambda: \text{特征值}", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(definition, DOWN, buff=0.5)
        
        # 特征方程
        char_eq = MathTex(
            r"\det(A - \lambda I) = 0",
            font_size=42,
            color=GREEN
        ).next_to(explanation, DOWN, buff=0.8)
        
        # 动画展示
        self.play(Write(definition))
        self.wait()
        self.play(FadeIn(explanation, shift=UP))
        self.wait(2)
        self.play(Write(char_eq))
        self.wait(3)
    
    def show_eigen_vector(self, stars, title_group):
        """演示特征向量的变换特性"""
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
        
        # 创建矩阵（对称矩阵，确保实数特征值）
        matrix = np.array([[2, 0.5], [0.5, 2]])
        matrix_display = Matrix([[2, 0.5], [0.5, 2]]).set_color(YELLOW)
        matrix_display.to_corner(UP+RIGHT)
        self.play(Write(matrix_display))
        
        # 计算特征值和特征向量
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        
        # 特征向量（取实部）
        vec1 = Vector(eigenvectors[:, 0].real, color=GREEN)
        vec2 = Vector(eigenvectors[:, 1].real, color=RED)
        
        # 非特征向量
        non_eigen_vec = Vector([1, 0.5], color=PURPLE)
        
        # 添加标签
        vec1_label = MathTex(r"\vec{v_1}", color=GREEN).next_to(vec1.get_end(), UP)
        vec2_label = MathTex(r"\vec{v_2}", color=RED).next_to(vec2.get_end(), DOWN)
        non_vec_label = MathTex(r"\vec{u}", color=PURPLE).next_to(non_eigen_vec.get_end(), RIGHT)
        
        # 显示特征值
        lambda1 = MathTex(fr"\lambda_1 = {eigenvalues[0]:.2f}", color=GREEN).next_to(matrix_display, DOWN)
        lambda2 = MathTex(fr"\lambda_2 = {eigenvalues[1]:.2f}", color=RED).next_to(lambda1, DOWN)
        
        self.play(
            Create(vec1), Write(vec1_label),
            Create(vec2), Write(vec2_label),
            Create(non_eigen_vec), Write(non_vec_label),
            Write(lambda1), Write(lambda2)
        )
        self.wait(2)
        
        # 应用矩阵变换
        transform_matrix = np.array([
            [2, 0.5, 0],
            [0.5, 2, 0],
            [0, 0, 1]
        ])
        
        # 变换后的向量
        transformed_vec1 = Vector(matrix @ eigenvectors[:, 0].real, color=GREEN)
        transformed_vec2 = Vector(matrix @ eigenvectors[:, 1].real, color=RED)
        transformed_non_vec = Vector(matrix @ [1, 0.5], color=PURPLE)
        
        # 添加变换后的标签
        trans_vec1_label = MathTex(r"A\vec{v_1}", color=GREEN).next_to(transformed_vec1.get_end(), UP)
        trans_vec2_label = MathTex(r"A\vec{v_2}", color=RED).next_to(transformed_vec2.get_end(), DOWN)
        trans_non_label = MathTex(r"A\vec{u}", color=PURPLE).next_to(transformed_non_vec.get_end(), RIGHT)
        
        # 变换动画
        self.play(
            Transform(vec1, transformed_vec1),
            Transform(vec1_label, trans_vec1_label),
            Transform(vec2, transformed_vec2),
            Transform(vec2_label, trans_vec2_label),
            Transform(non_eigen_vec, transformed_non_vec),
            Transform(non_vec_label, trans_non_label)
        )
        self.wait(3)
        
        # 添加说明
        explanation = VGroup(
            Tex("特征向量在变换后方向不变", color=YELLOW, font_size=30),
            Tex("非特征向量在变换后方向改变", color=YELLOW, font_size=30)
        ).arrange(DOWN, buff=0.5).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # 显示特征值缩放关系
        scale_text1 = MathTex(
            fr"A\vec{{v_1}} = {eigenvalues[0]:.2f}\vec{{v_1}}", 
            color=GREEN
        ).next_to(explanation, UP, buff=0.5)
        
        scale_text2 = MathTex(
            fr"A\vec{{v_2}} = {eigenvalues[1]:.2f}\vec{{v_2}}", 
            color=RED
        ).next_to(scale_text1, UP, buff=0.3)
        
        self.play(Write(scale_text1), Write(scale_text2))
        self.wait(3)
    
        # 几何解释：特征向量构成新的坐标系
        plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-3, 3],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        # 特征向量作为新基
        vec1 = Vector(eigenvectors[:, 0].real, color=GREEN)
        vec2 = Vector(eigenvectors[:, 1].real, color=RED)
        
        # 创建新的坐标系
        new_plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-3, 3],
            background_line_style={
                "stroke_color": GREEN_C,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={"stroke_color": GREEN}
        )
        
        # 应用特征向量基的变换
        basis_matrix = np.vstack([eigenvectors[:, 0].real, eigenvectors[:, 1].real]).T
        new_plane.apply_matrix(basis_matrix)
        
        # 动画：从标准坐标系转换到特征向量坐标系
        self.play(Create(plane))
        self.play(Create(vec1), Create(vec2))
        self.wait(1)
        
        self.play(
            Transform(plane, new_plane),
            vec1.animate.scale(eigenvalues[0], about_point=ORIGIN),
            vec2.animate.scale(eigenvalues[1], about_point=ORIGIN)
        )
        self.wait(2)
        
        # 添加说明
        final_explanation = VGroup(
            Tex("特征分解：在特征向量构成的坐标系中，", font_size=30, color=YELLOW),
            Tex("矩阵变换简化为沿坐标轴的缩放", font_size=30, color=YELLOW)
        ).arrange(DOWN).to_edge(DOWN)
        
        self.play(Write(final_explanation))
        self.wait(3)

# manim -pqh 矩阵特征.py EigenValueDemo -r 1920,1080