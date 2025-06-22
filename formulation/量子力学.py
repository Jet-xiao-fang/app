from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class QuantumCover(Scene):
    def construct(self):
        # 深空背景
        stars = VGroup(*[Dot(point=np.random.uniform(-7,7,3), 
                          radius=np.random.uniform(0.01,0.03),
                          color=BLUE_E) for _ in range(200)])
        self.add(stars)
        
        # 核心元素组 - 上下排列
        elements = VGroup()
        
        # 1. 海森堡矩阵
        matrix_tex = MathTex(
            r"\begin{pmatrix}"
            r"\sigma_x & 0 & -i\hbar \\ "
            r"0 & \sigma_y & 0 \\ "
            r"i\hbar & 0 & \sigma_z"
            r"\end{pmatrix}",
            color=YELLOW
        ).scale(0.7)  # 稍微放大一点
        matrix_label = Tex("海森堡矩阵", color=YELLOW, font_size=32).next_to(matrix_tex, DOWN)
        heisenberg = VGroup(matrix_tex, matrix_label)
        elements.add(heisenberg)
        
        # 2. 狄拉克反物质模型
        particle_sys = VGroup()
        for i in range(3):
            orbit = Circle(radius=0.8*i+0.5, color=GREEN_B, stroke_width=1.5)
            particle = Dot(point=orbit.point_from_proportion(0), 
                          color=GREEN, radius=0.15)
            particle_sys.add(orbit, particle)
        
        dirac_eq = MathTex(r"i\gamma^\mu \partial_\mu \psi = m\psi", 
                           color=GREEN, font_size=36)
        dirac_group = VGroup(particle_sys, dirac_eq)
        dirac_eq.next_to(particle_sys, DOWN, buff=0.3)
        elements.add(dirac_group)
        
        # 3. 薛定谔波函数
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"color": PINK},
        )
        wave_func = axes.plot(
            lambda x: np.sin(3*x)*np.exp(-0.2*x**2),
            color=PINK
        )
        schro_eq = MathTex(r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi", 
                           color=PINK, font_size=36)
        wave_group = VGroup(axes, wave_func, schro_eq)
        schro_eq.next_to(axes, DOWN, buff=0.3)
        elements.add(wave_group)
        
        # 上下排列元素
        elements.arrange(DOWN, buff=0.8, aligned_edge=ORIGIN)
        elements.center().shift(UP*0.5)  # 整体上移一点
        
        # 原子轨道装饰 - 移动到右上角
        atom_orbit = VGroup()
        for r in [1.2, 1.8]:
            orbit = Ellipse(width=r*1.5, height=r, color=BLUE_C, stroke_width=1.2)
            atom_orbit.add(orbit)
        nucleus = Dot(color=RED, radius=0.15)
        atom = VGroup(atom_orbit, nucleus).scale(0.7)
        atom.to_corner(UR, buff=1.0)  # 右上角
        
        # 动画序列
        self.play(
            LaggedStart(
                Create(atom_orbit),
                run_time=2
            )
        )
        self.play(
            LaggedStart(
                FadeIn(heisenberg, shift=UP),
                FadeIn(dirac_group, shift=UP),
                FadeIn(wave_group, shift=UP),
                GrowFromCenter(nucleus),
                lag_ratio=0.7
            )
        )
        
        # 粒子动画
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

# 运行命令: manim -pqh 量子力学.py QuantumCover -r 1920,1080
#  manim -pqh 量子力学.py QuantumCover -r 1920,1080