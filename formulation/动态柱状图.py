from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class DynamicBarChart(Scene):
    def construct(self):
        # 预定义各年份的数据（5个类别的值）
        year_data = {
            2020: [3, 7, 5, 9, 2],
            2021: [4, 6, 8, 5, 7],
            2022: [2, 5, 6, 8, 4],
            2023: [5, 8, 4, 6, 9],
            2024: [7, 4, 9, 7, 5]
        }
        
        # 固定标签和颜色
        labels = ["A", "B", "C", "D", "E"]
        colors = [BLUE, GREEN, YELLOW, RED, PURPLE]
        
        # 创建初始柱状图 (2020年)
        chart = BarChart(
            values=year_data[2020],
            bar_names=labels,
            bar_colors=colors,
            bar_fill_opacity=0.8,
            bar_stroke_width=2,
            y_range=[0, 10, 2],
            y_length=6,
            x_length=10
        )
        
        # 添加标题和年份标签
        title = Text("年度数据变化", font_size=32)
        year_text = Text("2020", font_size=36,color=RED)
        # 将标题和年份组合成一个VGroup，并整齐排列
        title_group = VGroup(year_text,title).arrange(LEFT, buff=0.3)
        title_group.to_edge(UP)
        # 添加数值标签
        value_labels = self.create_value_labels(chart, year_data[2020])
        
        # 添加坐标轴标签
        y_label = chart.get_y_axis_label("数值", edge=LEFT, direction=LEFT)
        x_label = chart.get_x_axis_label("类别", direction=DOWN)
        
        # 初始动画
        self.play(
            Create(chart),
            Write(title),
            Write(year_text),
            Write(y_label),
            Write(x_label)
        )
        self.play(Write(value_labels))
        self.wait(0.5)
        
        # 存储当前对象用于更新
        current_bars = chart.bars
        current_labels = value_labels
        current_year = year_text
        # 逐年更新数据 (2021-2024)
        for year in range(2021, 2025):
            # 创建新柱子和数值标签
            new_chart = BarChart(
                values=year_data[year],
                bar_names=labels,
                bar_colors=colors,
                bar_fill_opacity=0.8,
                bar_stroke_width=2,
                y_range=[0, 10, 2],
                y_length=6,
                x_length=10
            )
            new_bars = new_chart.bars
            new_labels = self.create_value_labels(new_chart, year_data[year])
           
            # 创建新年份文本
            new_year_text = Text(str(year), font_size=36,color="RED")
            new_year_text.move_to(current_year)  # 保持位置不变
            # 动画：更新柱子、数值标签和年份
            self.play(
                *[Transform(old_bar, new_bar) 
                  for old_bar, new_bar in zip(current_bars, new_bars)],
                *[Transform(old_label, new_label) 
                  for old_label, new_label in zip(current_labels, new_labels)],
                Transform(year_text, new_year_text),
                run_time=1.5
            )
            
            # 更新当前引用
            current_bars = new_bars
            current_labels = new_labels
            self.wait(0.5)
        
        # 最终展示
        self.wait(2)
    
    def create_value_labels(self, chart, values):
        """为每个柱子创建数值标签"""
        labels = VGroup()
        for bar, value in zip(chart.bars, values):
            label = Text(str(value), font_size=24)
            label.next_to(bar, UP, buff=0.2)
            labels.add(label)
        return labels

# 运行命令: 
# manim -pqh 动态柱状图.py DynamicBarChart -r 1920,1080
        
