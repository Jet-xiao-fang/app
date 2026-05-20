from manim import *

class LogoScene(Scene):
    """带左上角 Logo 的基础场景"""
    
    def add_logo(self,
                 text="TheMathFlow",
                 font="Microsoft YaHei",
                 font_size=18,
                 color=GREY_D,                # 灰色文字
                 stroke_color=WHITE,        # 白色描边
                 stroke_width=0.5,            # 描边宽度
                 corner=UL,
                 buff=0.5,
                 animate=False):
        """
        在场景左上角添加个人 Logo（无背景框，带白色描边）
        
        参数:
            text: Logo 文字
            font: 字体
            font_size: 字号
            color: 文字颜色（灰色）
            stroke_color: 描边颜色（白色）
            stroke_width: 描边宽度
            corner: 位置角 (UL, UR, DL, DR)
            buff: 距边缘距离
            animate: 是否使用淡入动画
        """
        # 主文字
        logo_text = Text(text, font=font, font_size=font_size, color=color, weight=BOLD)
        logo_text.set_stroke(color=stroke_color, width=stroke_width)
        logo_text.to_corner(corner, buff=buff)
        
        self.logo_group = logo_text
        
        if animate:
            self.play(FadeIn(self.logo_group, shift=RIGHT * 0.2), run_time=0.8)
        else:
            self.add(self.logo_group)
        
        return self.logo_group