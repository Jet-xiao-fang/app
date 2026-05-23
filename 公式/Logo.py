from manim import *
from starfield import add_logo as _add_logo


class LogoScene(Scene):
    """带左上角 Logo 的基础场景"""

    def add_logo(self,
                 text="TheMathFlow",
                 font="Microsoft YaHei",
                 font_size=18,
                 color=GREY_D,
                 stroke_color=WHITE,
                 stroke_width=0.5,
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
        return _add_logo(self, text=text, font=font, font_size=font_size,
                         color=color, stroke_color=stroke_color,
                         stroke_width=stroke_width, corner=corner,
                         buff=buff, animate=animate)