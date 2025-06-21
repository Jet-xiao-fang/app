from manim import *

class tupan(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0B1A"
        # 1. 创建标题
        title = Text("柱状图设置", 
                    font="Microsoft YaHei",
                    font_size=30,
                    color=BLUE).to_edge(UP)
        self.add(title)
        
        self.show()
    
    def show(self):
        # 数据设置
        categories = ["A", "B", "C", "D"]
        values = [3, 7, 5, 2]
        bar_colors = [BLUE, GREEN, YELLOW, RED]
        
        # 修复：使用bar_style替代单独的描边参数
        chart = BarChart(
            values,
            bar_names=categories,
            bar_colors=bar_colors,
            bar_stroke_width=2,
            bar_width=0.7,
            y_range=[0, 8],  # 替换 max_value → y_range
            y_axis_config={
                "font_size": 24, 
                "color": LIGHT_GRAY
            },
        )
        
        # 设置图表标题（已经有一个标题在顶部，这个可以放在图表上方）
        chart_title = Text("销售数据统计", font_size=32, color=WHITE)
        chart_title.next_to(chart, UP, buff=0.5)  # 放在柱状图上方
        y_label = Text("销售量", font_size=26, color=LIGHT_GRAY).next_to(chart.y_axis, LEFT, buff=0.5)
        
        # 添加数值标签到柱子顶部
        value_labels = VGroup()
        for bar, value in zip(chart.bars, values):
            label = Text(str(value), font_size=20, color=WHITE)
            label.next_to(bar, UP, buff=0.2)
            value_labels.add(label)

        # 动画展示
        self.play(
            Create(chart),
            FadeIn(chart_title),
            Write(y_label),
            run_time=2
        )
        self.wait(0.5)
        self.play(FadeIn(value_labels))
        self.wait(2)
        
        # 高亮第二个柱子
        bar = chart.bars[1]
        bar.save_state()  # 保存当前状态以便恢复
        
        self.play(
            bar.animate.set_color(RED).scale(1.2, about_point=bar.get_bottom()),
            bar.animate.set_stroke(width=4)
        )
        self.wait(2)
        
        # 恢复原状（可选）
        self.play(Restore(bar))
        self.wait()

#  manim -pqh --format=png 柱状图.py tupan -r 1920,1080

