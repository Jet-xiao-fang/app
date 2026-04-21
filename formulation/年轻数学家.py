from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080

class MultiImage(Scene):
    def construct(self):
        self.showImage()
        self.wait(0.5)
        self.clear_scene()
        self.showDescribe()

    def showImage(self):
        self.camera.background_color = "#0F0F1A"

        items = [
            {
                "image": r"D:\Videos\图片素材\阿贝尔.jpg",
                "name": "尼尔斯·阿贝尔\n(1802-1829，27岁去世)",
                "symbols": [
                    "证明五次方程无一般代数解（1824），\n终结了数学界250年的猜想",
                    "开创椭圆函数论，提出“阿贝尔积分”\n“阿贝尔函数”等概念，为复变函数奠基"
                ],
                "color": YELLOW,
                "image_scale": 0.2
            },
            {
                "image": r"D:\Videos\图片素材\伽罗瓦.png",
                "name": "埃瓦里斯特·伽罗瓦\n(1811-1832，21岁去世)",
                "symbols": [
                    "创立伽罗瓦理论，用群论彻底解决\n代数方程根式可解性问题",
                    "奠定近世代数基础"
                ],
                "color": GREEN,
                "image_scale": 0.2
            },
            {
                "image": r"D:\Videos\图片素材\拉马.jpeg",
                "name": "斯里尼瓦瑟·拉马努金\n(1887-1920，32岁去世)",
                "symbols": [
                    "自学成才，留下3900个公式，涉及数论、\n分拆数、模形式等，如圆周率无穷级数表达式",
                    "直觉推导能力惊人，许多公式后被\n应用于物理（如黑洞熵）"
                ],
                "color": PINK,
                "image_scale": 0.2
            }
        ]

        groups = []
        for info in items:
            img = ImageMobject(info["image"]).scale(info["image_scale"])
            name = Text(info["name"], font="STXingkai", font_size=26, color=info["color"])

            # 使用 Text 替代 Tex，支持换行
            formula1 = Text(info["symbols"][0], font_size=18, color=info["color"], line_spacing=1.2)
            formula2 = Text(info["symbols"][1], font_size=18, color=info["color"], line_spacing=1.2)

            text_group = VGroup(name, formula1, formula2)
            text_group.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            text_group.next_to(img, RIGHT, buff=0.3)

            group = Group(img, text_group)
            groups.append(group)

        # 手动排列 groups
        for i, group in enumerate(groups):
            if i == 0:
                group.move_to(UP * 3)
            elif i == 1:
                group.move_to(ORIGIN)
            else:
                group.move_to(DOWN * 3)

        self.play(LaggedStart(
            FadeIn(groups[0], shift=UP * 0.5,run_time=2),
            FadeIn(groups[1], shift=UP * 0.5,run_time=2),
            FadeIn(groups[2], shift=UP * 0.5,run_time=2),
            lag_ratio=1
        ))
        self.wait(1)

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def showDescribe(self):
        title = Text("英年早逝的数学家",
                    font="STKaiti",
                    font_size=36,
                    color=WHITE)
        title.to_edge(UP, buff=1)

        underline = Line(LEFT, RIGHT, color=BLUE).scale(1.1)
        underline.next_to(title, DOWN, buff=0.1)

        # 创建三个独立的组，每组内部竖排
        group1 = VGroup(
            Text("尼尔斯·阿贝尔", font="STXingkai", font_size=28, color=YELLOW),
            Text("• 出身贫困，18岁负担全家生计", color=YELLOW, font_size=20),
            Text("• 论文被柯西遗失、勒让德拒评", color=YELLOW, font_size=20),
            Text("• 1829年贫病中去世", color=YELLOW, font_size=20),
            Text("• 去世两天后聘书送达", color=YELLOW, font_size=20)
        )
        group1.arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        group2 = VGroup(
            Text("埃瓦里斯特·伽罗瓦", font="STXingkai", font_size=28, color=GREEN),
            Text("• 论文两次被退回", color=GREEN, font_size=20),
            Text("• 投身共和运动两次入狱", color=GREEN, font_size=20),
            Text("• 1832年决斗身亡", color=GREEN, font_size=20),
            Text("• 理论死后14年才发表", color=GREEN, font_size=20)
        )
        group2.arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        group3 = VGroup(
            Text("斯里尼瓦瑟·拉马努金", font="STXingkai", font_size=28, color=PINK),
            Text("• 印度贫寒家庭出身", color=PINK, font_size=20),
            Text("• 受哈代邀请赴剑桥", color=PINK, font_size=20),
            Text("• 因战争与饮食不适患病", color=PINK, font_size=20),
            Text("• 返回印度后病逝", color=PINK, font_size=20)
        )
        group3.arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        # 将三个组整体竖排列，并居中
        groups = VGroup(group1, group2, group3)
        groups.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        groups.move_to(ORIGIN)

        self.add(title, underline)
        self.wait(0.5)

        # 逐组淡入显示
        for group in groups:
            self.play(FadeIn(group, shift=RIGHT * 0.3), run_time=0.5)
        
        self.wait(1)

        final_text = Text("数学人才：人类思想的伟大结晶",
                        font="Microsoft YaHei",
                        font_size=30,
                        color=RED)
        final_text.to_edge(DOWN, buff=1)

        box = SurroundingRectangle(groups, buff=0.4, color=BLUE, stroke_width=2)

        self.play(
            Create(box),
            Write(final_text),
            run_time=1.2
        )
        self.wait(3)
        
# manim -p 年轻数学家.py MultiImage