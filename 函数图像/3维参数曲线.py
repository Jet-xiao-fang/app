from manim import *

class Basic3DShapes(ThreeDScene):
    def construct(self):
        # 创建三维坐标轴
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=10
        )
        
        # 创建一些几何体
        sphere = Sphere(radius=1).move_to([2, 2, 2])
        sphere.set_color(RED)
        
        cube = Cube(side_length=1.5).move_to([-2, -2, 1])
        cube.set_color(BLUE)
        
        torus = Torus(major_radius=1, minor_radius=0.3).move_to([0, 0, -2])
        torus.set_color(GREEN)
        
        # 文字标签
        labels = VGroup(
            MathTex("(2,2,2)").next_to(sphere, UP),
            MathTex("(-2,-2,1)").next_to(cube, DOWN),
            MathTex("Torus").next_to(torus, RIGHT)
        )
        
        self.add(axes, sphere, cube, torus, labels)
        
        # 设置初始相机角度（侧上方视角）
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # 动画：让相机环绕一周
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # 聚焦到球体
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, zoom=0.5, run_time=2)
        self.wait()
        
# manim -pqh 3维参数曲线.py Basic3DShapes