from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class StaticFormula(Scene):
    def construct(self):
        self.camera.background_color = "#263238"
        # 创建文字说明（支持LaTeX）
        title = Tex(r"看着难算、实际上是纸老虎", font_size=36, color=YELLOW)
        
        # 创建静态公式（带计算结果）
        formula = MathTex(r"\sqrt{96 \times 97 \times 98 \times 99 + 1} = ?",font_size=36)
        # 垂直排列文字和公式（文字在上，间距0.8个单位）
        
        group = VGroup(title, formula).arrange(DOWN, buff=0.8)
        # 居中显示组合
        group.move_to(ORIGIN)
        # 直接显示公式（无动画）
        self.add(group)

# manim -pqh --format=png 封面模板.py OptimizedFormula -r 1920,1080
