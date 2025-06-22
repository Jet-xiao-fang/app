from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class BiologyPioneersScene(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        # 标题
        title = Tex("高中生物$4$大人物", font_size=48, color=YELLOW).to_edge(UP,buff=1.5)
        self.add(title)
        self.wait(0.5)
        
        # 生物学家信息
        biologists = [
            {
                "name": "孟德尔",
                "image": r"D:\Videos\图片素材\孟德尔.jpeg",
                "contributions": [
                    ("分离定律", "F₂代性状分离比 3:1"),
                    ("自由组合定律", "两对性状独立遗传"),
                    ("遗传因子假说", "显性与隐性遗传因子")
                ],
                "color": GREEN
            },
            {
                "name": "达尔文",
                "image": r"D:\Videos\图片素材\达尔文.jpeg",
                "contributions": [
                    ("自然选择学说", "适者生存，不适者淘汰"),
                    ("共同由来学说", "所有生物有共同祖先"),
                    ("《物种起源》", "1859年出版")
                ],
                "color": ORANGE
            },
            {
                "name": "沃森与克里克",
                "image": r"D:\Videos\图片素材\沃森.jpg",
                "contributions": [
                    ("DNA双螺旋结构", "1953年提出"),
                    ("碱基互补配对", "A-T, G-C配对原则"),
                    ("备受争论", "关于黑人智商问题")
                ],
                "color": BLUE
            },
            {
                "name": "林奈",
                "image": r"D:\Videos\图片素材\林奈.jpg",
                "contributions": [
                    ("生物分类系统", "界、门、纲、目、科、属、种"),
                    ("双名法", "属名 + 种加词"),
                    ("现代分类学奠基人", "18世纪提出")
                ],
                "color": PURPLE
            }
        ]
        
        # 创建并展示每位生物学家
        groups = Group()
        y_positions = [4, 1, -2, -5]
        for i, bio_info in enumerate(biologists):
            # 加载图片
            img = ImageMobject(bio_info["image"])
            if i == 3 or i == 0:
                img.scale(0.3)
            else:
                img.scale(0.2)
            
            # 创建贡献组
            contrib_group = VGroup()
            for j, (title, desc) in enumerate(bio_info["contributions"]):
                # 贡献标题
                title_text = Text(title, font="Microsoft YaHei", 
                                 font_size=20, color=bio_info["color"])
                # 贡献描述
                desc_text = Text(desc, font="Microsoft YaHei", 
                                font_size=16, color=WHITE)
                # 组合
                group = VGroup(title_text, desc_text).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
                contrib_group.add(group)
            
            contrib_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            
            # 生物学家名字
            name_text = Text(bio_info["name"],
                            font_size=24, color=bio_info["color"])
            
            # 整体组合
            content_group = VGroup(name_text, contrib_group).arrange(DOWN, buff=0.2)
            group = Group(img, content_group).arrange(RIGHT, buff=0.8)
            group.move_to(y_positions[i] * UP)
            
            # 添加到场景
            self.play(
                FadeIn(img, shift=RIGHT),
                Write(content_group, shift=LEFT),
                run_time=3
            )
            self.wait(0.5)
            groups.add(group)
        
        # 最终文本
        final_text = Text("生命科学：揭示自然奥秘", 
                         font="Microsoft YaHei", font_size=36, color=GOLD)
        self.play(Write(final_text.to_edge(DOWN, buff=0.8)))
        self.wait(3)
        
        # 结束动画
        self.play(
            groups.animate.scale(0.85).shift(UP*0.5),
            final_text.animate.scale(1.2).set_color("#00FFCC"),
            run_time=2
        )
        self.wait(3)
        
# manim -pqh --format=png 生物大神.py BiologyPioneersScene -r 1920,1080
        