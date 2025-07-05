from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class BernoulliFamilyContributions(Scene):
    def construct(self):
        self.showImage()
        self.wait(1)
        self.clear_scene()
        self.showDescribe()
        
    def clear_scene(self):
        # 淡出所有内容，但保留背景色
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
    
    def showImage(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
       
        # 设置缩放比例和间距
        image_scale = 0.3
        group_buff = 0.4  # 减小垂直间距
        
        # 定义每组内容：图片路径、名称和公式
        items = [
            (
                r"D:\Videos\图片素材\雅各布·伯努利.png", 
                "雅各布·伯努利 (Jacob Bernoulli)",
                r"\text{概率论: } P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}",
                r"\text{大数定律: } \lim_{n \to \infty} P\left(\left|\frac{S_n}{n} - p\right| < \varepsilon\right) = 1"
            ),
            (
                r"D:\Videos\图片素材\约翰·伯努利.jpg", 
                "约翰·伯努利 (Johann Bernoulli)",
                r"\text{最速降线: } \int_{a}^{b} \frac{\sqrt{1 + (y')^2}}{\sqrt{y}} \, dx = \text{最小}",
                r"\text{悬链线: } y = a \cosh\left(\frac{x}{a}\right)"
            ),
            (
                r"D:\Videos\图片素材\丹尼尔·伯努利.jpg", 
                "丹尼尔·伯努利 (Daniel Bernoulli)",
                r"\text{流体方程: } \frac{1}{2} \rho v^2 + \rho g h + p = \text{常数}",
                r"\text{气体动力学: } p = \frac{1}{3} \rho \overline{v^2}"
            )
        ]

        groups = Group()
        colors = [YELLOW, GREEN, PINK]  # 每组不同的颜色
        
        for i, (img_path, name_str, formula_str1, formula_str2) in enumerate(items):
            if i == 1:  # 约翰·伯努利
                img = ImageMobject(img_path).scale(0.5)
            else:
                img = ImageMobject(img_path).scale(image_scale)
            
            # 创建名称文本（减小字体大小到24）
            name = Text(name_str, font="Microsoft YaHei", font_size=24, color=colors[i])
            
            # 创建两个公式（减小缩放比例到0.55）
            formula1 = MathTex(formula_str1, color=colors[i]).scale(0.55)
            formula2 = MathTex(formula_str2, color=colors[i]).scale(0.55)
            
            # 创建垂直组：名称 + 公式1 + 公式2（减小文本间距）
            text_group = VGroup(name, formula1, formula2)
            text_group.arrange(DOWN, buff=0.1, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.2)  # 增加图片与文本间距
            
            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)
            
        # 排列所有组（减小组间距）
        groups.arrange(DOWN, buff=group_buff).shift(UP*0.2)
        
        # 动画展示
        self.play(LaggedStart(
            FadeIn(groups[0], shift=UP*0.5),
            FadeIn(groups[1], shift=UP*0.5),
            FadeIn(groups[2], shift=UP*0.5),
            lag_ratio=1.0
        ))
        self.wait(4)
    
    def showDescribe(self):
        # 创建标题
        title = Text("伯努利家族的科学贡献", 
                     font="Microsoft YaHei", 
                     font_size=36, 
                     color=WHITE)
        title.to_edge(UP)
        
        # 添加装饰线
        underline = Line(LEFT, RIGHT, color=BLUE).scale(1.2)
        underline.next_to(title, DOWN, buff=0.2)
        
        # 创建贡献列表
        contributions = VGroup(
            Text("雅各布·伯努利:", font="Microsoft YaHei", font_size=32, color=YELLOW),
            Text("1. 概率论奠基人", color=YELLOW, font_size=28),
            Text("2. 大数定律发现者", color=YELLOW, font_size=28),
            Text("3. 伯努利数创造者", color=YELLOW, font_size=28),
            
            Text("约翰·伯努利:", font="Microsoft YaHei", font_size=32, color=GREEN),
            Text("1. 变分法先驱", color=GREEN, font_size=28),
            Text("2. 欧拉的导师", color=GREEN, font_size=28),
            Text("3. 解决最速降线问题", color=GREEN, font_size=28),
            
            Text("丹尼尔·伯努利:", font="Microsoft YaHei", font_size=32, color=PINK),
            Text("1. 流体力学之父", color=PINK, font_size=28),
            Text("2. 伯努利原理提出者", color=PINK, font_size=28),
            Text("3. 气体动力学开创者", color=PINK, font_size=28)
        )
        
        # 排列贡献列表为三列
        column1 = VGroup(contributions[0], contributions[1], contributions[2], contributions[3])
        column1.arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(LEFT*4 + UP*0.5)
        
        column2 = VGroup(contributions[4], contributions[5], contributions[6], contributions[7])
        column2.arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(UP*0.5)
        
        column3 = VGroup(contributions[8], contributions[9], contributions[10], contributions[11])
        column3.arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(RIGHT*4 + UP*0.5)
        
        # 动画展示标题
        self.play(Write(title), Create(underline))
        self.wait(1)
        
        # 动画展示贡献列表
        self.play(FadeIn(column1, shift=RIGHT))
        self.wait(0.5)
        self.play(FadeIn(column2, shift=RIGHT))
        self.wait(0.5)
        self.play(FadeIn(column3, shift=RIGHT))
        self.wait(2)
        
        # 添加最终强调
        final_text = Text("数学物理王朝的传奇", 
                         font="Microsoft YaHei", 
                         font_size=40, 
                         color=RED)
        final_text.to_edge(DOWN, buff=0.7)
        
        # 添加装饰框
        box = SurroundingRectangle(
            VGroup(column1, column2, column3),
            buff=0.5,
            color=BLUE,
            stroke_width=2
        )
        
        # 动画展示
        self.play(
            Create(box),
            Write(final_text),
            run_time=2
        )
        self.wait(4)