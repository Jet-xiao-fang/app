from manim import *

class GroupedGreekLetters(Scene):
    def construct(self):
        # ==========================================
        # 1. 数据准备：将14个字母按数学功能分为3组
        # ==========================================
        groups_data = [
            {
                "title": "第一组：角度与几何",
                "letters": [
                    (r"\alpha",   "Alpha / 阿尔法"),
                    (r"\beta",    "Beta / 贝塔"),
                    (r"\gamma",   "Gamma / 伽马"),
                    (r"\theta",   "Theta / 西塔"),
                    (r"\phi",     "Phi / 斐 (黄金分割/立体角)"),
                ]
            },
            {
                "title": "第二组：微积分与分析",
                "letters": [
                    (r"\epsilon", "Epsilon / 艾普西龙 (极限)"),
                    (r"\delta",   "Delta / 德尔塔 (变化量)"),
                    (r"\pi",      "Pi / 派 (圆周率)"),
                    (r"\tau",     "Tau / 陶 (2π)"),
                ]
            },
            {
                "title": "第三组：代数、统计与特殊",
                "letters": [
                    (r"\lambda",  "Lambda / 拉姆达 (特征值)"),
                    (r"\mu",      "Mu / 缪 (均值)"),
                    (r"\sigma",   "Sigma / 西格马 (标准差/求和)"),
                    (r"\omega",   "Omega / 奥米伽 (角速度/样本空间)"),
                    (r"\xi",      "Xi / 克赛 (随机变量)"),
                ]
            }
        ]

        # ==========================================
        # 2. UI 元素准备：背景板与标题
        # ==========================================
        background_rect = Rectangle(
            width=12, height=7, 
            fill_color=BLACK, fill_opacity=0.8, 
            stroke_width=0
        )
        self.add(background_rect)

        # 标题：先居中展示
        main_title = Text("数学中常见的 14 个希腊字母", font="SimHei", font_size=40, color=BLUE)
        main_title.move_to(ORIGIN)  # 初始居中
        self.play(Write(main_title))
        
        # 标题向上移动并固定
        self.play(main_title.animate.to_edge(UP, buff=0.3), run_time=0.5)
        self.wait(0.5)
        
        for group_info in groups_data:
            # --- 3.1 生成组内每行的 VGroup ---
            rows = []
            for latex_code, desc in group_info["letters"]:
                # 字母本身 (MathTex，增大字体)
                letter_sym = MathTex(latex_code, color=YELLOW, font_size=56)  # 从48增大到56
                # 读法与含义 (Text，白色，略微增大)
                letter_desc = Text(desc, font="SimHei", font_size=34, color=WHITE)  # 从32增大到34
                
                # 组合成一行，左符号，右文字
                row = VGroup(letter_sym, letter_desc).arrange(RIGHT, buff=1)
                rows.append(row)

            # 将所有行垂直排列成一组
            group_vgroup = VGroup(*rows).arrange(DOWN, buff=0.4)
            group_vgroup.move_to(ORIGIN + DOWN * 0.2)

            # --- 3.2 生成当前组的副标题 ---
            sub_title = Text(group_info["title"], font="SimHei", font_size=36, color=TEAL_A)
            sub_title.next_to(group_vgroup, UP, buff=0.5)

            # --- 3.3 入场动画 ---
            self.play(Write(sub_title), run_time=0.8)
            
            # 逐行出现
            for row in rows:
                self.play(
                    FadeIn(row, shift=LEFT * 0.5),
                    run_time=0.3
                )
            
            self.wait(2.5)
            
            # --- 3.4 出场动画 ---
            self.play(
                Unwrite(sub_title),
                *[FadeOut(row, shift=DOWN * 0.3) for row in rows],
                run_time=1
            )
            self.wait(0.5)

        # ==========================================
        # 4. 结尾动画（集体展示，符号进一步增大）
        # ==========================================
        all_symbols = MathTex(
            r"\alpha \quad \beta \quad \gamma \quad \delta \quad \epsilon \quad \theta \quad \lambda \quad \mu \quad \pi \quad \sigma \quad \tau \quad \phi \quad \omega \quad \xi",
            font_size=48, color=YELLOW  # 从36增大到48
        )
        all_symbols.move_to(ORIGIN)
        
        self.play(main_title.animate.set_color(WHITE))
        self.play(FadeIn(all_symbols, shift=UP), run_time=2)
        self.wait(2)
        
        self.play(FadeOut(VGroup(main_title, background_rect, all_symbols)))
    
#    manim -pqh 常见的数学符号.py GroupedGreekLetters