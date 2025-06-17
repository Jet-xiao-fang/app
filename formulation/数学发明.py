from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class MathSymbolsScene(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0F0F1A"
        
        # 标题
        title = Text("数学符号发明人", font="Microsoft YaHei", font_size=48, color=BLUE)
        self.play(Write(title.to_edge(UP, buff=0.9)))
        self.wait(1)
        
        # 数学家图片和符号信息
        mathematicians = [
            {
                "name": "莱布尼茨",
                "image": r"D:\Videos\图片素材\莱布尼茨.jpg",
                "symbols": [
                    (r"\int", "积分符号 (1675年)"),
                    (r"\frac{d}{dx}", "微分符号"),
                    (r"=", "等号")
                ],
                "color": YELLOW
            },
            {
                "name": "欧拉",
                "image": r"D:\Videos\图片素材\欧拉.jpeg",
                "symbols": [
                    (r"e", "自然常数 (1736年)"),
                    (r"i", "虚数单位"),
                    (r"\sum", "求和符号"),
                    (r"f(x)", "函数表示法")
                ],
                "color": RED_C
            },
            {
                "name": "高斯",
                "image": r"D:\Videos\图片素材\高斯.jpeg",
                "symbols": [
                    (r"\equiv", "同余符号"),
                    (r"\bmod", "模运算符号"),
                    (r"i", "复数单位")
                ],
                "color": BLUE
            },
            {
                "name": "牛顿",
                "image": r"D:\Videos\图片素材\牛顿.jpeg",
                "symbols": [
                    (r"\dot{x}", "流数记号 (导数)"),
                    (r"\binom{n}{k}", "二项式系数"),
                    (r"\infty", "无穷大符号")
                ],
                "color": PINK
            }
        ]
        
        # 创建并展示每位数学家
        groups = Group()
        y_positions = [4, 1, -2, -5]
        for i, math_info in enumerate(mathematicians):
            # 加载图片
            img = ImageMobject(math_info["image"])
            if i == 0:
                img.scale(0.5)
            else:
                img.scale(0.2)
            
            # 创建符号组
            symbol_group = VGroup()
            for j, (symbol, desc) in enumerate(math_info["symbols"]):
                sym = MathTex(symbol, font_size=26, color=math_info["color"])
                txt = Text(desc, font="Microsoft YaHei", font_size=20, color=WHITE)
                group = VGroup(sym, txt).arrange(RIGHT, buff=0.2)
                symbol_group.add(group)
            
            symbol_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            
            # 数学家名字
            name_text = Text(math_info["name"], font="Microsoft YaHei", 
                            font_size=32, color=math_info["color"])
            
            # 整体组合
            content_group = VGroup(name_text, symbol_group).arrange(DOWN, buff=0.5)
            group = Group(img, content_group).arrange(RIGHT, buff=1)
            
            # 垂直位置
            # group.shift(UP * (1.5 - i * 2.5))
            group.move_to(y_positions[i] * UP)
            
            # 添加到场景
            self.play(
                FadeIn(img, shift=RIGHT),
                Write(content_group, shift=LEFT),
                run_time=1.5
            )
            self.wait(1)
            groups.add(group)
        
        # 最终文本
        final_text = Text("数学符号：人类思想的伟大结晶", 
                         font="Microsoft YaHei", font_size=30, color=GOLD)
        self.play(Write(final_text.to_edge(DOWN, buff=0.5)))
        self.wait(3)
        
        # 结束动画
        self.play(
            groups.animate.scale(0.8).shift(UP*0.5),
            final_text.animate.scale(1.2).set_color(RED),
            run_time=2
        )
        self.wait(2)