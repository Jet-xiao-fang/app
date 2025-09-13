from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MultiImage(Scene):
    def construct(self):
        self.showImage()
        self.clear_scene()
        self.showDescribe()
        
    def showImage(self):
        # 设置深色背景
        self.camera.background_color = "#0F0F1A"
       
        # 设置缩放比例和间距
        image_scale = 0.3
        group_buff = 0.5
        
        # 定义每组内容：图片路径、名称和公式
        items = [
            {
                "image": r"D:\Videos\图片素材\牛顿.jpeg", 
                "name": r"牛顿",
                "symbols": [
                    r"F = G\frac{m_1 m_2}{r^2}",  # 万有引力定律
                    r"F = ma"  # 牛顿第二定律
                ],
                "color": YELLOW
            },
            {
                "image": r"D:\Videos\图片素材\爱因斯坦.jpeg", 
                "name": r"爱因斯坦",
                "symbols": [
                    r"E = mc^2",  # 质能方程
                    r"R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \kappa T_{\mu\nu}"  # 爱因斯坦场方程简化版
                ],
                "color": GREEN
            },
            {
                "image": r"D:\Videos\图片素材\麦克斯韦.jpg", 
                "name": r"麦克斯韦",
                "symbols": [
                    r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}",  # 高斯定律
                    r"\nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t}"  # 安培定律
                ],
                "color": PINK
            }
        ]

        groups = Group()
        
        for i, info in enumerate(items):
            if i == 1:
                img = ImageMobject(info["image"]).scale(0.5)
            else: 
                img = ImageMobject(info["image"]).scale(image_scale)
            # 创建名称文本
            name = Text(info["name"], font="Microsoft YaHei", font_size=26, color=info["color"])
            
            # 简化公式显示
            formula1 = MathTex(info["symbols"][0], color=info["color"]).scale(0.55)
            formula2 = MathTex(info["symbols"][1], color=info["color"]).scale(0.55)
            
            # 创建垂直组：名称 + 公式
            text_group = VGroup(name, formula1, formula2)
            text_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.2)
            
            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)
            
        # 排列所有组
        groups.arrange(DOWN, buff=group_buff).shift(UP*0.2)
        
        # 动画展示
        self.play(LaggedStart(
            FadeIn(groups[0], shift=UP*0.5),
            FadeIn(groups[1], shift=UP*0.5),
            FadeIn(groups[2], shift=UP*0.5),
            lag_ratio=1.0
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
        
        # 排列贡献列表为三列
        column1 = VGroup(*contributions[0:5])
        column1.arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(LEFT*4 + UP*0.2)
        
        column2 = VGroup(*contributions[5:10])
        column2.arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(UP*0.2)
        
        column3 = VGroup(*contributions[10:])
        column3.arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(RIGHT*4 + UP*0.2)
        
        # 动画展示标题
        self.play(Write(title), Create(underline))
        self.wait(0.5)
        
        # 动画展示贡献列表
        self.play(FadeIn(column1, shift=RIGHT))
        self.play(FadeIn(column2, shift=RIGHT))
        self.play(FadeIn(column3, shift=RIGHT))
        self.wait(1)
        
        # 添加最终强调
        final_text = Text("科学巨匠：人类智慧的璀璨星辰", 
                        font="Microsoft YaHei", 
                        font_size=36,
                        color=RED)
        final_text.to_edge(DOWN, buff=0.5)
        
        # 添加装饰框
        box = SurroundingRectangle(
            VGroup(column1, column2, column3),
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