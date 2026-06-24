from manim import *
import numpy as np
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class RichCurlAmpere3D(ThreeDScene):
    def construct(self):
        # ============================================================
        # 1. 物理参数与场函数
        # ============================================================
        epsilon = 0.3
        
        # 磁场 B = (-y, x) / (r^2 + epsilon)
        def b_field(pos):
            x, y, z = pos
            r2 = x**2 + y**2 + epsilon
            # 返回三维向量 (z方向为0)
            return np.array([-y / r2, x / r2, 0])
        
        # 旋度 Z 分量（用于热力图颜色映射）
        def curl_z_value(x, y):
            r2 = x**2 + y**2
            D = r2 + epsilon
            return (2 * epsilon - 2 * x**2 + 2 * y**2) / (D**2)

        # ============================================================
        # 2. 构建三维场景基础
        # ============================================================
        # 三维坐标轴（带浅色网格）
        axes = ThreeDAxes(
            x_range=[-6, 6, 2],
            y_range=[-6, 6, 2],
            z_range=[-1, 1, 1],
            axis_config={"include_numbers": False},
            z_axis_config={"stroke_opacity": 0.3}
        )
        # 添加一个半透明的辅助平面，帮助定位深度
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1, "stroke_opacity": 0.2}
        )
        grid.rotate(PI/2, axis=RIGHT)  # 平放在 z=0 平面
        grid.shift(OUT * 0.1) # 稍微前移避免闪烁

        # ============================================================
        # 3. 旋度热力图（散布在 z=0 平面上，带有轻微高度变化以示深度）
        # ============================================================
        heatmap_dots = VGroup()
        max_curl = 2.0 / epsilon
        
        for x in np.linspace(-5, 5, 25):
            for y in np.linspace(-5, 5, 25):
                val = curl_z_value(x, y)
                norm_val = np.clip(val / max_curl, -0.5, 0.5) + 0.5
                color = interpolate_color(BLUE, RED, norm_val)
                # 让圆点略微抬高 z 轴，使其浮在平面上（3D效果）
                dot = Dot3D(
                    point=[x, y, 0.02], 
                    color=color,
                    radius=0.08,
                    fill_opacity=0.8
                )
                heatmap_dots.add(dot)

        # ============================================================
        # 4. 主磁场向量场（3D箭头，略微悬浮）
        # ============================================================
        vector_field = ArrowVectorField(
            b_field,
            x_range=[-5, 5, 0.8],
            y_range=[-5, 5, 0.8],
            colors=[BLUE, GREEN, RED],
            stroke_width=2,
        )
        # 将整个向量场向前移动一点，使其浮在热力图上方
        vector_field.shift(OUT * 0.05)

        # ============================================================
        # 5. 物理元件：3D导线（发光圆柱）与电流标记
        # ============================================================
        # 使用 Cylinder 模拟通电导线（高度很薄，看起来像圆盘）
        wire = Cylinder(
            radius=0.3, 
            height=0.2, 
            fill_color=YELLOW, 
            fill_opacity=0.9,
            stroke_width=0
        )
        wire.shift(OUT * 0.1)  # 置于中心
        
        # 导线周围的发光光晕
        glow = Sphere(radius=0.7, color=YELLOW, fill_opacity=0.15, stroke_width=0)
        glow.shift(OUT * 0.1)
        
        # 电流方向标记（⊙ 表示流向屏幕外，对应逆时针磁场）
        current_label = Text("I ⊙", font_size=30, color=YELLOW)
        current_label.next_to(wire, UP * 1.5, buff=0.1)
        # 由于3D视角，给标签加点偏移
        current_label.shift(OUT * 0.5)

        # ============================================================
        # 6. 宏观安培环路（三维虚线圆）
        # ============================================================
        loop_radius = 2.8
        amperian_loop = Circle(
            radius=loop_radius, 
            color=WHITE, 
            stroke_width=2, 
            stroke_opacity=0.5
        )
        amperian_loop.shift(OUT * 0.02)
        
        # 环路上的切向指示箭头（三维放置）
        tangent_arrows = VGroup()
        for angle in [0, PI/2, PI, 3*PI/2]:
            pos = np.array([loop_radius*np.cos(angle), loop_radius*np.sin(angle), 0.02])
            dir_vec = np.array([-np.sin(angle), np.cos(angle), 0])
            arrow = Arrow(
                start=pos - dir_vec*0.4, 
                end=pos + dir_vec*0.4,
                color=WHITE,
                stroke_width=4,
                buff=0
            )
            tangent_arrows.add(arrow)
        
        loop_label = MathTex(r"\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I", font_size=28)
        loop_label.next_to(amperian_loop, UR, buff=0.5)
        loop_label.shift(OUT * 0.5)

        # ============================================================
        # 7. 核心视觉：双桨轮（三维化）
        # ============================================================
        def create_3d_paddle_wheel(color=WHITE, radius=0.35):
            """创建三维十字桨轮（带薄片感）"""
            base = VGroup(
                Circle(radius=radius, color=color, fill_opacity=0.2, stroke_width=2),
                Line(LEFT*radius, RIGHT*radius, color=color, stroke_width=4),
                Line(UP*radius, DOWN*radius, color=color, stroke_width=4),
            )
            base.shift(OUT * 0.15)  # 浮在平面上
            return base
        
        paddle_center = create_3d_paddle_wheel(color=RED)
        paddle_center.move_to([0, 0, 0])
        paddle_center_label = Text("桨轮A (旋度≠0)", font_size=18, color=RED).next_to(paddle_center, DOWN, buff=0.3)
        paddle_center_label.shift(OUT * 0.2)
        
        paddle_outer = create_3d_paddle_wheel(color=BLUE)
        paddle_outer.move_to([2.5, 2.0, 0])
        paddle_outer_label = Text("桨轮B (旋度≈0)", font_size=18, color=BLUE).next_to(paddle_outer, DOWN, buff=0.3)
        paddle_outer_label.shift(OUT * 0.2)

        # ============================================================
        # 8. 动态粒子流（沿磁感线运动的粒子群）
        # ============================================================
        particles = VGroup()
        # 创建多圈层粒子：半径从 1.0 到 4.8，每圈 8-12 个
        for r in np.linspace(1.0, 4.8, 6):
            num_dots = max(8, int(12 - r * 1.5))
            for i in range(num_dots):
                angle = i * 2 * PI / num_dots + np.random.uniform(0, 0.3)
                dot = Dot(radius=0.07, color=GREEN)
                # 为每个粒子存储运动参数
                dot.r = r
                dot.angle = angle
                # 速度与 1/r 成正比（近快远慢，符合磁场强度变化）
                dot.speed = 1.2 / (r + 0.2)
                dot.move_to([r * np.cos(angle), r * np.sin(angle), 0.1])  # 稍微抬高
                particles.add(dot)
        
        # 定义粒子更新函数（利用 dt 实现平滑运动）
        def update_particles(mob, dt):
            for dot in mob:
                dot.angle += dot.speed * dt
                # 计算新位置
                new_x = dot.r * np.cos(dot.angle)
                new_y = dot.r * np.sin(dot.angle)
                dot.move_to([new_x, new_y, 0.1])
        
        particles.add_updater(update_particles)

        # ============================================================
        # 9. 标题与公式（三维空间中的文字）
        # ============================================================
        title = Text("三维旋度与安培定律", font_size=32).to_edge(UP)
        title.shift(OUT * 1)  # 将文字拉到前方
        
        formula1 = MathTex(r"\nabla \times \mathbf{B} = \mu_0 \mathbf{J}", font_size=36)
        formula1.next_to(title, DOWN, buff=0.3)
        formula1.shift(OUT * 1)
        
        formula2 = MathTex(r"\text{内部: } \nabla \times \mathbf{B} \neq 0", font_size=30, color=RED)
        formula2.next_to(formula1, DOWN, aligned_edge=LEFT)
        formula2.shift(OUT * 1)
        
        formula3 = MathTex(r"\text{外部: } \nabla \times \mathbf{B} = 0", font_size=30, color=BLUE)
        formula3.next_to(formula2, DOWN, aligned_edge=LEFT)
        formula3.shift(OUT * 1)

        # ============================================================
        # 10. 动画序列（多角度 + 动态演示）
        # ============================================================
        
        # 设置初始相机视角（俯视 + 旋转角度）
        self.set_camera_orientation(phi=70 * DEGREES, theta=-30 * DEGREES, distance=12)
        
        # 添加基础元素
        self.add(axes, grid, title, formula1)
        self.play(Create(vector_field), run_time=3)
        self.wait()
        
        # 显示热力图和导线
        self.play(FadeIn(heatmap_dots, scale=0.8), run_time=2)
        self.play(FadeIn(glow), FadeIn(wire), Write(current_label))
        self.wait()
        
        # 显示中心旋度公式
        self.play(Write(formula2))
        self.wait()
        
        # 显示安培环路
        self.play(
            Create(amperian_loop),
            Create(tangent_arrows),
            Write(loop_label)
        )
        self.wait()
        
        # 注入桨轮和粒子流（粒子流从此刻开始自动运行）
        self.play(
            FadeIn(paddle_center, scale=0.5),
            Write(paddle_center_label),
            FadeIn(paddle_outer, scale=0.5),
            Write(paddle_outer_label),
            FadeIn(particles),  # 粒子出现
            run_time=2
        )
        self.wait()

        # 核心对比动画：中心桨轮旋转，外部桨轮平移（不自转）
        self.play(
            Rotate(paddle_center, angle=6*PI, about_point=paddle_center.get_center(), rate_func=linear),
            paddle_outer.animate.shift(LEFT * 1.5 + DOWN * 1.0),
            run_time=5,
            rate_func=linear
        )
        self.wait()
        
        # 显示外部旋度为零的公式
        self.play(Write(formula3))
        self.wait(2)

        # 相机运动：从俯视切换到侧面，展示三维深度
        self.move_camera(phi=40 * DEGREES, theta=-60 * DEGREES, run_time=3)
        self.wait(2)
        
        # 最后旋转相机，让观众从各个角度观察粒子环绕运动
        self.begin_ambient_camera_rotation(rate=0.2, about="theta")
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(2)

        # 总结语
        summary_text = Text(
            "结论: 旋度度量『局部』旋转 (红桨轮) vs 全局环流 (粒子绕圈)",
            font_size=26,
            color=YELLOW
        ).to_edge(DOWN)
        summary_text.shift(OUT * 1)
        self.play(Write(summary_text))
        self.wait(3)
        
# manim -pqh 梯度.py RichCurlAmpere3D   # 梯度演示