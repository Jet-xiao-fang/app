from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class GroupedGreekLetters(Scene):
    def construct(self):
        
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
                    (r"\alpha",  "阿尔法",            GOLD),
                    (r"\beta",   "贝塔",               ORANGE),
                    (r"\gamma",  "伽马",              YELLOW),
                    (r"\theta",  "西塔",              GOLD_C),
                    (r"\phi",    "斐", GOLD_D),
                ]
            },
            {
                "title": "微积分与分析",
                "theme_color": GREEN,
                "underline_color": GREEN_B,
                "letters": [
                    (r"\epsilon", "艾普西龙", GREEN_C),
                    (r"\delta",   "德尔塔",   TEAL),
                    (r"\pi",      "派",          PURE_GREEN),
                    (r"\tau",     "陶",             GREEN_E),
                ]
            },
            {
                "title": "代数、统计与特殊",
                "theme_color": BLUE,
                "underline_color": BLUE_C,
                "letters": [
                    (r"\lambda",  "拉姆达",      PINK),
                    (r"\mu",      "缪",                 PURPLE),
                    (r"\sigma",   "西格马",   BLUE_C),
                    (r"\omega",   "奥米伽", MAROON_C),
                    (r"\xi",      "克赛",           ORANGE),
                ]
            }
        ]

        # ==========================================
        # 2. 标题动画（居中弹出 → 升至顶部）
        # ==========================================

        main_title = Tex(
            r"数学中常见的$14$个希腊字母",
            font_size=48, color=BLUE
        ).scale(1.5)
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

        # ==========================================
        # 3. 逐个展示符号
        # ==========================================

        all_letters = []
        for group_info in groups_data:
            all_letters.extend(group_info["letters"])

        first_sym = MathTex(all_letters[0][0], font_size=80, color=WHITE).scale(2)
        first_sym.move_to(ORIGIN)

        first_desc = Text(
            all_letters[0][1],
            font="STXingkai",
            font_size=34,
            color=TEAL,
        ).scale(1.5)
        first_desc.next_to(first_sym, DOWN, buff=0.8)

        self.play(
            FadeIn(first_sym, scale=1.5),
            FadeIn(first_desc, shift=UP * 0.2),
            run_time=0.6
        )

        old_sym = first_sym
        old_desc = first_desc

        for latex_code, desc, _ in all_letters[1:]:
            new_sym = MathTex(latex_code, font_size=80, color=WHITE).scale(2)
            new_sym.move_to(ORIGIN)

            new_desc = Text(
                desc,
                font="STXingkai",
                font_size=34,
                color=TEAL,
            ).scale(1.5)
            new_desc.next_to(new_sym, DOWN, buff=0.8)

            self.play(
                ReplacementTransform(old_sym, new_sym),
                ReplacementTransform(old_desc, new_desc),
                run_time=0.5
            )
            self.wait(0.4)

            old_sym = new_sym
            old_desc = new_desc

        self.play(
            FadeOut(old_sym, scale=0.8),
            FadeOut(old_desc, shift=DOWN * 0.2),
            run_time=0.5
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
                sym = MathTex(latex_code, font_size=52, color=WHITE)
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
            run_time=1
        )

        # 呼吸动画：符号微微缩放
        self.play(
            LaggedStart(
                *[ApplyMethod(sym.scale, 1.08, rate_func=there_and_back)
                  for sym in all_group_symbols],
                lag_ratio=0.03,
            ),
            run_time=1
        )
        ring.set_stroke(opacity=0.6)
        self.wait(0.5)

# manim -pqh 常见的数学符号.py GroupedGreekLetters
