from manim import *

config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class LawnWithPaths(Scene):
    def construct(self):
        # 设置背景为深空蓝
        self.camera.background_color = "#0F0F1A"
        
        # 草坪参数 (实际尺寸)
        length = 20      # 长
        width = 12       # 宽
        path_width = 2   # 小路宽

        # 缩放比例
        scale_factor = 0.3

        # 计算缩放后的视觉尺寸
        vis_len = length * scale_factor
        vis_wid = width * scale_factor
        vis_path = path_width * scale_factor

        # 1. 草坪
        lawn = Rectangle(
            width=vis_len,
            height=vis_wid,
            color=GREEN,
            fill_opacity=0.7,
            stroke_width=2
        )
        lawn.move_to(ORIGIN)

        # 2. 水平小路
        h_path = Rectangle(
            width=vis_len,
            height=vis_path,
            color=GRAY,
            fill_opacity=0.9,
            stroke_width=0
        )
        h_path.move_to(ORIGIN)

        # 3. 垂直小路
        v_path = Rectangle(
            width=vis_path,
            height=vis_wid,
            color=GRAY,
            fill_opacity=0.9,
            stroke_width=0
        )
        v_path.move_to(ORIGIN)

        # 尺寸标签（修正为20和12）
        len_label = Text("20 m", font_size=28, color=YELLOW)
        len_label.next_to(lawn, DOWN, buff=0.25)

        wid_label = Text("12 m", font_size=28, color=YELLOW)
        wid_label.next_to(lawn, LEFT, buff=0.25)

        h_label = Text("2 m", font_size=22, color=WHITE)
        h_label.move_to(h_path.get_center())

        v_label = Text("2 m", font_size=22, color=WHITE)
        v_label.move_to(v_path.get_center())

        # 创建题目（修正公式）
        question_text = VGroup(
            MathTex( r"\text{长方形的草坪中有两条宽为 } 2\text{ 米的小路，}", font_size=42),
            MathTex(r"\text{求剩余草坪的面积？}", font_size=42)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        question_text.next_to(lawn, UP, buff=0.5)

        # 动画开始
        self.add(question_text)  # ✅ 修正
        self.play(Create(lawn))
        self.wait(0.5)

        # 同时出现两条小路
        self.play(
            FadeIn(h_path, scale=0.5),
            FadeIn(v_path, scale=0.5),
            lag_ratio=0
        )
        self.wait(0.3)

        # 显示所有尺寸标签
        self.play(
            Write(len_label),
            Write(wid_label),
            Write(h_label),
            Write(v_label)
        )
        self.wait(1)

        # 高亮交叉区域
        cross = Square(
            side_length=vis_path,
            color=RED,
            fill_opacity=0.4,
            stroke_width=0
        )
        cross.move_to(ORIGIN)
        self.play(FadeIn(cross, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(cross, run_time=0.5))

        self.wait(5)