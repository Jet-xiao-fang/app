from manim import *
import os

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MultiImage(Scene):
    def construct(self):
        self.showImage()
        self.wait(0.5)
        self.clear_scene()
        self.showDescribe()

    def showImage(self):
        self.camera.background_color = "#0F0B1A"

        items = [
            {
                "image": r"D:\Videos\图片素材\阿贝尔.jpg",
                "name": "尼尔斯·阿贝尔 (1802-1829)",
                "symbols": [
                    "证明五次方程无一般代数解（1824），终结了数学界250年的猜想",
                    "开创椭圆函数论，为复变函数奠基"
                ],
                "color": YELLOW,
                "image_scale": 0.3
            },
            {
                "image": r"D:\Videos\图片素材\伽罗瓦.png",
                "name": "埃瓦里斯特·伽罗瓦 (1811-1832)",
                "symbols": [
                    "创立伽罗瓦理论，用群论解决代数方程根式可解性问题",
                    "奠定近世代数基础"
                ],
                "color": GREEN,
                "image_scale": 0.3
            },
            {
                "image": r"D:\Videos\图片素材\拉马.jpeg",
                "name": "斯里尼瓦瑟·拉马努金 (1887-1920)",
                "symbols": [
                    "自学成才，留下3900个公式，涉及数论、模形式等",
                    "直觉推导能力惊人，公式被应用于黑洞熵研究"
                ],
                "color": PINK,
                "image_scale": 0.3
            }
        ]

        groups = Group()
        for info in items:
            # 检查图片是否存在
            if not os.path.exists(info["image"]):
                print(f"警告: 图片不存在 - {info['image']}")
                continue
                
            img = ImageMobject(info["image"]).scale(info["image_scale"])
            name = Text(info["name"], font="Microsoft YaHei", font_size=26, color=info["color"])

            formula1 = Text(info["symbols"][0], font_size=18, color=info["color"])
            formula2 = Text(info["symbols"][1], font_size=18, color=info["color"])

            text_group = VGroup(name, formula1, formula2)
            text_group.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            text_group.next_to(img, RIGHT, buff=0.3)

            # 使用 Group 来混合 ImageMobject 和 VGroup
            group = Group(img, text_group)
            groups.add(group)

        groups.arrange(DOWN, buff=0.5,aligned_edge=LEFT)
         # 动画展示
        self.play(LaggedStart(
            FadeIn(groups[0], shift=UP*0.5,scale=0.9),
            FadeIn(groups[1], shift=UP*0.5,scale=0.9),
            FadeIn(groups[2], shift=UP*0.5,scale=0.9),
            lag_ratio=1.0
        ))
        self.wait(3)

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

    def showDescribe(self):
        title = Text("英年早逝的数学家",
                    font="Microsoft YaHei",
                    font_size=36,
                    color=WHITE)
        title.to_edge(UP, buff=1)

        underline = Line(LEFT, RIGHT, color=BLUE).scale(1.1)
        underline.next_to(title, DOWN, buff=0.1)

        # 人物资料
        mathematicians = [
            {
                "name": "尼尔斯·阿贝尔",
                "color": YELLOW,
                "details": [
                    "• 出身贫困，18岁负担全家生计",
                    "• 论文被柯西遗失、勒让德拒评",
                    "• 1829年贫病中去世",
                    "• 去世两天后聘书送达"
                ]
            },
            {
                "name": "埃瓦里斯特·伽罗瓦",
                "color": GREEN,
                "details": [
                    "• 论文两次被退回",
                    "• 投身共和运动两次入狱",
                    "• 1832年决斗身亡",
                    "• 理论死后14年才发表"
                ]
            },
            {
                "name": "斯里尼瓦瑟·拉马努金",
                "color": PINK,
                "details": [
                    "• 印度贫寒家庭出身",
                    "• 受哈代邀请赴剑桥",
                    "• 因战争与饮食不适患病",
                    "• 返回印度后病逝"
                ]
            }
        ]

        groups = []
        for m in mathematicians:
            group = VGroup(
                Text(m["name"], font="Microsoft YaHei", font_size=28, color=m["color"]),
                *[Text(detail, color=m["color"], font_size=20) for detail in m["details"]]
            )
            group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            groups.append(group)

        # 这里使用 VGroup 因为都是 Text 对象
        groups_vgroup = VGroup(*groups)
        groups_vgroup.arrange(RIGHT, buff=0.3)
        groups_vgroup.center()

        self.play(FadeIn(title), Create(underline), run_time=0.8)
        self.wait(0.5)

        # 流畅的淡入动画
        for group in groups:
            self.play(FadeIn(group, shift=RIGHT * 0.3), run_time=0.5)
        
        self.wait(1)

        final_text = Text("数学人才：人类思想的伟大结晶",
                        font="Microsoft YaHei",
                        font_size=30,
                        color=RED)
        final_text.to_edge(DOWN, buff=1)

        box = SurroundingRectangle(groups_vgroup, buff=0.4, color=BLUE, stroke_width=2)

        # 同时播放框和文字动画
        self.play(
            Create(box),
            Write(final_text),
            run_time=1.2
        )
        self.wait(3)


# 运行命令: manim -pqh 年轻数学家.py MultiImage