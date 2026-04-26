from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
class ImageScene(Scene):
    def construct(self):
        # 设置封面
        self.camera.background_color = "#0F0F1A"
        # 标题设计
        img_files = [
            r"D:\Videos\图片素材\欧拉.jpeg",
            r"D:\Videos\图片素材\高斯.jpeg",
            r"D:\Videos\图片素材\莱布尼茨.jpg",
            r"D:\Videos\图片素材\拉马.jpeg",
        ]
        y_positions = [4, 1, -2, -5]
        groups = Group()
        for i, file in enumerate(img_files):
            img = ImageMobject(file)

            if i == 2:
                img.scale(0.5)
            else:
                img.scale(0.2)

            img.move_to(y_positions[i] * UP + 3.5 * LEFT)
            titile = Text("拉马努金厉害啊", font="Microsoft YaHei", font_size=36, color=BLUE)
            self.add(titile.to_edge(UP, buff=1.5))
            if i == 0:
                text_group = VGroup(
                    Text(f"欧拉公式 (Basel问题)", font_size=30, color=RED_C),
                    MathTex(
                        r"\frac{\pi^2}{6} = \sum_{n=1}^{\infty} \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \frac{1}{25} + \cdots",
                        font_size=30,
                        color=RED_C,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            elif i == 1:
                text_group = VGroup(
                    Text(f"高斯-勒让德积分公式", font_size=30, color=BLUE),
                    MathTex(
                        r"\pi = \left( \int_{-\infty}^{\infty} e^{-x^2} \, dx \right)^2",
                        font_size=30,
                        color=BLUE,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            elif i == 2:
                text_group = VGroup(
                    Tex(r"莱布尼茨$\pi$公式", font_size=30, color=YELLOW),
                    MathTex(
                        r"\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots",
                        font_size=30,
                        color=YELLOW,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            else:
                text_group = VGroup(
                    Text(f"拉马努金公式", font_size=30, color=PINK),
                    MathTex(
                        r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)!(1103 + 26390k)}{(k!)^4 396^{4k}}",
                        font_size=35,
                        color=PINK,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

            text_group.next_to(img, RIGHT, buff=0.3)
            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)

            # 同时显示图片和文字,我可以更好的控制每一个元素
            self.play(LaggedStart(FadeIn(group, shift=UP * 0.5,scale=0.8), lag_ratio=1.0))
            
            self.wait(1.0)
        final_text = Text("π是一个超越数！", font="Microsoft YaHei", font_size=36, color=RED)
        self.play(Write(final_text.to_edge(DOWN, buff=0.5)))
        self.wait(5)
    

# manim -p 人物.py ImageScene
