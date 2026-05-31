from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080
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
                "image": r"D:\Videos\图片素材\普朗克.png",
                "name": "普朗克",
                "formula": r"E = h\nu",
                "description": "能量量子化假说",
                "color": BLUE,
                "image_scale": 0.6
            },
            {
                "image": r"D:\Videos\图片素材\波尔.jpeg",
                "name": "玻尔",
                "formula": r"E_n = -\frac{13.6\,\text{eV}}{n^2}",
                "description": "玻尔原子模型",
                "color": YELLOW,
                "image_scale": 0.7
            },
            {
                "image": r"D:\Videos\图片素材\爱因斯坦.jpeg",
                "name": "爱因斯坦",
                "formula": r"E = mc^2",
                "description": "质能等价原理",
                "color": GREEN,
                "image_scale": 1.1
            },
            {
                "image": r"D:\Videos\图片素材\薛定谔.jpg",
                "name": "薛定谔",
                "formula": r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi",
                "description": "薛定谔波动方程",
                "color": PINK,
                "image_scale": 0.6
            },
            {
                "image": r"D:\Videos\图片素材\海森堡2.jpg",
                "name": "海森堡",
                "formula": r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                "description": "不确定性原理",
                "color": BLUE,
                "image_scale": 0.7
            },
            {
                "image": r"D:\Videos\图片素材\狄拉克.jpeg",
                "name": "狄拉克",
                "formula": r"(i\gamma^\mu\partial_\mu - m)\psi = 0",
                "description": "狄拉克相对论量子方程",
                "color": PURPLE,
                "image_scale": 0.7
            },
        ]

        # 第一位
        info = items[0]
        img = ImageMobject(info["image"]).scale(info["image_scale"])
        name = Text(info["name"], font="STXingkai", font_size=54, color=info["color"])
        formula = MathTex(info["formula"], color=WHITE)
        description = Text(info["description"], font_size=30, color=TEAL)  # 添加描述文本

        name.next_to(img, UP, buff=0.35)
        formula.next_to(img, DOWN, buff=0.35)
        description.next_to(formula, DOWN, buff=0.25)  # 描述放在公式下方
        Group(img, name, formula, description).move_to(ORIGIN).shift(UP * 0.2)  # 整体稍微上移一些

        self.play(
            FadeIn(img, shift=DOWN * 0.3),
            Write(name),
            FadeIn(formula, shift=UP * 0.3),
            Write(description),
            run_time=1
        )
        self.wait(0.5)

        # 依次转换后续人物
        for i in range(1, len(items)):
            old_img = img
            old_name = name
            old_formula = formula
            old_description = description

            info = items[i]
            img = ImageMobject(info["image"]).scale(info["image_scale"])
            name = Text(info["name"], font="STXingkai", font_size=54, color=info["color"])
            formula = MathTex(info["formula"], color=WHITE)
            description = Text(info["description"], font_size=30, color=TEAL)

            name.next_to(img, UP, buff=0.35)
            formula.next_to(img, DOWN, buff=0.35)
            description.next_to(formula, DOWN, buff=0.25)
            Group(img, name, formula, description).move_to(ORIGIN).shift(UP * 0.2)

            self.play(
                FadeOut(old_img),
                FadeIn(img),
                ReplacementTransform(old_name, name),
                ReplacementTransform(old_formula, formula),
                ReplacementTransform(old_description, description),
                run_time=1.2
            )
            self.wait(1)

# 运行命令: manim -pqh 名言警句.py CompleteBackgroundExample
