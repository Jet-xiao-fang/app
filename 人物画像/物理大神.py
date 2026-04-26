from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080

class MathSymbolsScene(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        # 数学家图片和符号信息
        items = [
            {
                "name": "爱因斯坦",
                "image": r"D:\Videos\图片素材\爱因斯坦.jpeg",
                "symbols": [
                    (r"E = h\nu", "光量子假说 (1905)"), 
                    (r"E_k = h\nu - W", "光电效应方程 (1905)"),
                    (r"\Delta E = \Delta m c^2", "质能方程 (1905)")
                ],
                "color": YELLOW,
                "img_scale": 0.4
            },
            {
                "name": "薛定谔",
                "image": r"D:\Videos\图片素材\薛定谔.jpg",
                "symbols": [
                    (r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi", "含时薛定谔方程 (1926)"), 
                    (r"-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi", "定态薛定谔方程 (1926)"),
                    (r"P = |\Psi|^2", "波函数概率诠释 (1926)")
                ],
                "color": RED_C,
                "img_scale": 0.2
            },
            {
                "name": "海森堡",
                "image": r"D:\Videos\图片素材\海森堡2.jpg",
                "symbols": [
                    (r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", "不确定性原理 (1927)"), 
                    (r"\left[ \hat{Q}, \hat{P} \right] = i\hbar", "矩阵力学对易关系 (1925)"),
                    (r"E_n = \langle n|\hat{H}|n \rangle", "能量本征值矩阵表示 (1925)")
                ],
                "color": BLUE,
                "img_scale": 0.2
            },
            {
                "name": "狄拉克",
                "image": r"D:\Videos\图片素材\狄拉克.jpeg",
                "symbols": [
                    (r"(i\gamma^\mu\partial_\mu - m)\psi = 0", "狄拉克方程 (1928)"), 
                    (r"\langle \phi | \psi \rangle", "狄拉克符号（左矢右矢）(1939)"),
                    (r"E = \pm \sqrt{p^2c^2 + m^2c^4}", "反粒子解 (1928)")
                ],
                "color": PINK,
                "img_scale": 0.2
            }
        ]
        
        # 创建并展示每位数学家
        groups = Group()
        for i, info in enumerate(items):
            if i==0:
                img = ImageMobject(info["image"]).scale(info["img_scale"])
            elif i==1:
                img = ImageMobject(info["image"]).scale(info["img_scale"])
            else:
                img = ImageMobject(info["image"]).scale(info["img_scale"])
            # 创建名称文本
            name = Text(info["name"], font="STXingkai", font_size=36, color=info["color"])
            formula_items = VGroup()
            for formula_str, description in info["symbols"]:
                # 公式部分使用 MathTex
                formula = MathTex(formula_str, color=info["color"]).scale(0.6)
                # 说明文字使用 Text
                desc = Text(description, font="Microsoft YaHei", font_size=23, color=WHITE)
                # 将公式和说明水平排列
                item_group = VGroup(formula, desc).arrange(RIGHT, buff=0.3)
                formula_items.add(item_group)
            
            # 垂直排列所有公式项
            formula_items.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
             # 创建垂直组：名称 + 公式
             
            text_group = VGroup(name, formula_items)
            text_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.3)
            
            
            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)
        # 排列所有组
        groups.arrange(DOWN, buff=0.5).shift(UP*0.2)
        
        
        # 优雅的淡入效果，每个持续2秒，总时长约8-10秒
        self.play(
            LaggedStart(
                FadeIn(groups[0], shift=UP*0.5, run_time=1.8),
                FadeIn(groups[1], shift=UP*0.5, run_time=1.8),
                FadeIn(groups[2], shift=UP*0.5, run_time=1.8),
                FadeIn(groups[3], shift=UP*0.5, run_time=1.8),
                lag_ratio=1  # 40%的重叠，让动画更流畅
            )
        )

        self.wait(6)  # 最后等待2秒
        
        
        
# manim -p 物理大神.py MathSymbolsScene