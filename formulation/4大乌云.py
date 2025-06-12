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
            r"D:\Videos\图片素材\爱.jpeg",
            r"D:\Videos\图片素材\牛.jpeg",
            r"D:\Videos\图片素材\杨.jpeg",
            r"D:\Videos\图片素材\tou.png"
        ]
        titile = Text("科学家的晚年生活", font="Microsoft YaHei", font_size=36, color=BLUE)
        self.add(titile.to_edge(UP, buff=1.5))
        # 左对齐参数
        LEFT_BUFF = 0.8  # 左侧边距
        
        y_positions = [4, 1, -2, -5]
        groups = Group()
        for i, file in enumerate(img_files):
            img = ImageMobject(file)

            img.scale(0.3)

            img.move_to(y_positions[i] * UP)
           
            if i == 0:
                text_group = VGroup(
                    Text("​1. 量子力学与广义相对论的矛盾", font_size=30, color=RED_C),
                    Text(
                        "广义相对论完美描述宏观引力（如天体运动），量子力学精准解释微观粒子行为，\n"
                        "但两者在黑洞奇点、宇宙起源等极端尺度下无法兼容。",
                        font_size=20,
                        color=RED_C,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            elif i == 1:
                text_group = VGroup(
                    Text("2. 暗物质与暗能量的本质", font_size=30, color=BLUE),
                    Text(
                        "暗物质粒子（如WIMP）未被直接探测到，现有粒子物理标准模型无法解释",
                        font_size=20,
                        color=BLUE,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            elif i == 2:
                text_group = VGroup(
                    Tex(r"3. 正反物质不对称性问题", font_size=30, color=YELLOW),
                    Text(
                        "根据大爆炸理论，宇宙诞生时应产生等量正物质与反物质，两者相遇会湮灭。\n"
                        "但现实宇宙几乎全部由正物质构成。",
                        font_size=20,
                        color=YELLOW,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            else:
                text_group = VGroup(
                    Text(f"大统一理论与万有理论的缺失", font_size=30, color=PINK),
                    Text(
                        "统一除引力外的三种基本力（电磁力、强力、弱力），\n"
                        "最终纳入引力形成“万有理论",
                        font_size=20,
                        color=PINK,
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            
            # 设置图片位置（左对齐）
            # img.set_width(IMAGE_WIDTH)
            img.to_edge(LEFT, buff=LEFT_BUFF)

            text_group.next_to(img, RIGHT, buff=0.3)
            # text_group.align_to(img, ORANGE)  # 文字顶部与图片顶部对齐
            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)

            # 同时显示图片和文字,我可以更好的控制每一个元素
            self.play(LaggedStart(FadeIn(group, shift=UP * 0.5,scale=0.8), lag_ratio=1.0))
            
            self.wait(1.0)
        final_text = Text("四大乌云中任一问题的突破，都可能引发物理学革命", font="Microsoft YaHei", font_size=24, color=RED)
        self.play(Write(final_text.to_edge(DOWN, buff=0.8)))
        self.wait(5)
    

# manim -pqh --format=png 4大乌云.py ImageScene -r 1920,1080
