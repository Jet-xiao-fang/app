from manim import *

class MovieCreditRoll(Scene):
    def construct(self):
        # ===== 1. 配置参数 =====
        lines = [
            "淞沪抗战参战部队番号",
            '<span color="YELLOW">上海地方部队：</span>上海市保安总团、上海市警察总队',
            '<span color="YELLOW">江苏部队：</span>江苏省保安部队',
            '<span color="YELLOW">西北军：</span>第32、33师',
            '<span color="YELLOW">东北军：</span>',
            "第105师、106师、107师、108师、109师、111师、112师、120师",
            '<span color="YELLOW">福建部队：</span>第52师',
            '<span color="YELLOW">四川部队：</span>',
            "第26师、133师、134师、135师、144师、145师、146师",
            "第147师、148师、独第13旅、独14旅",
            '<span color="YELLOW">贵州部队：</span>第102师、103师、121师、独立第34旅',
            '<span color="YELLOW">广西部队：</span>第170师、171师、172师、173师、174师、176师',
            '<span color="YELLOW">湖北部队：</span>第13师、79师、167师',
            '<span color="YELLOW">河南部队：</span>第40师、45师',
            '<span color="YELLOW">湖南部队：</span>',
            "预第11师、15师、16师、18师、19师、23师、46师、53师",
            "62师、63师、77师、128师、暂编第11旅、暂编第12旅",
            "暂编第13旅、独立第37旅",
            '<span color="YELLOW">广东部队：</span>第59师、90师、154师、156师、159师、160师、66军教导旅',
            '<span color="YELLOW">安徽部队：</span>第44师、55师、56师、57师',
            '<span color="YELLOW">中央军：</span>',
            "第1师、3师、6师、8师、9师、11师、14师、36师",
            "51师、58师、60师、61师、67师、78师、87师、88师、98师",
            "炮第2团、炮3团、炮4团、炮8团、炮16团、炮42团",
            "重炮第10团、财政部税警总团、中央军校教导总队、宪兵10团",
            "空军第210大队、海军第1、2舰队、练习舰队、鱼雷快艇大队",
            "—— 致敬 ——",
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
            run_time=28,
            rate_func=linear
        )
        self.wait(2)
    
# manim -pqh 抖音字幕流.py MovieCreditRoll