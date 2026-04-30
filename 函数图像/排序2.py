from manim import *
import numpy as np

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class DynamicLineChart(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        
        # ========== 完整数据（2012–2025，包含所有人） ==========
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
        
        # 转换为字典格式
        yearly_data = {}
        for year, data in yearly_raw.items():
            yearly_data[year] = {name: wealth for name, wealth in data}
        
        # 提取所有人物
        all_people = set()
        for data in yearly_data.values():
            for name in data.keys():
                all_people.add(name)
        all_people = sorted(list(all_people))
        
        # 颜色映射
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
        
        # 补充颜色
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
        
        # ========== 坐标轴（优化数字显示） ==========
        axes = Axes(
            x_range=[min(years)-0.5, max(years)+0.5, 2],
            y_range=[min_wealth, max_wealth, 500],
            x_length=12,
            y_length=6,
            axis_config={"color": WHITE, "include_numbers": True},
            x_axis_config={
                "numbers_to_include": list(range(2012, 2026, 2)),
                "font_size": 24,  # 增大字体
                "decimal_places": 0,  # 不显示小数
                "include_tip": False,
                "line_to_number_buff": 0.1
            },
            y_axis_config={
                "numbers_to_include": list(range(0, 2501, 500)),
                "font_size": 24,
                "decimal_places": 0
            }
        )
        axes.to_edge(DOWN, buff=0.5)
        axes.to_edge(LEFT, buff=0.5)
        
        # 强制设置x轴标签格式，避免重叠
        x_labels = VGroup()
        for year in range(2012, 2026, 2):
            label = Text(str(year), font_size=24, color=WHITE)
            point = axes.coords_to_point(year, 0)
            label.move_to(point + DOWN * 0.3)
            x_labels.add(label)
        
        # 移除原有的x轴数字，使用自定义的
        axes.x_axis.numbers = x_labels
        
        # 同样处理y轴
        y_labels = VGroup()
        for wealth in range(0, 2501, 500):
            label = Text(str(wealth), font_size=24, color=WHITE)
            point = axes.coords_to_point(min(years)-0.5, wealth)
            label.move_to(point + LEFT * 0.3)
            y_labels.add(label)
        axes.y_axis.numbers = y_labels
        
        # 坐标轴标签
        x_label = Text("年份", font_size=28, color=WHITE)
        x_label.next_to(axes.x_axis, DOWN, buff=0.5)
        y_label = Text("财富（亿美元）", font_size=28, color=WHITE)
        y_label.rotate(90 * DEGREES)
        y_label.next_to(axes.y_axis, LEFT, buff=0.5)
        
        # 标题
        title = Text("2012–2025 富豪财富变化曲线", font_size=42, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # 图例（右侧）
        legend_items = VGroup()
        for i, person in enumerate(all_people):
            dot_legend = Dot(color=color_map[person], radius=0.06)
            label_legend = Text(person, font_size=12, color=color_map[person])
            item = VGroup(dot_legend, label_legend)
            item.arrange(RIGHT, buff=0.1)
            legend_items.add(item)
        
        legend_items.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        legend_items.to_edge(RIGHT, buff=0.3)
        legend_items.to_edge(UP, buff=2.5)
        
        self.add(title, x_label, y_label, axes, legend_items)
        self.wait(0.5)
        
        # ========== 创建曲线（使用Cubic贝塞尔曲线实现平滑） ==========
        lines = {}
        dots = {}
        name_labels = {}
        
        def create_smooth_curve(points):
            """使用三次贝塞尔曲线创建平滑曲线"""
            if len(points) < 2:
                curve = VMobject(stroke_color=WHITE, stroke_width=3)
                curve.set_points_as_corners(points)
                return curve
            
            # 使用插值创建平滑曲线
            from scipy.interpolate import CubicSpline
            import numpy as np
            
            # 提取x和y坐标
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]
            
            # 创建更密集的点用于平滑曲线
            x_smooth = np.linspace(min(xs), max(xs), 100)
            cs = CubicSpline(xs, ys, bc_type='natural')
            y_smooth = cs(x_smooth)
            
            # 构建平滑曲线的点集
            smooth_points = [axes.coords_to_point(x_smooth[i], y_smooth[i]) 
                           for i in range(len(x_smooth))]
            
            curve = VMobject(stroke_color=WHITE, stroke_width=3)
            curve.set_points_smoothly(smooth_points)
            return curve
        
        # 获取第一年数据
        first_year = years[0]
        first_data = yearly_data[first_year]
        
        for person in all_people:
            if person in first_data:
                wealth = first_data[person]
                point = axes.coords_to_point(first_year, wealth)
                dot = Dot(point, color=color_map[person], radius=0.08)
                dots[person] = dot
                
                # 初始曲线只是一个点
                curve = VMobject(stroke_color=color_map[person], stroke_width=3)
                curve.set_points_as_corners([point, point])
                lines[person] = curve
                
                label = Text(person, font_size=14, color=color_map[person], weight=BOLD)
                label.next_to(point, RIGHT, buff=0.1)
                name_labels[person] = label
                
                self.add(dot, curve, label)
        
        self.wait(1)
        
        # ========== 逐年动画 ==========
        for idx in range(1, len(years)):
            year = years[idx]
            current_data = yearly_data[year]
            
            animations = []
            
            for person in all_people:
                # 收集所有历史数据点
                history_points = []
                for y in years[:idx+1]:
                    if y in yearly_data and person in yearly_data[y]:
                        w = yearly_data[y][person]
                        point = axes.coords_to_point(y, w)
                        history_points.append(point)
                
                if person in current_data:
                    wealth = current_data[person]
                    new_point = axes.coords_to_point(year, wealth)
                    
                    if person in dots:
                        # 移动点和标签
                        animations.append(dots[person].animate.move_to(new_point))
                        animations.append(name_labels[person].animate.next_to(new_point, RIGHT, buff=0.1))
                        
                        # 创建平滑曲线（如果至少有2个点）
                        if len(history_points) >= 2:
                            # 获取点的坐标（世界坐标）
                            coords = [(p[0], p[1]) for p in history_points]
                            smooth_curve = create_smooth_curve(coords)
                            smooth_curve.set_stroke(color=color_map[person], width=3)
                            animations.append(Transform(lines[person], smooth_curve))
                    else:
                        # 新出现的人物
                        dot = Dot(new_point, color=color_map[person], radius=0.08)
                        dots[person] = dot
                        
                        if len(history_points) >= 2:
                            coords = [(p[0], p[1]) for p in history_points]
                            smooth_curve = create_smooth_curve(coords)
                        else:
                            smooth_curve = VMobject(stroke_color=color_map[person], stroke_width=3)
                            smooth_curve.set_points_as_corners([new_point, new_point])
                        
                        lines[person] = smooth_curve
                        label = Text(person, font_size=14, color=color_map[person], weight=BOLD)
                        label.next_to(new_point, RIGHT, buff=0.1)
                        name_labels[person] = label
                        
                        animations.append(FadeIn(dot, shift=UP))
                        animations.append(FadeIn(smooth_curve, shift=UP))
                        animations.append(FadeIn(label, shift=UP))
                else:
                    # 人物不在当前数据中
                    if person in dots:
                        animations.append(FadeOut(dots[person]))
                        animations.append(FadeOut(name_labels[person]))
            
            # 年份指示器（使用Transform）
            new_year_indicator = Text(f"{year}年", font_size=36, color=YELLOW, weight=BOLD)
            new_year_indicator.to_edge(RIGHT, buff=0.8)
            new_year_indicator.to_edge(UP, buff=1.5)
            
            if idx == 1:
                self.add(new_year_indicator)
                animations.append(FadeIn(new_year_indicator))
                year_indicator = new_year_indicator
            else:
                animations.append(Transform(year_indicator, new_year_indicator))
            
            self.play(*animations, run_time=1.2, rate_func=linear)
            self.wait(0.8)
        
        self.wait(3)


# 运行命令：manim -pqh 曲线图.py DynamicLineChart