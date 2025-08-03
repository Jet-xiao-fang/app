from manim import *

class MovieCreditRoll(Scene):
    def construct(self):
        # ===== 1. 配置参数 =====
        lines = [
            "淞沪抗战参战部队番号",
            '<span color="YELLOW">上海地方部队：</span>上海市保安总团、上海市警察总队',
            "江苏部队：江苏省保安部队",
        ]
        font_size = 30  # 稍微增大字体大小
        line_spacing = 0.6  # 调整行间距

        # ===== 2. 创建字幕组 =====
        credits = VGroup()
        
        for i, text in enumerate(lines):
            if i == 0:
                line = MarkupText(text, font="Source Han Sans CN", font_size=48,color=RED)
            else:
                line = MarkupText(text, font="Source Han Sans CN", font_size=font_size)
            
            credits.add(line)
        credits.arrange(DOWN,buff=line_spacing,aligned_edge=ORIGIN)
        #credits.set_y(start_y)
        # 将整个字幕组移动到屏幕底部下方
        credits.move_to(DOWN * (config.frame_height / 2 + credits.get_height() / 2 + 1))
        # ===== 3. 滚动动画 =====
        # 计算滚动距离（整个字幕组高度 + 屏幕高度）
        target_y = credits.get_height() + config.frame_height+1
        
        self.play(
            credits.animate.shift(UP * target_y),
            run_time=6,
            rate_func=linear
        )
        self.wait(2)
    
# manim -pqh 历史.py MovieCreditRoll