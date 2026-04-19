from manim import *
import numpy as np
config.frame_height = 12
config.frame_width = 9
config.pixel_height = 1440
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class NineAngleRadarChart(Scene):
    """
    九角雷达图（九边形统计图）—— 0～100 分制
    科目：数学、政治、地理、历史、美术、生物、语文、英文、德文
    """
    def construct(self):
        self.camera.background_color = "#FDFDFD"
        # ========== 5. 标题 ==========
        title = Text("孩子偏科太严重了，\n以后毕业能干点什么？", font_size=42, color=BLACK)
        title.to_edge(UP, buff=1)
        self.add(title)
        # ========== 参数设置 ==========
        radius = 3.2                  # 外九边形半径
        center = ORIGIN               # 中心点坐标
        num_dims = 9                  # 维度数量
        # 九个轴的角度（从正上方开始，顺时针方向，间隔 2π/9）
        angles = [PI/2 - i * 2*PI/num_dims for i in range(num_dims)]
        # 示例数据（9个科目，分数 0～100，可自行修改）
        data = [10, 100, 13, 11, 100, 10, 11, 12, 100]   # 单位：分
        # 科目标签
        subjects = ["数学", "政治", "地理", "历史", "美术", "生物", "语文", "英文", "德文"]

        # 辅助函数：根据半径和角度列表计算顶点坐标
        def get_vertices(rad, angs):
            return [center + rad * np.array([np.cos(ang), np.sin(ang), 0]) for ang in angs]

        # ========== 1. 绘制网格（同心九边形） ==========
        # 网格比例对应 20,40,60,80,100 分（即半径比例 = 分数/100）
        grid_scales = [0.2, 0.4, 0.6, 0.8, 1.0]
        grid_polys = VGroup()
        for scale in grid_scales:
            vertices = get_vertices(radius * scale, angles)
            nonagon = Polygon(*vertices, color=GRAY, stroke_width=2, stroke_opacity=0.6)
            grid_polys.add(nonagon)

        # 添加网格分数标签（可选，标注在轴线适当位置）
        score_labels = VGroup()
        for scale in grid_scales:
            score = int(scale * 100)
            # 取第一个轴线的方向（正上方）来放置标签
            direction = np.array([np.cos(angles[0]), np.sin(angles[0]), 0])
            label_pos = center + (radius * scale) * direction
            label = Text(f"{score}", font_size=18, color=GRAY)
            label.next_to(label_pos, UP, buff=0.1)
            score_labels.add(label)

        # ========== 2. 绘制轴线（从中心到顶点的射线） ==========
        axis_lines = VGroup()
        for ang in angles:
            endpoint = center + radius * np.array([np.cos(ang), np.sin(ang), 0])
            line = Line(center, endpoint, color=WHITE, stroke_width=2)
            axis_lines.add(line)

        # ========== 3. 添加科目标签 ==========
        label_group = VGroup()
        offset = 0.5  # 标签距离顶点的偏移量
        for i, ang in enumerate(angles):
            direction = np.array([np.cos(ang), np.sin(ang), 0])
            label_pos = center + (radius + offset) * direction
            label = Text(subjects[i], font_size=28, color=BLUE_D)
            label.move_to(label_pos)
            # 根据角度微调标签位置，防止与轴线重叠
            if abs(ang - PI/2) < 0.1:          # 顶部标签向上偏移
                label.shift(UP * 0.2)
            elif abs(ang - (-PI/2)) < 0.1:     # 底部标签向下偏移
                label.shift(DOWN * 0.2)
            elif ang > 0 and ang < PI/2:       # 右上区域
                label.shift(UP * 0.1 + RIGHT * 0.1)
            elif ang > PI/2 and ang < PI:      # 左上区域
                label.shift(UP * 0.1 + LEFT * 0.1)
            label_group.add(label)

        # ========== 4. 数据点坐标及数据多边形（分数/100 映射半径） ==========
        data_points = []
        for i, ang in enumerate(angles):
            direction = np.array([np.cos(ang), np.sin(ang), 0])
            # 关键：分数除以100得到半径比例
            point = center + (radius * data[i] / 100.0) * direction
            data_points.append(point)

        data_polygon = Polygon(*data_points, color=YELLOW, fill_color=YELLOW, fill_opacity=0.35, stroke_width=3)
        dots = VGroup(*[Dot(point, color=RED, radius=0.08) for point in data_points])

        

        # ========== 动画播放 ==========
        self.add(grid_polys, axis_lines)
        self.play(Write(score_labels), run_time=0.8)          # 显示分数刻度
        self.play(Write(label_group), run_time=1.5)
        self.play(DrawBorderThenFill(data_polygon), run_time=1.2)
        self.play(GrowFromCenter(dots), run_time=0.8)
        self.wait(1)

        # ========== 6. 添加数值标注（显示具体分数） ==========
        value_labels = VGroup()
        for i, point in enumerate(data_points):
            direction = np.array([np.cos(angles[i]), np.sin(angles[i]), 0])
            # 数值文本放在数据点外侧稍远位置
            value_pos = point + 0.35 * direction
            # 显示整数分数，可改为 f"{data[i]:.1f}" 显示一位小数
            value_text = Text(f"{int(data[i])}", font_size=22, color=GREEN)
            value_text.move_to(value_pos)
            value_labels.add(value_text)
        self.play(FadeIn(value_labels, shift=UP, run_time=1))
        self.wait(15)

        