from manim import *
import numpy as np

class NestedCirclesWithTrace(Scene):
    def construct(self):
        # ---------- 参数配置 ----------
        # 每个圆的半径、角速度、初始相位
        circles_config = [
            {"radius": 2.0, "speed": 1.0,  "phase": 0},
            {"radius": 1.2, "speed": -2.5, "phase": PI/2},
            {"radius": 0.6, "speed": 4.0,  "phase": PI/4},
            {"radius": 0.3, "speed": -6.0, "phase": 0},   # 最后一个最小圆
        ]

        # 颜色方案
        colors = [BLUE, TEAL, GREEN, YELLOW]
        trace_color = PURPLE

        # 时间参数（使用ValueTracker方便更新）
        t = ValueTracker(0)

        # ---------- 创建所有圆和连接线 ----------
        circles = VGroup()       # 所有圆（半透明）
        centers = VGroup()       # 圆心点（小圆点）
        lines = VGroup()         # 圆心之间的连接线（可选）
        dot = None               # 最后一个圆的轨迹点

        # 先计算初始位置，以便创建所有对象
        def get_positions(time):
            """计算所有圆的圆心位置（绝对坐标）和最后一个圆的边缘点"""
            positions = [np.array([0., 0., 0.])]  # 第一个圆固定于原点
            # 逐级计算圆心
            for i, cfg in enumerate(circles_config):
                r = cfg["radius"]
                omega = cfg["speed"]
                phi = cfg["phase"]
                # 前一个圆心 + 当前圆的旋转向量
                prev = positions[-1]
                angle = omega * time + phi
                new_center = prev + np.array([r * np.cos(angle), r * np.sin(angle), 0])
                positions.append(new_center)
            # positions[0]是原点，positions[1]是第一个圆圆心，...，positions[-1]是最后一个圆的圆心
            # 最后一个圆的边缘点（轨迹点）：圆心 + 半径向量（取当前角度）
            last_cfg = circles_config[-1]
            r_last = last_cfg["radius"]
            omega_last = last_cfg["speed"]
            phi_last = last_cfg["phase"]
            angle_last = omega_last * time + phi_last
            edge_point = positions[-1] + np.array([r_last * np.cos(angle_last), r_last * np.sin(angle_last), 0])
            return positions, edge_point

        # 初始创建
        init_positions, init_edge = get_positions(0)

        # 创建每个圆
        for i, cfg in enumerate(circles_config):
            center = init_positions[i]   # 第i个圆的圆心（注意positions[0]是原点，positions[1]是第一个圆的圆心）
            radius = cfg["radius"]
            color = colors[i % len(colors)]
            circle = Circle(radius=radius, color=color, stroke_width=2, stroke_opacity=0.6)
            circle.move_to(center)
            circles.add(circle)

            # 圆心小点
            dot_center = Dot(center, radius=0.05, color=color)
            centers.add(dot_center)

            # 连接前一个圆心到当前圆心的线（除了第一个）
            if i > 0:
                prev_center = init_positions[i-1]
                line = Line(prev_center, center, color=color, stroke_width=1, stroke_opacity=0.5)
                lines.add(line)

        # 最后一个圆的轨迹点（将一直在最后一个圆的边缘上）
        trace_point = Dot(init_edge, color=RED, radius=0.1)
        # 保存轨迹点以便后续更新
        self.trace_point = trace_point

        # 轨迹曲线（用ParametricFunction在最后绘制，但我们这里手动累积轨迹点）
        # 使用 TracedPath 更简单，它会自动追踪一个点的运动路径
        traced_path = TracedPath(trace_point.get_center, stroke_color=trace_color, stroke_width=2)

        # ---------- 将所有对象加入场景 ----------
        self.add(circles, centers, lines, trace_point, traced_path)

        # ---------- 更新函数 ----------
        # 我们需要随着时间更新所有圆、圆心、连线以及轨迹点的位置
        def update_objects(time):
            positions, edge = get_positions(time)
            # 更新每个圆和圆心
            for i, circle in enumerate(circles):
                circle.move_to(positions[i])
            for i, dot_center in enumerate(centers):
                dot_center.move_to(positions[i])
            # 更新连线
            for i, line in enumerate(lines):
                # 第i条线连接 positions[i] 和 positions[i+1]
                line.put_start_and_end_on(positions[i], positions[i+1])
            # 更新轨迹点（最后一个圆的边缘点）
            trace_point.move_to(edge)
            # 注意 TracedPath 会自动追踪 trace_point 的运动，无需额外操作

        # 使用 updater 使所有对象随 t 变化
        # 但是 TracedPath 已经追踪 trace_point，所以只需更新 trace_point 的位置即可
        # 我们用一个 updater 来更新所有几何体
        def updater(obj):
            # obj 是任意对象，但我们直接使用外部变量 t 的值
            time = t.get_value()
            positions, edge = get_positions(time)
            for i, circle in enumerate(circles):
                circle.move_to(positions[i])
            for i, dot_center in enumerate(centers):
                dot_center.move_to(positions[i])
            for i, line in enumerate(lines):
                line.put_start_and_end_on(positions[i], positions[i+1])
            trace_point.move_to(edge)
            # traced_path 自动更新

        # 我们可以将所有对象放入一个VGroup，然后添加更新器
        group = VGroup(circles, centers, lines, trace_point)
        group.add_updater(updater)

        # 添加一个指示“最后一个圆”的发光环（可选）
        last_circle = circles[-1]
        glow = last_circle.copy().set_color(YELLOW).set_stroke(opacity=0.3, width=4)
        glow.add_updater(lambda g: g.move_to(last_circle.get_center()))  # 跟随最后一个圆
        self.add(glow)

        # ---------- 运行动画 ----------
        # 让 t 从 0 变化到 4*PI，持续 12 秒
        self.play(t.animate.set_value(4 * PI), run_time=12, rate_func=linear)
        self.wait(2)
        # 淡出
        self.play(FadeOut(VGroup(group, glow, traced_path)))
    
# manim -pqh 分形螺旋.py NestedCirclesWithTrace