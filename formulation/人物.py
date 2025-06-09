from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1080
config.pixel_width = 608
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex


class ImageScene(Scene):
    def construct(self):
        self.camera.background_color = "#0F0B1A"
        # 标题设计
        title = Tex("你心目中的第一是谁？", font_size=46, color="#FFD700").to_edge(UP,buff=0.5)
        self.add(title)
        global text_group
        color = WHITE
        img_files = [
            r"D:\Videos\图片素材\a.jpg",
            r"D:\Videos\图片素材\b.jpg",
            r"D:\Videos\图片素材\c.jpg",
        ]
        y_positions = [4, 0, -4]
        for i, file in enumerate(img_files):
            img = ImageMobject(file)
            img.scale(0.8)
            if i == 1:
                img.scale(0.5)
            
            img.move_to(y_positions[i] * UP + 2 * LEFT)
            self.play(FadeIn(img), run_time=0.8)
            if i == 0:
                text_group = VGroup(
                    Text(f"1.提出运动三定律和万有引力定律", font_size=20, color=color),
                    Text(f"2.发明微积分和揭示光的色散性质", font_size=20, color=color),
                    Text(f"3.确立实验+数学推导的科学范式", font_size=20, color=color),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            if i == 1:
                text_group = VGroup(
                    Text(f"1.用四个方程统一电、磁、光现象", font_size=20, color=BLUE),
                    Text(f"2.理论直接引导无线电、通信学发展", font_size=20, color=BLUE),
                    Text(f"3.方程组隐含光速不变性", font_size=20, color=BLUE),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            if i == 2:
                text_group = VGroup(
                    Text(f"1.光电效应理论证实光的粒子性", font_size=20, color=YELLOW),
                    Text(f" 推动量子力学诞生", font_size=20, color=YELLOW),
                    Text(f"2.狭义相对论否定绝对时空", font_size=20, color=YELLOW),
                    Text(f"3.广义相对论将引力解释为时空弯曲", font_size=20, color=YELLOW),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            text_group.next_to(img, RIGHT, buff=0.3)
            self.play(Write(text_group), run_time=1.5)
            self.wait(1.0)
        self.wait(3)
# manim -pqh --format=png 人物.py ImageScene -r 1920,1080
