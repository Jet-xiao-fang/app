from manim import *

class FunctionSurface3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=8,
            z_length=4
        )
        
        # 定义曲面函数: f(u,v) -> (x,y,z)  注意参数是 u, v
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            return np.array([x, y, z])
        
        surface = Surface(
            lambda u, v: axes.c2p(*param_surface(u, v)),  # 必须转换到场景坐标
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, BLUE_E]  # 棋盘格效果便于观察起伏
        )
        
        # 添加颜色渐变效果（高级功能，需安装 manim 最新版）
        # surface.set_fill_by_value(axes=axes, colorscale=[BLUE, GREEN, YELLOW, RED])
        
        self.add(axes, surface)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-30 * DEGREES)
        
        # 展示曲面生成过程
        self.play(Create(surface, run_time=3))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        
# manim -pqh 3D.py FunctionSurface3D