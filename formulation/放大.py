from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class PanningImageEffect(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # 加载图片（保持原始大小）
        img = ImageMobject(r"D:\Videos\图片素材\会议.jpg")
        img.scale(1)  # 保持原始尺寸
        img.move_to(ORIGIN)
        
        # 预先创建科学家的介绍文字
        scientists_down_text = Group(
            # 前排科学家
            Tex("\\text{前排}{\\small（权威元老）}", font_size=32, color=YELLOW),
            Tex("\\text{爱因斯坦（居中）:} 相对论创始人，1921年诺贝尔物理学奖得主", font_size=25),
            Tex("\\text{居里夫人（唯一女性）:} 唯一两度获诺贝尔奖（物理+化学）的女性科学家", font_size=25),
            Tex("\\text{普朗克（爱因斯坦左侧）:} 量子论奠基人，1918年诺贝尔奖得主", font_size=25),
            Tex("\\text{洛伦兹（爱因斯坦右侧）:} 提出「洛伦兹变换」，狭义相对论数学基础奠基人", font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        scientists_up_text = Group(
             # 中排科学家
            Tex("\\text{中排}{\\small（量子力学领袖）}", font_size=32, color=RED),
            Tex("\\text{玻尔（中排右一）:} 哥本哈根学派领袖，与爱因斯坦激烈论战", font_size=25),
            Tex("\\text{薛定谔（中排左五）:} 波动力学创始人，以「薛定谔的猫」思想实验闻名", font_size=25),
            Tex("\\text{狄拉克（中排左四）:} 预言反物质，1933年诺贝尔奖得主（爱因斯坦正后方）", font_size=25),
            Tex("\\text{德布罗意（中排左六）:} 物质波理论提出者，首位以博士论文获诺奖的学者", font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # 将文字组放置在图片下方适当位置
        scientists_down_text.next_to(img, DOWN, buff=0.7).to_edge(LEFT, buff=0.3)
        scientists_up_text.next_to(img, UP, buff=0.7).to_edge(LEFT, buff=0.3)
        
        # 初始状态：图片和文字同时淡入
        self.play(
            FadeIn(img, shift=UP*0.3, scale=0.9, run_time=1.5),
            FadeIn(scientists_up_text, shift=DOWN*0.3, scale=1.1, run_time=1.5),
            FadeIn(scientists_down_text, shift=DOWN*0.3, scale=1.1, run_time=1.5),
        )
        self.wait(1)
        
        # 计算需要移动的距离
        frame_width = config.frame_width
        img_width = img.get_width()
        pan_distance = (img_width - frame_width)/2 * 1.1
        
        # 1. 向左移动展示图片右侧（被遮挡的部分）
        # 注意：文字保持不动，只有图片移动
        self.play(
            ApplyMethod(
                img.shift, LEFT * pan_distance,
                rate_func=smooth,
                run_time=6  # 缓慢移动
            )
        )
        self.wait(0.5)
        
        # 2. 向右移动展示图片左侧（被遮挡的部分）
        self.play(
            ApplyMethod(
                img.shift, RIGHT * pan_distance * 2,  # 向右移动到右侧极限
                rate_func=smooth,
                run_time=8  # 更慢的速度
            )
        )
        self.wait(0.5)
        
        # 3. 缓慢移回中心位置
        self.play(
            ApplyMethod(
                img.shift, LEFT * pan_distance,  # 移回中心
                rate_func=smooth,
                run_time=2
            )
        )
        
        # 4. 在原位置放大1.2倍
        # 文字仍保持不动
        self.play(
            ApplyMethod(
                img.scale, 1.2,  # 放大1.2倍
                about_point=img.get_center(),  # 围绕中心点放大
                rate_func=smooth,
                run_time=3  # 慢慢放大
            )
        )
        self.wait(1)  # 保持放大状态1秒
        
        # 5. 高亮爱因斯坦的名字（作为示例）
        einstein_line = scientists_down_text[1]
        highlight_box = SurroundingRectangle(einstein_line, buff=0.2, 
                                            fill_color=YELLOW_E, fill_opacity=0.2, 
                                            stroke_color=YELLOW, stroke_width=2)
        
        self.play(
            FadeIn(highlight_box, scale=0.8),
            einstein_line.animate.set_color(YELLOW),
            run_time=1.2
        )
        self.wait(1)
        
        # 移除高亮
        self.play(
            FadeOut(highlight_box, scale=1.1),
            einstein_line.animate.set_color(WHITE),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 6. 文字和图片一起淡出
        self.play(
            FadeOut(scientists_up_text, shift=DOWN*0.2, scale=0.9, run_time=2),
            FadeOut(scientists_down_text, shift=DOWN*0.2, scale=0.9, run_time=2),
            FadeOut(img, shift=UP*0.5, scale=1.2, run_time=2)
        )
        self.wait(1)