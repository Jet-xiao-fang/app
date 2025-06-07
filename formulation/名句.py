from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class OptimizedMultiImage(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        
        # 添加标题 "量子力学三剑客"
        title = Tex("量子力学三剑客", color=BLUE).scale(1)
        title_box = SurroundingRectangle(title, color=WHITE, stroke_width=1, buff=0.4)
        title_group = VGroup(title, title_box)
        title_group.to_edge(UP, buff=0.5)
        title_box.surround(title, stretch=True)
        
        # 设置缩放比例和间距
        image_scale = 0.3
        group_buff = 0.4
        
        # 定义每组内容
        items = [
            (r"D:\Videos\图片素材\hs", "提出矩阵力学、不确定性原理"),
            (r"D:\Videos\图片素材\dila", "提出狄拉克方程、预测反物质"),
            (r"D:\Videos\图片素材\xue", "创立了波动力学，提出了量子力学的核心方程——薛定谔方程")
        ]

        groups = Group()
        colors = [YELLOW, GREEN, PINK]
        
        for i, (img_path, formula_str) in enumerate(items):
            # 创建图像
            img = ImageMobject(img_path).scale(image_scale)
            
            # 创建对应的文本
            formula = Tex(formula_str, color=colors[i]).scale(0.8)
            
            # 组合图片和公式
            group = Group(img, formula).arrange(RIGHT, buff=0.4, aligned_edge=ORIGIN)
            groups.add(group)
        
        # 排列所有组（左对齐）
        groups.arrange(DOWN, buff=group_buff, aligned_edge=ORIGIN)
        groups.next_to(title_group, DOWN, buff=0.5)  # 将内容组放在标题下方
        
        # 动画展示 - 先显示标题，然后逐个显示图片和公式
        self.play(
            Create(title_box),
            Write(title),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(LaggedStart(
            *[FadeIn(group, shift=UP*0.5) for group in groups],
            lag_ratio=1.2
        ))
        self.wait(2)
        # 添加最终强调
        final_text = Text("物理之美", font="Microsoft YaHei", font_size=26, color=RED)
        self.play(Write(final_text.to_edge(DOWN, buff=0.2)))
        self.wait(4)