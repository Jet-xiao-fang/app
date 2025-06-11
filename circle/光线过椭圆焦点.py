from manim import *
import numpy as np

class EllipseOptics(Scene):
    
    def construct(self):
        self.camera.background_color = "#263238"
        # 椭圆参数
        a = 3.0          # 长半轴
        c = 2.0          # 焦距
        b = np.sqrt(a**2 - c**2)  # 短半轴

        # 创建椭圆和焦点
        ellipse = Ellipse(width=2*a, height=2*b, color=WHITE)
        f1 = Dot(point=[-c, 0, 0], color=RED).scale(1.5)  # 焦点F1
        f2 = Dot(point=[c, 0, 0], color=GREEN).scale(1.5) # 焦点F2
        
        # 添加椭圆和焦点到场景
        self.play(
            Create(ellipse),
            Create(f1),
            Create(f2)
        )
        self.wait()

        # 生成椭圆上的采样点
        num_rays = 12  # 光线数量
        thetas = np.linspace(0, 2*PI, num_rays, endpoint=False)
        points = [ellipse.point_at_angle(theta) for theta in thetas]  # 椭圆上的点

        # 创建光线动画
        rays = VGroup()
        for p in points:
            # 入射光线（F1到椭圆上的点）
            incident = Line(f1.get_center(), p, color=YELLOW, stroke_width=2)
            # 反射光线（椭圆上的点到F2）
            reflected = Line(p, f2.get_center(), color=YELLOW, stroke_width=2)
            
            # 添加箭头提示
            incident.add_tip(tip_length=0.15)
            reflected.add_tip(tip_length=0.15)
            
            # 组合光线
            ray = VGroup(incident, reflected)
            rays.add(ray)

        # 动画序列：逐个显示光线路径
        self.play(
            LaggedStart(
                *[Succession(
                    Create(ray[0], run_time=1.5),  # 绘制入射光线
                    Create(ray[1], run_time=1.5)   # 绘制反射光线
                ) for ray in rays],
                lag_ratio=0.3
            )
        )
        self.wait(2)

        # 高亮显示光路传播过程
        for ray in rays:
            self.play(
                ShowPassingFlash(
                    ray.copy().set_color(WHITE).set_stroke(width=5),
                    time_width=0.5
                ),
                run_time=1.5
            )
        self.wait()

# manim -pqh 光线过椭圆焦点.py EllipseOptics -r 1920,1080