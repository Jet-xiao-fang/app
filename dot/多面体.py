from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class FixedPlatonicSolids(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        # 设置相机方位
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        # 创建八面体和它的标签
        octahedron = Octahedron(edge_length=2).set_fill(BLUE, opacity=0.6)
        oct_label = Text("正八面体").to_edge(UP, buff=3.5)  # 添加缓冲距离避免与边框重叠

        # 创建十二面体和它的标签
        dodecahedron = Dodecahedron(edge_length=1.5).set_fill(GREEN, opacity=0.7)
        dode_label = Text("正十二面体").to_edge(UP, buff=3.5)

        # 创建二十面体和它的标签
        icosahedron = Icosahedron(edge_length=1.5).set_fill(RED, opacity=0.7)
        ico_label = Text("正二十面体").to_edge(UP, buff=3.5)

        # 添加八面体
        self.play(Create(octahedron))
        self.add_fixed_in_frame_mobjects(oct_label)  # 确保标签固定在屏幕上方
        self.play(Write(oct_label))

        # 开始环绕相机旋转
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)

        # 移除八面体并展示十二面体
        self.play(FadeOut(octahedron), FadeOut(oct_label))
        self.play(Create(dodecahedron))
        self.add_fixed_in_frame_mobjects(dode_label)
        self.play(Write(dode_label))
        self.wait(5)

        # 移除十二面体并展示二十面体
        self.play(FadeOut(dodecahedron), FadeOut(dode_label))
        self.play(Create(icosahedron))
        self.add_fixed_in_frame_mobjects(ico_label)
        self.play(Write(ico_label))
        self.wait(5)

# 渲染命令行指导（在命令行中运行下面命令）：
# manim -pqh --format=png 多面体.py FixedPlatonicSolids -r 1920,1080