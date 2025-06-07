from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
# config.frame_width = 6
# config.frame_height = 8

class QuantumCover(Scene):
    def construct(self):
        # 深空背景
        stars = VGroup(*[Dot(point=np.random.uniform(-7,7,3), 
                          radius=np.random.uniform(0.01,0.03),
                          color=BLUE_E) for _ in range(200)])
        self.add(stars)
        
        # 核心元素组
        elements = VGroup()
        
        # 1. 修复海森堡矩阵：使用 MathTex 替代 Matrix
        # 创建矩阵作为单个 MathTex 对象
        matrix_tex = MathTex(
            r"\begin{pmatrix}"
            r"\sigma_x & 0 & -i\hbar \\ "
            r"0 & \sigma_y & 0 \\ "
            r"i\hbar & 0 & \sigma_z"
            r"\end{pmatrix}",
            color=YELLOW
        ).scale(0.5)
        matrix_label = Tex("海森堡矩阵", color=YELLOW, font_size=24).next_to(matrix_tex, DOWN).scale(0.5)
        elements.add(VGroup(matrix_tex, matrix_label))
        
        # 2. 狄拉克反物质模型
        particle_sys = VGroup()
        for i in range(3):
            orbit = Circle(radius=0.8*i+0.5, color=GREEN_B, stroke_width=1.5).scale(0.5)
            particle = Dot(point=orbit.point_from_proportion(0), 
                          color=GREEN, radius=0.15).scale(0.5)
            particle_sys.add(orbit, particle)
        
        # 修复 Dirac 方程中的下标问题
        dirac_eq = MathTex(r"i\gamma^\mu \partial_\mu \psi = m\psi", 
                           color=GREEN, font_size=28)
        dirac_group = VGroup(particle_sys, dirac_eq)
        dirac_eq.next_to(particle_sys, DOWN, buff=0.5)
        elements.add(dirac_group)
        
        # 3. 薛定谔波函数
        wave_func = ParametricFunction(
            lambda t: np.array([t, np.sin(3*t)*np.exp(-0.2*t**2), 0]),
            t_range=[-3, 3], color=PINK
        )
        # 修复 Schrodinger 方程中的 \hat{H}
        schro_eq = MathTex(r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi", 
                           color=PINK, font_size=28)
        wave_group = VGroup(wave_func, schro_eq)
        schro_eq.next_to(wave_func, DOWN, buff=0.5)
        elements.add(wave_group)
        
        # 排列核心元素
        elements.arrange(RIGHT, buff=0.5)
        elements.shift(DOWN*0.5)
        
        # 原子轨道装饰
        atom_orbit = VGroup()
        for r in [1.2, 1.8]:
            orbit = Ellipse(width=r*1.5, height=r, color=BLUE_C, stroke_width=1.2)
            atom_orbit.add(orbit)
        nucleus = Dot(color=RED, radius=0.15)
        atom = VGroup(atom_orbit, nucleus).scale(0.6)
        atom.to_corner(DR, buff=1.0)
        
        # 动画序列
        self.play(
            LaggedStart(
                Create(atom_orbit),
                run_time=2
            )
        )
        self.play(
            LaggedStart(
                FadeIn(matrix_tex, shift=UP),
                FadeIn(dirac_group, shift=UP),
                FadeIn(wave_group, shift=UP),
                GrowFromCenter(nucleus),
                lag_ratio=0.7
            )
        )
        
        # 修复粒子动画：每个粒子沿自己的轨道运动
        particle_anims = []
        for i in range(1, len(particle_sys), 2):  # 只选择粒子对象
            particle = particle_sys[i]
            orbit = particle_sys[i-1]  # 对应的轨道
            particle_anims.append(MoveAlongPath(particle, orbit))
            
        self.play(
            *particle_anims,
            run_time=3,
            rate_func=linear
        )
        
        self.wait(3)
        
        # 输出静态帧
        # self.camera.capture_mobjects([stars, title_group, elements, atom])
        self.wait(0.5)

#  manim -pqh 量子力学.py QuantumCover -r 1920,1080