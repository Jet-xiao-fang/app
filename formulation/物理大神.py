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
        title = Text("量子力学奠基人之一", font_size=48, color=YELLOW).to_edge(UP,buff=1.5)
        self.add(title)
        self.wait(0.5)
        
        # 数学家图片和符号信息
        mathematicians = [
            {
                "name": "爱因斯坦",
                "image": r"D:\Videos\图片素材\爱因斯坦.jpeg",
                "symbols": [
                    (r"E = h\nu", "光量子假说 (1905)"), 
                    (r"E_k = h\nu - W", "光电效应方程 (1905)"),
                    (r"\Delta E = \Delta m c^2", "质能方程 (1905)")
                ],
                "color": YELLOW
            },
            {
                "name": "薛定谔",
                "image": r"D:\Videos\图片素材\薛定谔.jpg",
                "symbols": [
                    (r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi", "含时薛定谔方程 (1926)"), 
                    (r"-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi", "定态薛定谔方程 (1926)"),
                    (r"P = |\Psi|^2", "波函数概率诠释 (1926)")
                ],
                "color": RED_C
            },
            {
                "name": "海森堡",
                "image": r"D:\Videos\图片素材\海森堡2.jpg",
                "symbols": [
                    (r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", "不确定性原理 (1927)"), 
                    (r"\left[ \hat{Q}, \hat{P} \right] = i\hbar", "矩阵力学对易关系 (1925)"),
                    (r"E_n = \langle n|\hat{H}|n \rangle", "能量本征值矩阵表示 (1925)")
                ],
                "color": BLUE
            },
            {
                "name": "狄拉克",
                "image": r"D:\Videos\图片素材\狄拉克.jpeg",
                "symbols": [
                    (r"(i\gamma^\mu\partial_\mu - m)\psi = 0", "狄拉克方程 (1928)"), 
                    (r"\langle \phi | \psi \rangle", "狄拉克符号（左矢右矢）(1939)"),
                    (r"E = \pm \sqrt{p^2c^2 + m^2c^4}", "反粒子解 (1928)")
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
                img.scale(0.3)
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
            group = Group(img, content_group).arrange(RIGHT, buff=0.5)
            
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
        final_text = Text("量子力学：人类思想的伟大结晶", 
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
        
# manim -pqh 物理大神.py MathSymbolsScene -r 1920,1080