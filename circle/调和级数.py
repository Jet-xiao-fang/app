from manim import *
import numpy as np

class HarmonicSeries(Scene):
    def construct(self):
        # 初始化参数
        max_terms = 15  # 最大项数
        terms = [1/n for n in range(1, max_terms+1)]
        partial_sums = np.cumsum(terms).tolist()

        # 创建坐标系
        axes = Axes(
            x_range=[0, max_terms, 5],
            y_range=[0, partial_sums[-1]+1, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, max_terms+1, 5)}
        ).shift(DOWN*0.3)
        
        # 添加标签
        title = Tex(
        r"$1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots : H(n) = \sum_{k=1}^n \frac{1}{k}$",
        font_size=36,
        color=YELLOW
        ).to_edge(UP)
        self.play(Write(title))

        # 绘制坐标系
        self.play(Create(axes))
        self.wait(0.5)

        # 初始化图形元素
        bars = VGroup()
        dots = VGroup()
        sum_label = always_redraw(lambda: Tex(
            f"$H({len(bars)}) \\approx {partial_sums[len(bars)-1]:.3f}$" if len(bars) > 0 else "",
            font_size=24
        ).next_to(axes, UP, buff=0.2))

        # 动画过程
        self.add(sum_label)
        current_sum = 0
        for i in range(max_terms):
            # 创建条形图
            bar = Rectangle(
                height=terms[i],
                width=0.4,
                fill_color=BLUE,
                fill_opacity=0.7,
                stroke_color=WHITE
            ).move_to(axes.c2p(i+1, terms[i]/2))
            
            # 创建点图
            dot = Dot(axes.c2p(i+1, partial_sums[i]), color=RED)
            
            # 动画序列
            self.play(
                Create(bar),
                Create(dot),
                run_time=0.5
            )
            bars.add(bar)
            dots.add(dot)
            
            # 连接点（从第二个点开始）
            if i > 0:
                line = Line(
                    dots[i-1].get_center(),
                    dots[i].get_center(),
                    color=RED
                )
                self.play(Create(line), run_time=0.3)
            
            self.wait(0.1)

        self.wait(2)

#   manim -pqh 调和级数.py HarmonicSeries -r 1920,1080
