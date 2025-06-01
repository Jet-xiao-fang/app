from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class ParabolaPlot(Scene):
    def construct(self):
    
        self.camera.background_color = "#263238"
        
        # 坐标系
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-4, 4, 1],
            x_length=16,
            y_length=8,
            axis_config={"color": "#ECEFF1", "stroke_width": 2},
            tips=False,
        ).set_aspect_ratio(1.0)
        
        grid = NumberPlane(
            x_range=[-8, 8, 0.5],
            y_range=[-4, 4, 0.5],
            x_length=16,
            y_length=8,
            background_line_style={
                "stroke_color": "#546E7A",
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={"color": "#ECEFF1"},
        )
        
        axis_labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))
        origin_point = axes.c2p(0, 0)
        origin_dot = Dot(point=origin_point).scale(0.8)
        origin_label = Tex("O").next_to(origin_dot, DR, buff=0.1)

        self.add(axes,grid,axis_labels,origin_dot,origin_label);

        # 设置场景标题
        title = Text("向量操作演示", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.7).to_edge(UP))
        self.wait(0.5)

        # 定义向量
        vector_a = Vector([1.5,1],color=RED_C)
        vector_b = Vector([0.5,1.5],color=RED_C)
        
        # 向量标签
        a_label = MathTex("\\vec{a}", color=RED).next_to(vector_a.get_end(), UP)
        b_label = MathTex("\\vec{b}", color=GREEN).next_to(vector_b.get_end(), RIGHT)
        
        # 显示向量
        self.play(GrowArrow(vector_a), Write(a_label))
        self.wait(0.5)
        self.play(GrowArrow(vector_b), Write(b_label))
        self.wait(0.5)
        self.wait(1)
        # 向量加法
        add_title = Text("向量加法: a + b", font_size=36, color=YELLOW).to_edge(UP)
        self.play(ReplacementTransform(title, add_title))
        self.wait(0.5)

        # 创建向量b的副本并移动到向量a的末端
        vector_b_copy = vector_b.copy()
        b_copy_label = MathTex("\\vec{b}", color=GREEN).next_to(vector_b_copy.get_end(), RIGHT)
        
        # 动画显示向量加法
        self.play(vector_b_copy.animate.shift(vector_a.get_end()))
        self.play(Write(b_copy_label))

         # 创建和向量
        result_vector = Vector(vector_a.get_end() + vector_b.get_end() - ORIGIN, color=YELLOW_C)
        result_label = MathTex("\\vec{a} + \\vec{b}", color=YELLOW_C).next_to(result_vector.get_end(), LEFT)
        
        self.play(GrowArrow(result_vector), Write(result_label))
        self.wait(2)

                # 清理加法场景
        self.play(
            FadeOut(vector_b_copy),
            FadeOut(b_copy_label),
            FadeOut(result_vector),
            FadeOut(result_label)
        )
        # 向量减法
        sub_title = Text("向量减法: a - b", font_size=36, color=YELLOW).to_edge(UP)
        self.play(ReplacementTransform(add_title, sub_title))
        self.wait(0.5)
        
        # 创建负向量
        neg_vector_b = Vector(-vector_b.get_end(), color=GREEN)
        neg_b_label = MathTex("-\\vec{b}", color=GREEN).next_to(neg_vector_b.get_end(), LEFT)
        
        self.play(GrowArrow(neg_vector_b), Write(neg_b_label))
        self.wait(1)
        # 移动负向量到向量a的末端
        neg_vector_b_copy = neg_vector_b.copy()
        neg_b_copy_label = MathTex("-\\vec{b}", color=GREEN).next_to(neg_vector_b_copy.get_end(), LEFT)
        
        self.play(neg_vector_b_copy.animate.shift(vector_a.get_end()))
        self.play(Write(neg_b_copy_label))
        
        # 创建差向量
        diff_vector = Vector(vector_a.get_end() - vector_b.get_end(), color=YELLOW)
        diff_label = MathTex("\\vec{a} - \\vec{b}", color=YELLOW).next_to(diff_vector.get_end(), RIGHT)
        
        self.play(GrowArrow(diff_vector), Write(diff_label))
        self.wait(2)
        # 清理减法场景
        self.play(
            FadeOut(neg_vector_b),
            FadeOut(neg_vector_b_copy),
            FadeOut(neg_b_label),
            FadeOut(neg_b_copy_label),
            FadeOut(diff_vector),
            FadeOut(diff_label)
        )



# manim -pqh --format=png 向量.py ParabolaPlot -r 1920,1080


