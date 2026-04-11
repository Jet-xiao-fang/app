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
        # ========== 真实数据（2010–2025，只存储每年实际前五名） ==========
        yearly_data = {
            2012: [("卡洛斯·斯利姆", 690), ("比尔·盖茨", 610), ("沃伦·巴菲特", 440), ("伯纳德·阿诺特", 410), ("阿曼西奥·奥尔特加", 375)],
            2013: [("卡洛斯·斯利姆", 730), ("比尔·盖茨", 670), ("阿曼西奥·奥尔特加", 570), ("沃伦·巴菲特", 535), ("拉里·埃里森", 430)],
            2014: [("比尔·盖茨", 760), ("卡洛斯·斯利姆", 720), ("阿曼西奥·奥尔特加", 640), ("沃伦·巴菲特", 582), ("拉里·埃里森", 480)],
            2015: [("比尔·盖茨", 792), ("卡洛斯·斯利姆", 771), ("沃伦·巴菲特", 727), ("阿曼西奥·奥尔特加", 645), ("拉里·埃里森", 543)],
            2016: [("比尔·盖茨", 750), ("阿曼西奥·奥尔特加", 670), ("沃伦·巴菲特", 608), ("卡洛斯·斯利姆", 500), ("杰夫·贝佐斯", 452)],
            2017: [("比尔·盖茨", 860), ("沃伦·巴菲特", 756), ("杰夫·贝佐斯", 728), ("阿曼西奥·奥尔特加", 713), ("马克·扎克伯格", 560)],
            2018: [("杰夫·贝佐斯", 1120), ("比尔·盖茨", 900), ("沃伦·巴菲特", 840), ("伯纳德·阿诺特", 720), ("马克·扎克伯格", 710)],
            2019: [("杰夫·贝佐斯", 1310), ("比尔·盖茨", 965), ("沃伦·巴菲特", 825), ("伯纳德·阿诺特", 760), ("马克·扎克伯格", 623)],
            2020: [("杰夫·贝佐斯", 1130), ("比尔·盖茨", 980), ("马克·扎克伯格", 860), ("伯纳德·阿诺特", 760), ("沃伦·巴菲特", 735)],
            2021: [("杰夫·贝佐斯", 1770), ("埃隆·马斯克", 1510), ("伯纳德·阿诺特", 1500), ("比尔·盖茨", 1240), ("马克·扎克伯格", 970)],
            2022: [("埃隆·马斯克", 2190), ("杰夫·贝佐斯", 1710), ("伯纳德·阿诺特", 1580), ("比尔·盖茨", 1290), ("沃伦·巴菲特", 1180)],
            2023: [("伯纳德·阿诺特", 2110), ("埃隆·马斯克", 1800), ("杰夫·贝佐斯", 1140), ("拉里·埃里森", 1070), ("沃伦·巴菲特", 1060)],
            2024: [("伯纳德·阿诺特", 2330), ("埃隆·马斯克", 1950), ("杰夫·贝佐斯", 1940), ("马克·扎克伯格", 1770), ("拉里·埃里森", 1410)],
            2025: [("伯纳德·阿诺特", 2330), ("埃隆·马斯克", 1950), ("杰夫·贝佐斯", 1940), ("马克·扎克伯格", 1770), ("拉里·埃里森", 1460)],
        }
        
        years = list(yearly_data.keys())
        max_wealth = 2330   # 2024/2025 年最大财富值
        max_height = 5.5
        
        def get_height(wealth):
            return (wealth / max_wealth) * max_height
        
        # 颜色映射（统一颜色，每人固定）
        color_map = {
            "卡洛斯·斯利姆": "#FFD966",
            "比尔·盖茨": "#6AA84F",
            "沃伦·巴菲特": "#3C78D8",
            "伯纳德·阿诺特": "#8E7CC3",
            "拉里·埃里森": "#E06666",
            "阿曼西奥·奥尔特加": "#F6B26B",
            "杰夫·贝佐斯": "#45818E",
            "马克·扎克伯格": "#93C47D",
            "埃隆·马斯克": "#D5A6BD",
        }
        # ========== 添加标题和单位备注 ==========
        title = Text("近14年前五富豪排名", font_size=42, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=3)
        self.add(title)
        
        unit_note = Text("单位：亿美元", font_size=20, color=GREY, weight=NORMAL)
        unit_note.next_to(title,DOWN, buff=0.5)
        self.add(unit_note)

        # 布局参数（5个条形）
        bar_width = 0.7
        bar_spacing = 0.8
        total_width = 5 * bar_width + 4 * bar_spacing
        x_start = -total_width / 2 + bar_width/2   # 第一个条形的底部中心 x 坐标
        y_bottom = -3.5
        
        # 网格
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 8, 1],
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0}
        )
        self.add(grid)
        
        # 初始年份（2010）数据
        init_data = yearly_data[years[0]]
        bars = VGroup()
        label_dict = {}
        current_wealth = {}
        
        for i, (name, wealth) in enumerate(init_data):
            h = get_height(wealth)
            rect = Rectangle(
                width=bar_width,
                height=h,
                fill_color=color_map[name],
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=3,
            )
            rect.move_to([x_start + i*(bar_width+bar_spacing), y_bottom, 0], aligned_edge=DOWN)
            rect.name = name
            bars.add(rect)
            
            label = Text(f"{name}\n{wealth}", font_size=18, color=WHITE, weight=BOLD)
            label.next_to(rect, UP, buff=0.1)
            label_dict[name] = label
            current_wealth[name] = wealth
        
        self.add(bars, *label_dict.values())
        
        # 年份标签（条形组下方正中）
        center_x = x_start + (total_width - bar_width)/2
        year_label = Text(f"{years[0]}年", font_size=36, color=YELLOW, weight=BOLD)
        year_label.move_to([center_x, y_bottom - 0.8, 0])
        self.add(year_label)
        self.wait(0.8)
        
        
        
        # 逐年动画
        for year_idx in range(1, len(years)):
            new_data = yearly_data[years[year_idx]]
            new_names = [pair[0] for pair in new_data]
            new_wealths = [pair[1] for pair in new_data]
            
            # 确定每个条形的新主人：优先保留同名，否则按顺序匹配（最直接方法：按排名一一对应）
            # 更健壮：构建从旧名字到新名字的映射，尽量让同名留在原位，新人替换掉离开的人
            old_names = [rect.name for rect in bars]
            # 找出仍然留在前五的旧名字
            remaining = set(old_names) & set(new_names)
            # 需要替换的索引：旧名字不在新列表中
            replace_indices = [i for i, name in enumerate(old_names) if name not in remaining]
            # 新名字中尚未被匹配的
            new_names_unmatched = [n for n in new_names if n not in remaining]
            # 构建替换映射
            replace_map = {}
            for i, new_name in zip(replace_indices, new_names_unmatched):
                replace_map[old_names[i]] = new_name
            
            # 重新计算最终参数（按新排名顺序）
            final_params = []
            for rank, (name, wealth) in enumerate(new_data):
                # 确定这个条形当前对应的 rect（可能是同名，也可能是被替换的）
                if name in old_names:
                    rect = bars[old_names.index(name)]
                else:
                    # 找到被替换的旧名字对应的 rect
                    for old, new in replace_map.items():
                        if new == name:
                            rect = bars[old_names.index(old)]
                            break
                target_h = get_height(wealth)
                target_bottom = np.array([x_start + rank*(bar_width+bar_spacing), y_bottom, 0])
                final_params.append({
                    "rect": rect,
                    "target_bottom": target_bottom,
                    "target_height": target_h,
                    "name": name,
                    "wealth": wealth,
                    "old_name": rect.name
                })
            
            # 条形动画和标签动画
            bar_animations = []
            label_animations = []
            for p in final_params:
                rect = p["rect"]
                old_name = p["old_name"]
                new_name = p["name"]
                new_wealth = p["wealth"]
                # 条形变换
                target_rect = Rectangle(
                    width=bar_width,
                    height=p["target_height"],
                    fill_color=color_map[new_name],
                    fill_opacity=0.8,
                    stroke_color=WHITE,
                    stroke_width=3,
                )
                target_rect.move_to(p["target_bottom"], aligned_edge=DOWN)
                bar_animations.append(rect.animate.become(target_rect))
                # 更新 rect 存储的名字
                rect.name = new_name
                
                # 标签变换
                target_top = p["target_bottom"] + UP * p["target_height"]
                target_text = Text(f"{new_name}\n{new_wealth}", font_size=18, color=WHITE, weight=BOLD)
                target_text.next_to(target_top, UP, buff=0.1)
                if old_name in label_dict:
                    old_label = label_dict.pop(old_name)
                    label_animations.append(Transform(old_label, target_text))
                    label_dict[new_name] = old_label
                else:
                    # 理论上不会发生
                    new_label = target_text
                    self.add(new_label)
                    label_dict[new_name] = new_label
            
            # 年份标签动画
            new_year_text = Text(f"{years[year_idx]}年", font_size=36, color=YELLOW, weight=BOLD)
            new_year_text.move_to(year_label.get_center())
            year_anim = Transform(year_label, new_year_text)
            
            # 播放
            self.play(
                *bar_animations,
                *label_animations,
                year_anim,
                run_time=1.5,
                rate_func=linear
            )
            self.wait(1)
        

# 运行命令：manim -pqh 动态条形图.py DynamicBarChart

# 运行命令：manim -pqh 排序3.py DynamicBarChart