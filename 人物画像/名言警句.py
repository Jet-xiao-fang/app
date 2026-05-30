from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class CompleteBackgroundExample(Scene):
    def construct(self):
        background = ImageMobject(r"D:\Videos\图片素材\星空背景图.jpg")
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        background.set_opacity(0.7)
        self.add(background)

        overlay = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            color=BLACK,
            fill_opacity=0.5,
            stroke_opacity=0
        )
        self.add(overlay)

        items = [
            {
                "image": r"D:\Videos\图片素材\阿贝尔.jpg",
                "name": "尼尔斯·阿贝尔",
                "formula": r"v = v_0 + at",
                "color": YELLOW,
                "image_scale": 0.6
            },
            {
                "image": r"D:\Videos\图片素材\伽罗瓦.png",
                "name": "伽罗瓦",
                "formula": r"f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0",
                "color": GREEN,
                "image_scale": 0.6
            },
            {
                "image": r"D:\Videos\图片素材\拉马.jpeg",
                "name": "拉马努金",
                "formula": r"\sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}",
                "color": PINK,
                "image_scale": 0.6
            }
        ]

        # 第一位
        info = items[0]
        img = ImageMobject(info["image"]).scale(info["image_scale"])
        name = Text(info["name"], font="STXingkai", font_size=44, color=info["color"])
        formula = MathTex(info["formula"], color=info["color"]).scale(0.6)

        name.next_to(img, UP, buff=0.35)
        formula.next_to(img, DOWN, buff=0.35)
        Group(img, name, formula).move_to(ORIGIN)

        self.play(
            FadeIn(img, shift=DOWN * 0.3),
            Write(name),
            FadeIn(formula, shift=UP * 0.3),
            run_time=1.5
        )
        self.wait(2)

        # 依次转换后续人物
        for i in range(1, len(items)):
            old_img = img
            old_name = name
            old_formula = formula

            info = items[i]
            img = ImageMobject(info["image"]).scale(info["image_scale"])
            name = Text(info["name"], font="STXingkai", font_size=44, color=info["color"])
            formula = MathTex(info["formula"], color=info["color"]).scale(0.6)

            name.next_to(img, UP, buff=0.35)
            formula.next_to(img, DOWN, buff=0.35)
            Group(img, name, formula).move_to(ORIGIN)

            self.play(
                FadeOut(old_img),
                FadeIn(img),
                ReplacementTransform(old_name, name),
                ReplacementTransform(old_formula, formula),
                run_time=1.2
            )
            self.wait(2)

        self.wait(3)

# 运行命令: manim -pqh 名言警句.py CompleteBackgroundExample
