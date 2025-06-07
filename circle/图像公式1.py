from manim import *

class MultiImage(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
       
        # 设置缩放比例和间距
        image_scale = 0.3
        group_buff = 0.5
        
        # 定义每组内容：图片路径、名称和公式
        items = [
            (
                r"D:\Videos\图片素材\欧拉", 
                "欧拉公式 (Basel问题)",
                r"\pi = \sqrt{6 \sum_{n=1}^{\infty} \frac{1}{n^2}}"
            ),
            (
                r"D:\Videos\图片素材\高斯", 
                "高斯-勒让德积分公式",
                r"\pi = \left( \int_{-\infty}^{\infty} e^{-x^2} \, dx \right)^2"
            ),
            (
                r"D:\Videos\图片素材\拉马", 
                "拉马努金公式",
                r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)!(1103 + 26390k)}{(k!)^4 396^{4k}}"
            )
        ]

        groups = Group()
        colors = [YELLOW, GREEN, PINK]  # 每组不同的颜色
        
        for i, (img_path, name_str, formula_str) in enumerate(items):
            # 创建图像
            img = ImageMobject(img_path).scale(image_scale)
            
            # 创建名称文本
            name = Text(name_str, font="Microsoft YaHei", font_size=26, color=colors[i])
            
            # 创建公式
            formula = MathTex(formula_str, color=colors[i]).scale(0.8)
            if "sum" in formula_str:  # 针对较长的公式进行额外缩放
                formula.scale(0.85)
            
            # 创建垂直组：名称 + 公式
            text_group = VGroup(name, formula)
            text_group.arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.4)
            
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
        self.wait(1)
        
        self.wait(2)
        
        # 添加最终强调
        final_text = Text("π是一个超越数！", font="Microsoft YaHei", font_size=36, color=RED)
        self.play(Write(final_text.to_edge(DOWN, buff=0.5)))
        self.wait(4)