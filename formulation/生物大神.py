from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class BiologyPioneersScene(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        items = [
            {
                "name": "孟德尔",
                "image": r"D:\Videos\图片素材\孟德尔.jpeg",
                "contributions": [
                    r"分离定律-F₂代性状分离比 3:1",
                    r"自由组合定律-两对性状独立遗传",
                    r"遗传因子假说-显性与隐性遗传因子",
                ],
                "color": GREEN,   # 确保 GREEN 已定义
                "img_scale": 0.4,
            },
            {
                "name": "达尔文",
                "image": r"D:\Videos\图片素材\达尔文.jpeg",
                "contributions": [
                    r"自然选择学说-适者生存，不适者淘汰",
                    r"共同由来学说-所有生物有共同祖先",
                    r"《物种起源》-1859年出版"
                ],
                "color": ORANGE,
                "img_scale": 0.3,
            },
            {
                "name": "沃森与克里克",
                "image": r"D:\Videos\图片素材\沃森.jpg",
                "contributions": [
                    r"DNA双螺旋结构-1953年提出",
                    r"碱基互补配对-A-T, G-C配对原则",
                    r"备受争论-关于黑人智商问题",
                ],
                "color": BLUE,
                "img_scale": 0.3,
            }
        ]

        all_groups = Group()  # 改用 Group
        for i, info in enumerate(items):
            if i==0:
                img = ImageMobject(info["image"]).scale(info["img_scale"])
            elif i==1:
                img = ImageMobject(info["image"]).scale(info["img_scale"])
            else:
                img = ImageMobject(info["image"]).scale(info["img_scale"])
            # 创建名称文本
            name = Text(info["name"], font="STXingkai", font_size=26, color=info["color"])
            formula1 = Tex(info["contributions"][0], color=info["color"]).scale(0.55)
            formula2 = Tex(info["contributions"][1], color=info["color"]).scale(0.55)
            formula3 = Tex(info["contributions"][2], color=info["color"]).scale(0.55)
             # 创建垂直组：名称 + 公式
            text_group = VGroup(name, formula1, formula2,formula3)
            text_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.2)
            
            
            # 将图片和文本组组合
            group = Group(img, text_group)
            all_groups.add(group)
        # 排列所有组
        all_groups.arrange(DOWN, buff=0.5).shift(UP*0.2)   
        
        self.play(LaggedStart(
            FadeIn(all_groups[0], shift=UP*0.5),
            FadeIn(all_groups[1], shift=UP*0.5),
            FadeIn(all_groups[2], shift=UP*0.5),
            lag_ratio=1.0
        ))

        final_text = Text("生命科学：揭示自然奥秘",
                          font="Microsoft YaHei", font_size=36, color=GOLD)
        final_text.to_edge(DOWN, buff=0.8)
        self.play(Write(final_text))
        self.wait(3)
        
# manim -p 生物大神.py BiologyPioneersScene