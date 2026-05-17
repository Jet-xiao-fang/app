from manim import *
import random
from Logo import LogoScene  # 导入带 Logo 的基础场景类
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantPhysicsFormulas(LogoScene):
    def construct(self):
        # 设置宇宙深空背景
        self.camera.background_color = "#0F0F1A"
        self.add_logo()  # 添加 Logo
        # 公式数据：(LaTeX公式, 公式名称, 发现人及年份)
        formulas_data = [
            (r"F = ma", "牛顿第二定律", "艾萨克·牛顿 (1687年)"),
            (r"E = mc^2", "爱因斯坦质能方程", "阿尔伯特·爱因斯坦 (1905年)"),
            (r"F = G\frac{m_1 m_2}{r^2}", "万有引力定律", "艾萨克·牛顿 (1687年)"),
            (r"V = IR", "欧姆定律", "乔治·西蒙·欧姆 (1827年)"),
            (r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}", "高斯定律 (电磁学)", "卡尔·弗里德里希·高斯 (1835年)"),
            (r"\Delta S \geqslant \frac{Q}{T}", "热力学第二定律", "鲁道夫·克劳修斯 (1865年)"),
            (r"i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi", "薛定谔方程", "埃尔温·薛定谔 (1926年)"),
            (r"F = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})", "洛伦兹力公式", "亨德里克·洛伦兹 (1895年)"),
            (r"\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}", "薄透镜方程", "卡尔·弗里德里希·高斯 (约1840年)"),
            (r"E = h\nu", "光子能量公式", "马克斯·普朗克 (1900年)")
        ]
        
        # 逐个展示公式
        for idx, (formula_tex, name_text, info_text) in enumerate(formulas_data, start=1):
            # 创建公式名称
            name = Text(name_text, font="Microsoft YaHei", font_size=56, color=YELLOW)
            # 创建公式
            formula = MathTex(formula_tex, color=WHITE,font_size=54)
            # 适当缩放公式（若过长则缩小）
            if len(formula_tex) > 30:
                formula.scale(0.8)
            # 创建发现人及年份信息
            info = Text(info_text, font="Microsoft YaHei", font_size=42, color=BLUE_C)
            
            # 垂直排列：名称在上，公式居中，信息在下
            content = VGroup(name, formula, info).arrange(DOWN, buff=1.5, center=True)
            content.move_to(ORIGIN)
            
            # 显示当前公式 (先清除之前的，再显示新的)
            if idx > 1:
                # 清除上一个内容
                self.play(FadeOut(previous_content, shift=UP,scale=0.8), run_time=0.5)
            
            # 动画展示
            self.play(
                Write(name),
                Write(formula),
                FadeIn(info, shift=UP*0.3),
                run_time=1.5
            )
            self.wait(0.5)  # 停留观看
            previous_content = content  # 保存用于清除
        
        # 清除最后一个公式
        self.play(FadeOut(previous_content, shift=UP), run_time=0.5)
        
        self.wait(0.5)  # 短暂结束缓冲

# 运行命令：manim -pqh 新公式.py ImportantPhysicsFormulas