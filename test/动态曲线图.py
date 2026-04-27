from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class DynamicLineChart(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # ========== 完整数据（2012–2025，包含所有人） ==========
        # 构建完整数据集：每年记录所有有数据的人
        yearly_raw = {
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
        
        # 转换为字典格式 {年份: {人名: 财富}}
        yearly_data = {}
        for year, data in yearly_raw.items():
            yearly_data[year] = {name: wealth for name, wealth in data}
        
        # 提取所有出现过的人物
        all_people = set()
        for data in yearly_data.values():
            for name in data.keys():
                all_people.add(name)
        all_people = sorted(list(all_people))
        
        # 颜色映射（每人固定颜色）
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
        
        # 为没有指定颜色的人物分配新颜色
        default_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", 
                          "#DDA0DD", "#98D8C8", "#F7DC6F", "#BB8FCE", "#85C1E2"]
        color_idx = 0
        for person in all_people:
            if person not in color_map:
                color_map[person] = default_colors[color_idx % len(default_colors)]
                color_idx += 1
        
        years = sorted(yearly_data.keys())
        max_wealth = 2400
        min_wealth = 0
        
        # ========== 坐标轴 ==========
        axes = Axes(
            x_range=[min(years)-0.5, max(years)+0.5, 2],
            y_range=[min_wealth, max_wealth, 500],
            x_length=12,
            y_length=6,
            axis_config={"color": WHITE, "include_numbers": True},
            x_axis_config={"numbers_to_include": list(range(2012, 2026, 2))},
            y_axis_config={"numbers_to_include": list(range(0, 2501, 500))}
        )
        axes.to_edge(DOWN, buff=0.5)
        axes.to_edge(LEFT, buff=0.5)
        
        # 坐标轴标签
        x_label = Text("年份", font_size=24, color=WHITE)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("财富（亿美元）", font_size=24, color=WHITE)
        y_label.rotate(90 * DEGREES)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3)
        
        # 标题
        title = Text("2012–2025 富豪财富变化曲线", font_size=42, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # 图例（显示所有人，放在右侧）
        legend_items = VGroup()
        for i, person in enumerate(all_people):
            dot_legend = Dot(color=color_map[person], radius=0.08)
            label_legend = Text(person, font_size=12, color=color_map[person])
            item = VGroup(dot_legend, label_legend)
            item.arrange(RIGHT, buff=0.1)
            legend_items.add(item)
        
        legend_items.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        legend_items.to_edge(RIGHT, buff=0.5)
        legend_items.to_edge(UP, buff=2.5)
        
        self.add(title, x_label, y_label, axes, legend_items)
        self.wait(0.5)
        
        # ========== 为每个人创建折线 ==========
        lines = {}
        dots = {}
        name_labels = {}
        
        # 获取第一年的数据
        first_year = years[0]
        first_data = yearly_data[first_year]
        
        for person in all_people:
            if person in first_data:
                wealth = first_data[person]
                point = axes.coords_to_point(first_year, wealth)
                dot = Dot(point, color=color_map[person], radius=0.08)
                dots[person] = dot
                
                # 折线初始只有起点
                line = VMobject(stroke_color=color_map[person], stroke_width=3)
                line.set_points_as_corners([point, point])
                lines[person] = line
                
                # 名字标签
                label = Text(person, font_size=12, color=color_map[person], weight=BOLD)
                label.next_to(point, RIGHT, buff=0.1)
                name_labels[person] = label
                
                self.add(dot, line, label)
            else:
                # 第一年不在数据中，稍后出现
                pass
        
        self.wait(1)
        
        # ========== 逐年动画 ==========
        for idx in range(1, len(years)):
            year = years[idx]
            prev_year = years[idx-1]
            current_data = yearly_data[year]
            prev_data = yearly_data[prev_year]
            
            animations = []
            
            for person in all_people:
                # 构建完整的历史路径点
                path_points = []
                for y in years[:idx+1]:
                    if y in yearly_data and person in yearly_data[y]:
                        w = yearly_data[y][person]
                        path_points.append(axes.coords_to_point(y, w))
                    else:
                        # 如果某年没有数据，不添加点（路径会断开）
                        pass
                
                if person in current_data:
                    wealth = current_data[person]
                    new_point = axes.coords_to_point(year, wealth)
                    
                    if person in dots:
                        # 已存在的人物：移动点和标签，延长折线
                        animations.append(dots[person].animate.move_to(new_point))
                        animations.append(name_labels[person].animate.next_to(new_point, RIGHT, buff=0.1))
                        
                        # 更新折线：基于所有历史数据点
                        if len(path_points) >= 2:
                            new_line = VMobject(stroke_color=color_map[person], stroke_width=3)
                            new_line.set_points_as_corners(path_points)
                            animations.append(Transform(lines[person], new_line))
                    else:
                        # 新出现的人物
                        dot = Dot(new_point, color=color_map[person], radius=0.08)
                        dots[person] = dot
                        
                        # 构建路径（可能只有当前点）
                        if len(path_points) >= 2:
                            line = VMobject(stroke_color=color_map[person], stroke_width=3)
                            line.set_points_as_corners(path_points)
                        else:
                            line = VMobject(stroke_color=color_map[person], stroke_width=3)
                            line.set_points_as_corners([new_point, new_point])
                        lines[person] = line
                        
                        label = Text(person, font_size=12, color=color_map[person], weight=BOLD)
                        label.next_to(new_point, RIGHT, buff=0.1)
                        name_labels[person] = label
                        
                        animations.append(FadeIn(dot, shift=UP))
                        animations.append(FadeIn(line, shift=UP))
                        animations.append(FadeIn(label, shift=UP))
                else:
                    # 该人物本年没有数据（不在前五）
                    if person in dots and person in prev_data and person not in current_data:
                        # 淡出点，但保留折线
                        animations.append(FadeOut(dots[person]))
                        animations.append(FadeOut(name_labels[person]))
                        # 可选：折线也淡出
                        # animations.append(FadeOut(lines[person]))
            
            # 年份指示器
            year_indicator = Text(f"{year}年", font_size=30, color=YELLOW, weight=BOLD)
            year_indicator.to_edge(RIGHT, buff=0.8)
            year_indicator.to_edge(UP, buff=1.5)
            if idx == 1:
                self.add(year_indicator)
                animations.append(FadeIn(year_indicator))
            else:
                animations.append(Transform(self.year_indicator, year_indicator))
            
            self.play(*animations, run_time=1.2, rate_func=linear)
            self.wait(0.8)
            
            # 保存年份指示器
            if idx == 1:
                self.year_indicator = year_indicator
            else:
                self.year_indicator = year_indicator
        
        # 最终停留
        self.wait(3)


# 运行命令：manim -pqh 动态曲线图.py DynamicLineChart