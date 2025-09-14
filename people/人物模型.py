from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class MultiImage(Scene):
    def construct(self):
        self.showImage()
        
    def showImage(self):
        # 设置深色背景
        self.camera.background_color = "#0F0F1A"
        title = Text("数学符号发明人", font="Microsoft YaHei", font_size=48, color=YELLOW)
        self.play(Write(title.to_edge(UP, buff=0.9)))
        # 设置缩放比例和间距
        image_scale = 0.2
        group_buff = 0.5
        
        # 定义每组内容：图片路径、名称和公式
        items = [
            {
                "name": "莱布尼茨",
                "image": r"D:\Videos\图片素材\莱布尼茨.jpg",
                "symbols": [
                    (r"\int", "积分符号 (1675年)"),
                    (r"\frac{d}{dx}", "微分符号"),
                    (r"=", "等号")
                ],
                "color": YELLOW
            },
            {
                "name": "欧拉",
                "image": r"D:\Videos\图片素材\欧拉.jpeg",
                "symbols": [
                    (r"e", "自然常数 (1736年)"),
                    (r"i", "虚数单位"),
                    (r"\sum", "求和符号"),
                    (r"f(x)", "函数表示法")
                ],
                "color": RED_C
            },
            {
                "name": "高斯",
                "image": r"D:\Videos\图片素材\高斯.jpeg",
                "symbols": [
                    (r"\equiv", "同余符号"),
                    (r"\bmod", "模运算符号"),
                    (r"i", "复数单位")
                ],
                "color": BLUE
            },
            {
                "name": "牛顿",
                "image": r"D:\Videos\图片素材\牛顿.jpeg",
                "symbols": [
                    (r"\dot{x}", "流数记号 (导数)"),
                    (r"\binom{n}{k}", "二项式系数"),
                    (r"\infty", "无穷大符号")
                ],
                "color": PINK
            }
        ]

        groups = Group()  # 使用 Group 而不是 VGroup
        
        for i, info in enumerate(items):
            if i == 0:
                img = ImageMobject(info["image"]).scale(0.5)
            else: 
                img = ImageMobject(info["image"]).scale(image_scale)
            
            # 创建名称文本
            name = Text(info["name"], font="Microsoft YaHei", font_size=26, color=info["color"])
            
            # 创建符号组
            symbol_group = VGroup()
            for j, (symbol, desc) in enumerate(info["symbols"]):
                sym = MathTex(symbol, font_size=26, color=info["color"])
                txt = Text(desc, font="Microsoft YaHei", font_size=20, color=WHITE)
                group = VGroup(sym, txt).arrange(RIGHT, buff=0.2)
                symbol_group.add(group)
            
            symbol_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            
             # 整体组合
            content_group = VGroup(name, symbol_group).arrange(DOWN, buff=0.5)
            # text_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.2)
            
            # 将图片和文本组组合 - 使用 Group 而不是 VGroup
            group = Group(img, content_group).arrange(RIGHT, buff=1)
            groups.add(group)
            
        # 排列所有组，左对齐
        groups.arrange(DOWN, buff=group_buff, aligned_edge=LEFT).to_edge(LEFT, buff=0.5)
        
        # 动画展示
        self.play(LaggedStart(
            FadeIn(groups[0], shift=UP*0.5),
            FadeIn(groups[1], shift=UP*0.5),
            FadeIn(groups[2], shift=UP*0.5),
            FadeIn(groups[3], shift=UP*0.5),
            lag_ratio=1.0,
            run_time=6
        ))
        self.wait(3)
        
    def clear_scene(self):
        # 淡出所有内容，但保留背景色
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
    def showDescribe(self):
        # 创建标题
        title = Text("物理学巨匠的科学贡献", 
                    font="Microsoft YaHei", 
                    font_size=32,
                    color=WHITE)
        title.to_edge(UP, buff=0.5)
        
        # 添加装饰线
        underline = Line(LEFT, RIGHT, color=BLUE).scale(1.2)
        underline.next_to(title, DOWN, buff=0.1)
        
        # 创建贡献列表
        contributions = VGroup(
            Text("牛顿", font="Microsoft YaHei", font_size=28, color=YELLOW),
            Text("• 经典力学体系奠基人", color=YELLOW, font_size=24),
            Text("• 万有引力定律", color=YELLOW, font_size=24),
            Text("• 微积分发明者之一", color=YELLOW, font_size=24),
            Text("• 光学色散研究先驱", color=YELLOW, font_size=24),
            
            Text("爱因斯坦", font="Microsoft YaHei", font_size=28, color=GREEN),
            Text("• 相对论创立者", color=GREEN, font_size=24),
            Text("• 质能方程提出者", color=GREEN, font_size=24),
            Text("• 光电效应理论解释者", color=GREEN, font_size=24),
            Text("• 宇宙学常数提出者", color=GREEN, font_size=24),
            
            Text("麦克斯韦", font="Microsoft YaHei", font_size=28, color=PINK),
            Text("• 电磁理论集大成者", color=PINK, font_size=24),
            Text("• 麦克斯韦方程组创立者", color=PINK, font_size=24),
            Text("• 电磁波预言者", color=PINK, font_size=24),
            Text("• 气体分子运动论奠基人", color=PINK, font_size=24)
        )
        
        # 将所有贡献项垂直排列
        contributions.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        contributions.scale(0.9)  # 稍微缩小以适应屏幕
        contributions.to_edge(LEFT, buff=1.0)  # 左对齐，留出边距
        
        # 动画展示标题
        self.play(Write(title), Create(underline))
        self.wait(0.5)
        
        # 动画展示贡献列表
        self.play(FadeIn(contributions, shift=RIGHT))
        self.wait(1)
        
        # 添加最终强调
        final_text = Text("科学巨匠：人类智慧的璀璨星辰", 
                        font="Microsoft YaHei", 
                        font_size=36,
                        color=RED)
        final_text.to_edge(DOWN, buff=0.5)
        
        # 添加装饰框
        box = SurroundingRectangle(
            contributions,
            buff=0.3,
            color=BLUE,
            stroke_width=2
        )
        
        # 动画展示
        self.play(
            Create(box),
            Write(final_text),
            run_time=1.5
        )
        self.wait(3)
        
# manim -pqh 人物模型.py MultiImage