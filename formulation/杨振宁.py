from manim import *
import random

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class YangGallery(Scene):
    def construct(self):
        # 设置星空背景
        self.camera.background_color = "#0F0F1A"
        stars = VGroup(*[Dot(color=WHITE, radius=0.05).shift(5*random.uniform(-5,5)*RIGHT + 5*random.uniform(-3,3)*UP) for _ in range(100)])
        self.add(stars)
        
        # 动态标题设计
        title = Text("物理学大师杨振宁", 
                    font="Microsoft YaHei", 
                    font_size=48, 
                    color=BLUE_C,
                    weight=BOLD)
        title.set_color_by_gradient(BLUE_A, BLUE_D)
        title_box = SurroundingRectangle(title, color=BLUE_E, corner_radius=0.2, buff=0.4)
        title_box.set_fill(BLACK, opacity=0.7)
        title_group = VGroup(title_box, title).to_edge(UP, buff=0.5)
        self.play(DrawBorderThenFill(title_box), Write(title), run_time=1.5)
        self.wait(0.5)

        # 加载四张图片（替换为你的实际路径）
        img_paths = [
            r"D:\Videos\图片素材\杨.jpeg",
            r"D:\Videos\图片素材\杨2.jpg",
            r"D:\Videos\图片素材\杨和费.jpg",
            r"D:\Videos\图片素材\杨3.jpeg"
        ]
        
        # 图片说明文字
        captions = [
            "杨振宁肖像（青年时期）",
            "诺贝尔奖颁奖典礼（1957）",
            "与费米实验室学者交流",
            "在清华大学授课场景"
        ]
        
        # 依次展示四张图片
        for i in range(4):
            # 创建图片对象
            img = ImageMobject(img_paths[i])
            
            # 设置图片宽度占满屏幕，同时保持原始比例
            # 计算目标宽度（留出左右边距）
            target_width = config.frame_width - 0.5  # 留出0.25单位的左右边距
            img.set_width(target_width)
            
            # 计算垂直位置（考虑标题和说明文字的空间）
            top_margin = config.frame_height/2 - 3  # 标题下方留出空间
            img.move_to(UP * (top_margin - img.get_height()/2))
            
            # 创建说明文字
            caption = Text(captions[i], 
                          font="Microsoft YaHei", 
                          font_size=32)
            # 文字放在图片下方
            caption.next_to(img, DOWN, buff=0.3)
            
            # 添加相框 - 宽度与图片相同
            frame = SurroundingRectangle(
                img, 
                color=BLUE_E, 
                buff=0.1, 
                stroke_width=3,
                corner_radius=0.1
            )
            frame.set_fill(BLACK, opacity=0)
            
            # 使用Group组合
            group = Group(img, frame, caption)
            
            # 先添加图片和相框到场景
            self.add(img, frame)
            
            # 淡入显示图片和相框
            self.play(
                FadeIn(img),
                FadeIn(frame),
                run_time=1
            )
            
            # 淡入显示文字
            self.play(
                FadeIn(caption, shift=UP),
                run_time=1
            )
            
            # 显示2秒
            self.wait(2)
            
            # 淡出图片（最后一张除外）
            if i < 3:
                # 淡出整个组
                self.play(
                    FadeOut(group),
                    run_time=1
                )
            else:
                # 保存最后一张图片的组
                last_group = group
        
        # 添加结语
        quote = Text("物理学的本质在于创新与探索", 
                    font="Microsoft YaHei", 
                    font_size=36,
                    color=BLUE_B)
        quote_box = SurroundingRectangle(quote, color=BLUE_D, buff=0.4)
        quote_box.set_fill(BLACK, opacity=0.8)
        
        # 将结语放在最后一张图片的下方
        quote_group = VGroup(quote_box, quote)
        quote_group.next_to(last_group, DOWN, buff=1)
        
        self.play(
            FadeIn(quote_group, shift=UP),
            run_time=1.5
        )
        self.wait(3)
        
        # 星空淡出效果
        self.play(
            FadeOut(Group(*self.mobjects)),
            run_time=2
        )
# manim -pqh --format=png 杨振宁.py YangGallery -r 1920,1080
