from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class GroupedGreekLetters(Scene):
    def construct(self):
        # ==========================================
        # 0. 设置美观的背景（渐变 + 网格）- 兼容 manim 0.20.0
        # ==========================================

        # 0.1 创建全屏渐变背景（从上到下：深紫 -> 深蓝）
        gradient_bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            stroke_width=1,
        )
        
        self.add(gradient_bg)  # 最先添加，位于最底层

        # 0.2 添加半透明网格，增加科技感（不会干扰文字阅读）
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-4.5, 4.5, 1],
            background_line_style={"stroke_color": "#546E7A", "stroke_width": 1, "stroke_opacity": 0.6},
            axis_config={"color": "#ECEFF1","stroke_opacity": 0}
            
        )
        self.add(grid)

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

        # 标题：先居中展示
        main_title = Tex(r"数学中常见的$14$个希腊字母", font_size=48, color=BLUE)
        main_title.move_to(ORIGIN)  # 初始居中
        self.play(Write(main_title))

        # 标题向上移动并固定
        self.play(main_title.animate.to_edge(UP, buff=0.5), run_time=0.5)
        self.wait(0.5)

        for group_info in groups_data:
            # --- 3.1 生成组内每行的 VGroup ---
            rows = []
            for latex_code, desc in group_info["letters"]:
                # 字母本身 (MathTex，增大字体)
                letter_sym = MathTex(latex_code, font_size=56,color=RED)
                # 读法与含义 (Text，白色，略微增大)
                letter_desc = Text(desc, font_size=34, color=WHITE)

                # 组合成一行，左符号，右文字
                row = VGroup(letter_sym, letter_desc).arrange(RIGHT, buff=1)
                rows.append(row)

            # 将所有行垂直排列成一组
            group_vgroup = VGroup(*rows).arrange(DOWN, buff=0.6)
            group_vgroup.move_to(ORIGIN + DOWN * 0.8)

            # --- 3.2 生成当前组的副标题 ---
            sub_title = Text(group_info["title"], font_size=32, color=TEAL_A)
            sub_title.next_to(main_title, DOWN, buff=0.5)

            # --- 3.3 入场动画 ---
            self.play(Write(sub_title), run_time=0.8)

            # 逐行出现
            for row in rows:
                self.play(
                    FadeIn(row, shift=LEFT * 0.5),
                    run_time=0.5
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
            font_size=48
        )
        all_symbols.move_to(ORIGIN)
        self.add(all_symbols)
        self.wait(3)
        