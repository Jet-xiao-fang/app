from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImageGallery(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 添加标题
        title = Text("量子物理学奠基人", font_size=40, color=YELLOW)
        title.to_edge(UP)
        self.add(title)
        self.wait(0.5)
        
        # 图片路径
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

        # 重新设计的描述文本
        descriptions = [
            # 普朗克
            "\\begin{array}{c} \\text{马克斯·普朗克} \\\\ \\text{(1858–1947)} \\\\ \\hline \\text{1900年提出量子假说} \\\\ \\text{解释黑体辐射} \\\\ \\text{奠基量子理论} \\end{array}",
            # 爱因斯坦
            "\\begin{array}{c} \\text{阿尔伯特·爱因斯坦} \\\\ \\text{(1879–1955)} \\\\ \\hline \\text{1905年提出光量子理论} \\\\ \\text{1916年预言受激辐射} \\\\ \\text{(激光原理)} \\end{array}",
            # 康普顿
            "\\begin{array}{c} \\text{阿瑟·康普顿} \\\\ \\text{(1892–1962)} \\\\ \\hline \\text{1923年发现康普顿效应} \\\\ \\text{证实光子动量} \\end{array}",
            # 卢瑟福
            "\\begin{array}{c} \\text{欧内斯特·卢瑟福} \\\\ \\text{(1871–1937)} \\\\ \\hline \\text{1911年提出} \\\\ \\text{原子核式结构模型} \\\\ \\text{1919年实现人工核反应} \\end{array}",
            # 玻尔
            "\\begin{array}{c} \\text{尼尔斯·玻尔} \\\\ \\text{(1885–1962)} \\\\ \\hline \\text{1913年提出} \\\\ \\text{量子化原子模型} \\\\ \\text{1927年创立哥本哈根诠释} \\end{array}",
            # 德布罗意
            "\\begin{array}{c} \\text{路易·德布罗意} \\\\ \\text{(1892–1987)} \\\\ \\hline \\text{1924年提出物质波假设} \\\\ \\text{奠定波动力学基础} \\end{array}",
            # 海森堡
            "\\begin{array}{c} \\text{维尔纳·海森堡} \\\\ \\text{(1901–1976)} \\\\ \\hline \\text{1925年创立矩阵力学} \\\\ \\text{1927年提出不确定性原理} \\end{array}",
            # 薛定谔
            "\\begin{array}{c} \\text{埃尔温·薛定谔} \\\\ \\text{(1887–1961)} \\\\ \\hline \\text{1926年提出} \\\\ \\text{波动力学方程} \\\\ \\text{1935年发表薛定谔猫} \\end{array}",
            # 狄拉克
            "\\begin{array}{c} \\text{保罗·狄拉克} \\\\ \\text{(1902–1984)} \\\\ \\hline \\text{1928年创立狄拉克方程} \\\\ \\text{1931年预言反物质存在} \\end{array}"
        ]

        # 创建图片-文字组合
        image_text_pairs = []
        for path, desc in zip(image_paths, descriptions):
            # 创建容器组
            group = Group()
            
            # 添加图片
            img = ImageMobject(path)
            img.height = 3
            group.add(img)
            
            # 添加文字 - 使用数组格式确保排版
            text = MathTex(desc, font_size=24, color=WHITE)
            text.next_to(img, DOWN, buff=0.3)  # 增加间距
            group.add(text)
            
            image_text_pairs.append(group)

        # 排列图片组
        gallery = Group(*image_text_pairs)
        gallery.arrange(RIGHT, buff=1.0)

        # 初始位置：屏幕右侧外
        screen_width = config.frame_width
        gallery.next_to(ORIGIN, RIGHT, buff=0)
        gallery.shift(RIGHT * (screen_width / 2))

        # 目标位置：屏幕左侧外
        gallery_width = gallery.get_width()
        target_position = gallery.copy()
        target_position.shift(LEFT * (screen_width + gallery_width))

        # 动画序列
        self.play(
            gallery.animate.set_opacity(1),
            run_time=1
        )
        self.play(
            gallery.animate.move_to(target_position.get_center()),
            run_time=45,  # 缓慢滚动
            rate_func=linear
        )
        self.play(
            gallery.animate.set_opacity(0),
            run_time=1
        )
        
        # 结束字幕
        ending = Text("量子物理学发展历程", font_size=40, color=BLUE)
        self.play(Write(ending))
        self.wait(2)
