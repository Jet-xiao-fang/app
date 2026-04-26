from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080
class ImageScene(Scene):
    def construct(self):
        # 设置封面
        self.camera.background_color = "#0F0F1A"
        items = [
            {
                "name": f"欧拉公式 (Basel问题)",
                "image": r"D:\Videos\图片素材\欧拉1.jpg",
                "symbols": r"\frac{\pi^2}{6} = \sum_{n=1}^{\infty} \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \frac{1}{25} + \cdots",
                "color": YELLOW,
                "img_scale": 0.25
            },
            {
                "name": f"高斯-勒让德积分公式",
                "image": r"D:\Videos\图片素材\高斯.jpeg",
                "symbols": r"\pi = \left( \int_{-\infty}^{\infty} e^{-x^2} \, dx \right)^2",
                "color": RED,
                "img_scale": 0.28
            },
            {
                "name": r"莱布尼茨$\pi$公式",
                "image": r"D:\Videos\图片素材\莱布尼茨.jpg",
                "symbols": r"\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots",
                "color": BLUE,
                "img_scale": 0.5
            },
            {
                "name": f"拉马努金公式",
                "image": r"D:\Videos\图片素材\拉马.jpeg",
                "symbols": r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)!(1103 + 26390k)}{(k!)^4 396^{4k}}",
                "color": PINK,
                "img_scale": 0.3
            }
        ]
        groups = Group()
        for i, info in enumerate(items):
            
            img = ImageMobject(info["image"]).scale(info["img_scale"])

            # 创建名称
            describe = Tex(info["name"], font_size=30, color=info["color"])
            formulation = MathTex(
                        info["symbols"],
                        font_size=30,
                        color=info["color"],
                    )
            text_group = VGroup(describe,formulation).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(img, RIGHT, buff=0.2)

            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)
        groups.arrange(DOWN, buff=0.3,aligned_edge=LEFT)
        self.play(LaggedStart(
            FadeIn(groups[0], shift=UP*0.5,scale=0.8,run_time=1.8),
            FadeIn(groups[1], shift=UP*0.5,scale=0.8,run_time=1.8),
            FadeIn(groups[2], shift=UP*0.5,scale=0.8,run_time=1.8),
            FadeIn(groups[3], shift=UP*0.5,scale=0.8,run_time=1.8),
            lag_ratio=1.0
        ))
        final_text = Text("π是一个超越数！", font="Microsoft YaHei", font_size=36, color=RED)
        self.play(Write(final_text.to_edge(DOWN, buff=0.5)))
        self.wait(5)
    

# manim -p 人物.py ImageScene
