from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class DynamicBarChart(Scene):
    def construct(self):
        # 富豪财富数据（单位：十亿美元），年份2010、2015、2020、2025
        data = {
            2010: {"马斯克": 12, "贝佐斯": 18, "阿诺特": 27, "盖茨": 54, "巴菲特": 47},
            2015: {"马斯克": 23, "贝佐斯": 50, "阿诺特": 41, "盖茨": 79, "巴菲特": 67},
            2020: {"马斯克": 151, "贝佐斯": 113, "阿诺特": 102, "盖茨": 98, "巴菲特": 82},
            2025: {"马斯克": 250, "贝佐斯": 180, "阿诺特": 200, "盖茨": 120, "巴菲特": 110},
        }
        years = list(data.keys())
        colors = {
            "马斯克": GREY,
            "贝佐斯": BLUE,
            "阿诺特": PURPLE,
            "盖茨": GREEN,
            "巴菲特": ORANGE,
        }

        # 布局参数
        bar_width = 0.7
        bar_spacing = 0.5
        x_start = -2.6              # 最左侧条形的底部中心 x 坐标
        y_bottom = -3.5             # 所有条形的底部 y 坐标（固定）
        max_height = 5.5
        max_wealth = max(max(d.values()) for d in data.values())  # 250

        def get_height(wealth):
            return (wealth / max_wealth) * max_height

        # 半透明网格
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 8, 1],
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0}
        )
        self.add(grid)

        # 初始化条形（按财富降序）
        init_data = data[years[0]]
        sorted_init = sorted(init_data.items(), key=lambda x: x[1], reverse=True)

        bars = VGroup()
        label_dict = {}
        current_values = {}

        for i, (name, wealth) in enumerate(sorted_init):
            h = get_height(wealth)
            rect = Rectangle(
                width=bar_width,
                height=h,
                fill_color=colors[name],
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=3,
            )
            rect.move_to([x_start + i*(bar_width+bar_spacing), y_bottom, 0], aligned_edge=DOWN)
            rect.name = name
            bars.add(rect)

            # 标签位于条形顶部上方
            label = Text(f"{name}\n{wealth}", font_size=18, color=WHITE, weight=BOLD)
            label.next_to(rect, UP, buff=0.1)
            label_dict[name] = label
            current_values[name] = wealth

        self.add(bars, *label_dict.values())

        # 年份标签：放在条形图下方正中间
        year_label = Text(f"{years[0]}年", font_size=36, color=YELLOW, weight=BOLD)
        # 计算整个条形组的大致中心 x 坐标
        total_width = len(sorted_init) * (bar_width + bar_spacing) - bar_spacing
        center_x = x_start + total_width / 2
        year_label.move_to([center_x, y_bottom - 0.8, 0])
        self.add(year_label)
        self.wait(0.8)

        # 逐年动画
        for year_idx in range(1, len(years)):
            new_data = data[years[year_idx]]
            for name, v in new_data.items():
                current_values[name] = v

            # 按新财富降序排序
            sorted_names = sorted(current_values.keys(), key=lambda n: current_values[n], reverse=True)

            # 计算每个条形的最终状态
            final_params = {}
            for i, name in enumerate(sorted_names):
                new_h = get_height(current_values[name])
                new_bottom = np.array([x_start + i*(bar_width+bar_spacing), y_bottom, 0])
                final_params[name] = {
                    "bottom": new_bottom,
                    "height": new_h,
                    "value": current_values[name]
                }

            # 条形动画
            bar_animations = []
            for rect in bars:
                name = rect.name
                p = final_params[name]
                target_rect = Rectangle(
                    width=bar_width,
                    height=p["height"],
                    fill_color=colors[name],
                    fill_opacity=0.8,
                    stroke_color=WHITE,
                    stroke_width=3,
                )
                target_rect.move_to(p["bottom"], aligned_edge=DOWN)
                bar_animations.append(rect.animate.become(target_rect))

            # 标签动画
            label_animations = []
            for name in sorted_names:
                p = final_params[name]
                target_top = p["bottom"] + UP * p["height"]
                target_text = Text(f"{name}\n{p['value']}", font_size=18, color=WHITE, weight=BOLD)
                target_text.next_to(target_top, UP, buff=0.1)
                old_label = label_dict[name]
                label_animations.append(Transform(old_label, target_text))

            # 年份标签动画
            new_year_text = Text(f"{years[year_idx]}年", font_size=36, color=YELLOW, weight=BOLD)
            new_year_text.move_to(year_label.get_center())  # 位置保持不变
            year_anim = Transform(year_label, new_year_text)

            # 播放所有动画
            self.play(
                *bar_animations,
                *label_animations,
                year_anim,
                run_time=1.5,
                rate_func=linear
            )
            self.wait(1)

        self.wait(2)

# 运行命令：manim -pqh 排序.py DynamicBarChart

# 运行命令：manim -p 排序2.py DynamicBarChart