from manim import *

class MultiImage(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        # 1. 创建标题
        title = Text("不同的求π公式", 
                    font="Microsoft YaHei",
                    font_size=26,
                    color=BLUE).to_edge(UP)
        self.play(Write(title))
        image_scale = 0.3
        group_buff = 0.5
        text_font_size = 32

        items=[("D:\Videos\图片素材\欧拉","描述文本1"),
               ("D:\Videos\图片素材\高斯","描述文本2"),
               ("D:\Videos\图片素材\拉马","描述文本3")]

        groups = Group()
        
        for img_path,text_str in items:
            img = ImageMobject(img_path).scale(image_scale)
            text= Text(text_str,font_size=text_font_size,font="SimHei")
            group = Group(img,text).arrange(RIGHT,buff=0.3)
            groups.add(group)
        groups.arrange(DOWN,buff=group_buff).center()

        self.play(LaggedStart(*[FadeIn(group,scale = 0.7) for group in groups],lag_ratio=1.5))
        self.wait(2)

# manim -pqh --format=png 头像公式.py MultiImage -r 1920,1080

        