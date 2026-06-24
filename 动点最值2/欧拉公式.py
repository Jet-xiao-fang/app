from manim import *
import numpy as np

class EulerFormulaScene(Scene):
    def construct(self):
        # 1. 设置画布
        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        plane.add_coordinates()
        self.add(plane)

        # 2. 初始元素：单位圆、起始点、向量
        circle = Circle(radius=1, color=YELLOW, stroke_width=2)
        dot = Dot(plane.n2p(1+0j), color=RED)
        vec = Vector(RIGHT, color=GREEN)
        vec.put_start_and_end_on(plane.n2p(0+0j), plane.n2p(1+0j))

        # 3. 公式（使用 Tex）
        euler_formula = MathTex(
            "e^{i\\theta}", "=", "\\cos\\theta", "+", "i\\sin\\theta"
        ).to_corner(UL)
        # 为公式的不同部分设置颜色，使其与图形对应
        euler_formula.set_color_by_tex("e^{i\\theta}", YELLOW)
        euler_formula.set_color_by_tex("\\cos\\theta", RED)
        euler_formula.set_color_by_tex("i\\sin\\theta", BLUE)

        # 添加一个角度标签的占位符，稍后更新
        theta_tex = MathTex("\\theta = 0.00").to_corner(DR)

        # 4. 将所有初始元素添加到场景
        self.play(Create(circle), Write(euler_formula), Write(theta_tex))
        self.add(dot, vec)

        # 5. 动画循环：让点沿单位圆运动
        # 使用 ValueTracker 来控制角度 theta
        theta = ValueTracker(0)

        # 更新函数：根据 theta 的值更新点、向量和角度标签的位置
        dot.add_updater(
            lambda d: d.move_to(plane.n2p(np.exp(1j * theta.get_value())))
        )
        vec.add_updater(
            lambda v: v.put_start_and_end_on(
                plane.n2p(0+0j),
                plane.n2p(np.exp(1j * theta.get_value()))
            )
        )
        theta_tex.add_updater(
            lambda t: t.become(
                MathTex(f"\\theta = {theta.get_value():.2f}").to_corner(DR)
            )
        )

        # 运行动画：让 theta 从 0 变化到 2*PI
        self.play(theta.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait()

        # 6. 在 theta = PI 时暂停，突出显示欧拉恒等式
        # 先让 theta 回到 PI
        self.play(theta.animate.set_value(PI), run_time=2)
        # 高亮公式
        self.play(
            euler_formula.animate.set_color(YELLOW),
            Flash(euler_formula, color=YELLOW, line_length=0.2, num_lines=20),
            run_time=2
        )
        self.wait(2)

        # 7. 淡出结束
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
# manim -pqh 欧拉公式.py EulerFormulaScene 