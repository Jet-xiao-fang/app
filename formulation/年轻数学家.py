from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class MultiImage(Scene):
    def construct(self):
        self.showImage()
        self.wait(0.5)
        self.clear_scene()
        self.showDescribe()
        
    def showImage(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
       
        # 设置缩放比例和间距
        image_scale = 0.3
        group_buff = 0.5
        
        # 定义每组内容：图片路径、名称和公式
        items = [
            {
                "image": r"D:\Videos\图片素材\阿贝尔.jpg", 
                "name": r"尼尔斯·阿贝尔：(1802-1829，27岁去世)",
                "symbols": [
                    r"证明五次方程无一般代数解（1824），终结了数学界250年的猜想",
                    r"开创椭圆函数论，提出“阿贝尔积分”“阿贝尔函数”等概念，为复变函数奠基"
                ],
                "color": YELLOW
            },
            {
                "image": r"D:\Videos\图片素材\伽罗瓦.png", 
                "name": r"埃瓦里斯特·伽罗瓦：(1811-1832，21岁去世)",
                "symbols": [
                    r"创立伽罗瓦理论，用群论彻底解决代数方程根式可解性问题",
                    r"奠定近世代数基础"
                ],
                "color": GREEN
            },
            {
                "image": r"D:\Videos\图片素材\拉马.jpeg", 
                "name": r"斯里尼瓦瑟·拉马努金：(1887-1920，32岁去世)",
                "symbols": [
                    r"自学成才，留下3900个公式，涉及数论、分拆数、模形式等，如圆周率无穷级数表达式",
                    r"直觉推导能力惊人，许多公式后被应用于物理（如黑洞熵）"
                ],
                "color": PINK
            }
        ]

        groups = Group()
        
        for i, info in enumerate(items):
            if i==0:
                img = ImageMobject(info["image"]).scale(image_scale)
            elif i==1:
                img = ImageMobject(info["image"]).scale(image_scale)
            else:
                img = ImageMobject(info["image"]).scale(image_scale)
            
            # 创建名称文本
            name = Text(info["name"], font="STXingkai", font_size=26, color=info["color"])
            
            formula1 = Tex(info["symbols"][0], color=info["color"]).scale(0.55)
            formula2 = Tex(info["symbols"][1], color=info["color"]).scale(0.55)
            
            # 创建垂直组：名称 + 公式
            text_group = VGroup(name, formula1, formula2)
            text_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(img, RIGHT, buff=0.2)
            
            # 将图片和文本组组合
            group = Group(img, text_group)
            groups.add(group)
            
        # 排列所有组
        groups.arrange(DOWN, buff=group_buff).shift(UP*0.2)
        
        # 动画展示
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
        title = Text("英年早逝的数学家", 
                    font="STKaiti",
                    font_size=38,  # 减小标题字号
                    color=WHITE)
        title.to_edge(UP, buff=0.5)  # 增加上边距
        
        # 添加装饰线
        underline = Line(LEFT, RIGHT, color=BLUE).scale(1.2)
        underline.next_to(title, DOWN, buff=0.1)  # 减小间距
        
        # 创建贡献列表 - 精简内容并减小字号
        contributions = VGroup(
            Text("尼尔斯·阿贝尔", font="STXingkai", font_size=28, color=YELLOW),
            Text("• 出身贫困，18岁负担全家生计", color=YELLOW, font_size=20),
            Text("• 论文被柯西遗失、勒让德拒评", color=YELLOW, font_size=20),
            Text("• 1829年贫病中去世", color=YELLOW, font_size=24),
            Text("• 去世两天后聘书送达", color=YELLOW, font_size=24),
            
            Text("埃瓦里斯特·伽罗瓦", font="STXingkai", font_size=28, color=GREEN),
            Text("• 论文两次被退回", color=GREEN, font_size=24),
            Text("• 投身共和运动两次入狱", color=GREEN, font_size=24),
            Text("• 1832年决斗身亡", color=GREEN, font_size=24),
            Text("• 理论死后14年才发表", color=GREEN, font_size=24),
            
            Text("斯里尼瓦瑟·拉马努金", font="STXingkai", font_size=28, color=PINK),
            Text("• 印度贫寒家庭出身", color=PINK, font_size=24),
            Text("• 受哈代邀请赴剑桥", color=PINK, font_size=24),
            Text("• 因战争与饮食不适患病", color=PINK, font_size=24),
            Text("• 返回印度后病逝", color=PINK, font_size=24)
        )
        
        # 排列贡献列表为三列 - 调整间距
        column1 = VGroup(*contributions[0:5])
        column1.arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(LEFT*4 + UP*0.2)  # 减小水平和垂直偏移
        
        column2 = VGroup(*contributions[5:10])
        column2.arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(UP*0.2)
        
        column3 = VGroup(*contributions[10:])
        column3.arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(RIGHT*4 + UP*0.2)
        
        # 动画展示标题
        self.add(title, underline)
        self.wait(0.5)
        
        # 动画展示贡献列表
        self.play(FadeIn(column1, shift=RIGHT))
        self.play(FadeIn(column2, shift=RIGHT))
        self.play(FadeIn(column3, shift=RIGHT))
        self.wait(1)
        
        # 添加最终强调
        final_text = Text("数学人才：人类思想的伟大结晶", 
                        font="Microsoft YaHei", 
                        font_size=36,  # 减小字号
                        color=RED)
        final_text.to_edge(DOWN, buff=0.5)  # 增加底部边距
        
        # 添加装饰框 - 减小缓冲
        box = SurroundingRectangle(
            VGroup(column1, column2, column3),
            buff=0.3,  # 减小缓冲
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
        
# manim -pqh 年轻数学家.py MultiImage