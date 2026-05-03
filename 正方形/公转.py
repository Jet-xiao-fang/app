from manim import *
import numpy as np

class SolarSystem(ThreeDScene):
    def construct(self):
        # 1. 设置相机
        self.set_camera_orientation(phi=0, theta=-90)  # 俯视视角

        # 2. 创建太阳
        sun = Sphere(radius=0.5, color=YELLOW).move_to(ORIGIN)
        self.add(sun)

        # 3. 行星数据：(名字, 颜色, 轨道半径, 公转周期年)
        planets_data = [
            ("水星", "#B2B2B2",  1.0, 0.24),
            ("金星", "#E6B856",  1.5, 0.62),
            ("地球", "#4A90D9",  2.0, 1.0),
            ("火星", "#C1440E",  2.8, 1.88),
            ("木星", "#C8B88A",  4.2, 11.86),
            ("土星", "#E0C080",  5.8, 29.46),
            ("天王星", "#6FD4D4", 7.5, 84.02),
            ("海王星", "#4169E1", 9.0, 164.8),
        ]

        # 动画总时长(秒)
        total_time = 10.0
        # 时间比例因子（动画10秒对应1个地球年）
        time_scale = total_time / 1.0

        planets_group = VGroup()
        orbits_group = VGroup()
        labels_group = VGroup()

        for name, color, radius, period_year in planets_data:
            # 公转速度 = 2*pi / (周期 * 时间比例)
            angular_velocity = (2 * np.pi) / (period_year * time_scale)

            planet = Sphere(radius=0.2, color=color).move_to([radius, 0, 0])
            orbit = Circle(radius=radius, color=BLUE, stroke_width=1).move_to(ORIGIN)

            # 添加标签
            label = Text(name, font_size=12).next_to(planet.get_center(), UP)

            # 添加更新器，让行星持续旋转
            planet.add_updater(lambda m, dt, av=angular_velocity: m.rotate(
                angle=av * dt, axis=OUT, about_point=ORIGIN))
            label.add_updater(lambda m: m.next_to(planet.get_center(), UP))

            planets_group.add(planet)
            orbits_group.add(orbit)
            labels_group.add(label)

        self.add(orbits_group, planets_group, labels_group)

        # 4. 播放动画
        self.wait(total_time)
        
# manim -pqh 公转.py SolarSystem