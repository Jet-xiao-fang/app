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

        items=[("D:\Videos\图片素材\欧拉","欧拉公式"),
               ("D:\Videos\图片素材\高斯","高斯公式"),
               ("D:\Videos\图片素材\拉马","拉马努金公式")]

        groups = Group()
        
        # 创建所有元素并设置初始位置（屏幕左侧外）
        for img_path, text_str in items:
            img = ImageMobject(img_path).scale(image_scale)
            text = Text(text_str, font_size=text_font_size, font="SimHei")
            group = Group(img, text).arrange(RIGHT, buff=0.3)
            group.shift(LEFT * self.camera.frame_width)  # 初始位置在屏幕左侧外
            groups.add(group)
        
        # 设置每组的目标位置（垂直排列）
        groups.arrange(DOWN, buff=group_buff).center()
        
        # 创建从左向右滑动的动画序列
        animations = []
        for group in groups:
            animations.append(group.animate.shift(RIGHT * self.camera.frame_width))
        
        # 播放带延迟的滑动动画
        self.play(LaggedStart(
            *animations,
            lag_ratio=0.4,  # 控制每组动画的间隔时间
            run_time=2      # 每组动画持续时间
        ))
        self.wait(2)

# manim -pqh --format=png 微积分公式.py MultiImage -r 1920,1080