from manim import *
import numpy as np
import random
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class QuantumGallery(Scene):
    def construct(self):
        # 宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        title = Text("1900-1935 量子革命时代", color=YELLOW, font="Microsoft YaHei")
        title.to_edge(UP,buff=3)
        self.add(title)
        self.wait(0.5)
        
        # 图片路径 (使用你的实际路径)
        image_paths = [
            r"D:\Videos\图片素材\普朗克.png",
            r"D:\Videos\图片素材\爱因斯坦.jpeg",
            r"D:\Videos\图片素材\康普顿.jpeg",
            r"D:\Videos\图片素材\卢瑟福.jpg",
            r"D:\Videos\图片素材\玻尔.png",
            r"D:\Videos\图片素材\德布罗意.jpeg",
            r"D:\Videos\图片素材\海森堡.jpg",
            r"D:\Videos\图片素材\薛定谔.jpg",
            r"D:\Videos\图片素材\狄拉克.jpeg"
        ]

        # 描述文本
        descriptions = [
            ["马克斯·普朗克", "(1858-1947)", "量子假说", "黑体辐射"],
            ["阿尔伯特·爱因斯坦", "(1879-1955)", "光量子理论", "受激辐射"],
            ["阿瑟·康普顿", "(1892-1962)", "康普顿效应", "光子动量"],
            ["欧内斯特·卢瑟福", "(1871-1937)", "核式结构模型", "人工核反应"],
            ["尼尔斯·玻尔", "(1885-1962)", "量子化原子", "哥本哈根诠释"],
            ["路易·德布罗意", "(1892-1987)", "物质波假设", "波动力学"],
            ["维尔纳·海森堡", "(1901-1976)", "矩阵力学", "不确定性原理"],
            ["埃尔温·薛定谔", "(1887-1961)", "波动力学方程", "薛定谔猫"],
            ["保罗·狄拉克", "(1902-1984)", "狄拉克方程", "反物质"]
        ]
        
        # 创建图片-文字组合
        image_text_pairs = []
        for path, desc_lines in zip(image_paths, descriptions):
            # 使用 Group 而不是 VGroup
            group = Group()
            
            # 添加图片
            img = ImageMobject(path)
            img.height = 2.8
            
            # 创建更大的圆形边框
            border_radius = img.height/2 * 1.25  # 增加边框尺寸比例
            border = Circle(
                radius=border_radius,
                color="#4a86e8",
                stroke_width=4,  # 增加边框宽度
                fill_opacity=0,
                stroke_opacity=0.8
            )
            border.move_to(img.get_center())
            
            # 添加更大的光晕效果
            glow = Circle(
                radius=border_radius * 1.15,  # 增加光晕尺寸
                color="#4a86e8",
                stroke_width=0,
                fill_opacity=0.2
            )
            glow.move_to(img.get_center())
            
            # 创建文字组
            text_group = VGroup()
            for i, line in enumerate(desc_lines):
                if i == 0:  # 姓名
                    text = Text(line, font_size=30, font="Microsoft YaHei", weight="BOLD", color="#FFD700")
                elif i == 1:  # 年份
                    text = Text(line, font_size=24, font="Microsoft YaHei", color="#4FC3F7")
                else:  # 描述
                    text = Text(line, font_size=26, font="Microsoft YaHei", color="WHITE")
                text_group.add(text)
            
            # 排列文字组
            text_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            text_group.next_to(border, DOWN, buff=0.3)
            
            # 添加所有元素到组中
            group.add(glow, border, img, text_group)
            image_text_pairs.append(group)
            group.scale(0.85)

        # 排列图片组 - 使用 Group 而不是 VGroup
        gallery = Group(*image_text_pairs)
        gallery.arrange(RIGHT, buff=1.5)
        
        # 初始位置：屏幕右侧外
        gallery.move_to(RIGHT * (config.frame_width/2 + gallery.get_width()/2))
        
        # 目标位置：屏幕左侧外
        target_position = gallery.copy()
        target_position.move_to(LEFT * (config.frame_width/2 + gallery.get_width()/2))

        # 直接添加画廊到场景（不再设置透明度）
        self.add(gallery)
        
        # 添加时间线
        timeline = NumberLine(
            x_range=[1900, 1935, 5],
            length=10,
            color="#4a86e8",
            stroke_width=2
        )
        timeline.to_edge(UP, buff=1.8).shift(DOWN * 3.0)
        
        # 添加年份标记
        years = [1900, 1905, 1910, 1915, 1920, 1925, 1930, 1935]
        year_marks = VGroup()
        for year in years:
            mark = Triangle(color="#99ccff", fill_opacity=1).scale(0.1)
            mark.rotate(PI)
            mark.move_to(timeline.n2p(year))
            
            year_text = Text(str(year), font_size=20, color="#99ccff")
            year_text.next_to(mark, DOWN, buff=0.1)
            year_marks.add(mark, year_text)
        
        timeline_group = VGroup(timeline, year_marks)
        timeline_group.set_opacity(0)
        
        self.add(timeline_group)
        
        # 缓慢滚动动画
        scroll_time = 30
        self.play(
            gallery.animate.move_to(target_position),
            timeline_group.animate.set_opacity(0.7),
            run_time=scroll_time,
            rate_func=linear
        )
        
        # 结束场景
        ending = Text("量子革命: 重塑物理学", color=RED, font="Microsoft YaHei")
        ending.to_edge(DOWN, buff=3)
        
        # 创建退出动画
        self.play(
            FadeIn(ending, shift=UP),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(1)
# manim -pqh --format=png 图片排列.py QuantumGallery -r 1920,1080