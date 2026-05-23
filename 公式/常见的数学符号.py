from manim import *
from starfield import create_starfield, add_logo

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex


class GroupedGreekLetters(Scene):
    def construct(self):
        self.camera.background_color = "#020212"
        self.add(create_starfield(n_stars=100))

        # ==========================================
        # 1. 数据准备
        # ==========================================

        # 每组配色：主色 + 每个字母的独立颜色
        groups_data = [
            {
                "title": "角度与几何",
                "theme_color": GOLD,
                "underline_color": YELLOW_E,
                "letters": [
                    (r"\alpha",  "Alpha / 阿尔法",            GOLD),
                    (r"\beta",   "Beta / 贝塔",               ORANGE),
                    (r"\gamma",  "Gamma / 伽马",              YELLOW),
                    (r"\theta",  "Theta / 西塔",              GOLD_C),
                    (r"\phi",    "Phi / 斐 (黄金分割/立体角)", GOLD_D),
                ]
            },
            {
                "title": "微积分与分析",
                "theme_color": GREEN,
                "underline_color": GREEN_B,
                "letters": [
                    (r"\epsilon", "Epsilon / 艾普西龙 (极限)", GREEN_C),
                    (r"\delta",   "Delta / 德尔塔 (变化量)",   TEAL),
                    (r"\pi",      "Pi / 派 (圆周率)",          PURE_GREEN),
                    (r"\tau",     "Tau / 陶 (2π)",             GREEN_E),
                ]
            },
            {
                "title": "代数、统计与特殊",
                "theme_color": BLUE,
                "underline_color": BLUE_C,
                "letters": [
                    (r"\lambda",  "Lambda / 拉姆达 (特征值)",      PINK),
                    (r"\mu",      "Mu / 缪 (均值)",                 PURPLE),
                    (r"\sigma",   "Sigma / 西格马 (标准差/求和)",   BLUE_C),
                    (r"\omega",   "Omega / 奥米伽 (角速度/样本空间)", MAROON_C),
                    (r"\xi",      "Xi / 克赛 (随机变量)",           ORANGE),
                ]
            }
        ]

        # ==========================================
        # 2. 标题动画（居中弹出 → 升至顶部）
        # ==========================================

        main_title = Tex(
            r"数学中常见的$14$个希腊字母",
            font_size=48, color=GOLD
        )
        main_title.move_to(ORIGIN)
        self.play(
            FadeIn(main_title, scale=1.3, shift=DOWN * 0.3),
            run_time=0.8
        )
        self.play(main_title.animate.to_edge(UP, buff=0.6), run_time=0.6)

        underline = Line(
            LEFT * 4, RIGHT * 4,
            color=GOLD, stroke_width=2
        )
        underline.next_to(main_title, DOWN, buff=0.2)
        self.play(Create(underline), run_time=0.8)

        add_logo(self, animate=True)

        # ==========================================
        # 3. 分组展示
        # ==========================================

        for idx, group_info in enumerate(groups_data):
            theme_color = group_info["theme_color"]

            # --- 3.1 副标题 ---
            sub_title = Text(
                group_info["title"],
                font="Microsoft YaHei",
                font_size=34,
                color=theme_color,
                weight=BOLD,
            )
            sub_title.next_to(underline, DOWN, buff=0.5)

            sub_underline = Line(
                LEFT * 2.5, RIGHT * 2.5,
                color=group_info["underline_color"],
                stroke_width=1.5,
            )
            sub_underline.next_to(sub_title, DOWN, buff=0.15)

            self.play(
                FadeIn(sub_title, shift=UP * 0.2),
                Create(sub_underline),
                run_time=0.7
            )

            # --- 3.2 构建行 ---
            rows = []
            for latex_code, desc, letter_color in group_info["letters"]:
                letter_sym = MathTex(latex_code, font_size=60, color=letter_color)
                letter_desc = Text(
                    desc,
                    font="Microsoft YaHei",
                    font_size=30,
                    color=WHITE,
                )

                row = VGroup(letter_sym, letter_desc).arrange(RIGHT, buff=1.2)

                bg_rect = BackgroundRectangle(
                    row,
                    buff=0.35,
                    fill_opacity=0.12,
                    fill_color=theme_color,
                    stroke_opacity=0,
                )
                row_with_bg = VGroup(bg_rect, row)
                rows.append(row_with_bg)

            group_vgroup = VGroup(*rows).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            group_vgroup.next_to(sub_underline, DOWN, buff=0.6)

            # --- 3.3 逐行入场 ---
            for row in rows:
                self.play(
                    FadeIn(row, scale=1.15, shift=RIGHT * 0.4),
                    run_time=0.55
                )

            self.wait(0.5)

            # --- 3.4 出场 ---
            self.play(
                FadeOut(sub_title, shift=UP * 0.2),
                FadeOut(sub_underline),
                *[FadeOut(row, scale=0.95, shift=DOWN * 0.3) for row in rows],
                run_time=1.0
            )
            self.wait(0.3)

        # 收掉标题与底线，为结尾展示腾出空间
        self.play(
            FadeOut(main_title, shift=UP * 0.3),
            FadeOut(underline),
            run_time=0.6
        )

        # ==========================================
        # 4. 结尾展示：符号围成圆环 ✦
        # ==========================================

        all_group_symbols = VGroup()
        for group_info in groups_data:
            for latex_code, desc, letter_color in group_info["letters"]:
                sym = MathTex(latex_code, font_size=52, color=letter_color)
                all_group_symbols.add(sym)

        n = len(all_group_symbols)
        radius = 3.0
        y_shift = 0.3

        for i, sym in enumerate(all_group_symbols):
            angle = i * TAU / n - PI / 2
            sym.move_to(
                np.array([radius * np.cos(angle), y_shift + radius * np.sin(angle), 0])
            )

        # 轨道光圈
        ring = Annulus(
            inner_radius=radius - 0.2,
            outer_radius=radius + 0.2,
            color=GOLD,
            fill_opacity=0.04,
            stroke_opacity=0.3,
        )
        ring.shift(UP * y_shift)

        # 中心装饰
        center_glow = Circle(
            radius=1.0,
            fill_color=GOLD,
            fill_opacity=0.08,
            stroke_color=GOLD,
            stroke_width=1.5,
        )
        center_glow.shift(UP * y_shift)
        center_text = MathTex(r"\Sigma", font_size=64, color=GOLD)
        center_text.set_opacity(0.6)
        center_text.shift(UP * y_shift)

        self.play(
            Create(ring),
            FadeIn(VGroup(center_glow, center_text), scale=1.5),
            run_time=1.0
        )
        self.play(
            LaggedStart(
                *[FadeIn(sym, scale=1.5, shift=sym.get_center() * 0.3)
                  for sym in all_group_symbols],
                lag_ratio=0.06,
            ),
            run_time=2.5
        )

        # 呼吸动画：符号微微缩放
        self.play(
            LaggedStart(
                *[ApplyMethod(sym.scale, 1.08, rate_func=there_and_back)
                  for sym in all_group_symbols],
                lag_ratio=0.03,
            ),
            run_time=2
        )
        ring.set_stroke(opacity=0.6)
        self.wait(0.5)

# manim -pqh 常见的数学符号.py GroupedGreekLetters
