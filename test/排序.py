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
        data = {
            2020: {"中国": 12, "美国": 21, "印度": 8, "日本": 15, "德国": 14},
            2025: {"中国": 16, "美国": 22, "印度": 11, "日本": 14, "德国": 13},
            2030: {"中国": 19, "美国": 23, "印度": 15, "日本": 12, "德国": 11},
        }
        years = list(data.keys())
        colors = {
            "中国": BLUE,
            "美国": RED,
            "印度": ORANGE,
            "日本": GREEN,
            "德国": PURPLE,
        }

        # 布局参数
        bar_width = 0.7
        bar_spacing = 0.5
        x_start = -2.6              # 最左侧条形的底部中心 x 坐标
        y_bottom = -3.5              # 所有条形的底部 y 坐标（固定）
        max_height = 5.5
        max_gdp = max(max(d.values()) for d in data.values())  # 23

        def get_height(gdp):
            return (gdp / max_gdp) * max_height

        # 半透明网格
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 8, 1],
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0}
        )
        self.add(grid)

        # 初始化条形（按GDP降序）
        init_data = data[years[0]]
        sorted_init = sorted(init_data.items(), key=lambda x: x[1], reverse=True)

        bars = VGroup()
        label_dict = {}
        current_values = {}

        for i, (country, gdp) in enumerate(sorted_init):
            h = get_height(gdp)
            rect = Rectangle(
                width=bar_width,
                height=h,
                fill_color=colors[country],
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=3,
            )
            rect.move_to([x_start + i*(bar_width+bar_spacing), y_bottom, 0], aligned_edge=DOWN)
            rect.country = country
            bars.add(rect)

            # 标签垂直排列，位于条形顶部上方
            label = Text(f"{country}\n{gdp}", font_size=18, color=WHITE, weight=BOLD)
            label.next_to(rect, UP, buff=0.1)
            label_dict[country] = label
            current_values[country] = gdp

        self.add(bars, *label_dict.values())

        # 标题
        title = Text(str(years[0]), font_size=42, color=YELLOW, weight=BOLD).to_edge(UP, buff=3)
        title.shift(UP*0.2)
        self.play(Write(title))
        self.wait(0.8)

        # 逐年动画
        for year_idx in range(1, len(years)):
            new_data = data[years[year_idx]]
            for c, v in new_data.items():
                current_values[c] = v

            # 按新GDP降序排序
            sorted_countries = sorted(current_values.keys(), key=lambda c: current_values[c], reverse=True)

            # 计算每个条形的最终状态（底部中心坐标、高度、数值）
            final_params = {}
            for i, country in enumerate(sorted_countries):
                new_h = get_height(current_values[country])
                new_bottom = np.array([x_start + i*(bar_width+bar_spacing), y_bottom, 0])
                final_params[country] = {
                    "bottom": new_bottom,
                    "height": new_h,
                    "value": current_values[country]
                }

            # 条形动画：使用 become 变换到目标矩形（确保宽度不变、底部对齐）
            bar_animations = []
            for rect in bars:
                country = rect.country
                p = final_params[country]
                # 创建目标矩形（相同样式，正确的高度和底部位置）
                target_rect = Rectangle(
                    width=bar_width,
                    height=p["height"],
                    fill_color=colors[country],
                    fill_opacity=0.8,
                    stroke_color=WHITE,
                    stroke_width=3,
                )
                target_rect.move_to(p["bottom"], aligned_edge=DOWN)
                bar_animations.append(rect.animate.become(target_rect))

            # 标签动画：更新文字并移动到新条形顶部上方
            label_animations = []
            for country in sorted_countries:
                p = final_params[country]
                target_top = p["bottom"] + UP * p["height"]
                target_text = Text(f"{country}\n{p['value']}", font_size=18, color=WHITE, weight=BOLD)
                target_text.next_to(target_top, UP, buff=0.1)
                old_label = label_dict[country]
                label_animations.append(Transform(old_label, target_text))

            # 标题动画
            new_title = Text(str(years[year_idx]), font_size=42, color=YELLOW, weight=BOLD).to_edge(UP, buff=0.5)
            new_title.shift(UP*0.2)
            title_anim = Transform(title, new_title)

            # 播放所有动画
            self.play(
                *bar_animations,
                *label_animations,
                title_anim,
                run_time=1.5,
                rate_func=linear
            )
            self.wait(1)

        self.wait(2)
        
# manim -pqh 排序.py DynamicBarChart