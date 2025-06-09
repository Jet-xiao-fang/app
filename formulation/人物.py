from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImageScene(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 标题设计
        img_files = [
            r"D:\Videos\图片素材\欧拉.jpeg",
            r"D:\Videos\图片素材\高斯.jpeg",
            r"D:\Videos\图片素材\bb.jpg",
            r"D:\Videos\图片素材\拉马.jpeg",
        ]
        y_positions = [3, 1, -1, -3]
        
        for i, file in enumerate(img_files):
            img = ImageMobject(file)
           
            if i == 2:
                img.scale(0.6)
            else:
                img.scale(0.3)
               
            img.move_to(y_positions[i] * UP + 2 * LEFT)
            
            if i == 0:
                text_group = VGroup(
                    Text(f"欧拉公式 (Basel问题)", font_size=20, color=RED_C),
                    MathTex(r"\frac{\pi^2}{6} = \sum_{n=1}^{\infty} \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \frac{1}{25} + \cdots", font_size=20, color=RED_C)
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            elif i == 1:
                text_group = VGroup(
                    Text(f"高斯-勒让德积分公式", font_size=20, color=BLUE),
                    MathTex(r"\pi = \left( \int_{-\infty}^{\infty} e^{-x^2} \, dx \right)^2", font_size=20, color=BLUE)
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            elif i == 2:
                text_group = VGroup(
                    Tex(r"莱布尼茨$\pi$公式", font_size=20, color=YELLOW),
                    MathTex(r"\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots", font_size=20, color=YELLOW)
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            else:
                text_group = VGroup(
                    Text(f"拉马努金公式", font_size=20, color=PINK),
                    MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)!(1103 + 26390k)}{(k!)^4 396^{4k}}", font_size=20, color=PINK)
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            
            text_group.next_to(img, RIGHT, buff=0.3)
            
            self.wait(1.0)
            
            # 同时显示图片和文字
            self.play(
                FadeIn(img),
                FadeIn(text_group),
                run_time=1.2
            )
            self.wait(1.0)
            
        self.wait(3)
# manim -pqh --format=png 人物.py ImageScene -r 1920,1080
