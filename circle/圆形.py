from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class OptimizedFormula(Scene):
    def construct(self):
        # 设置抖音风格的背景色（深紫色渐变）
        self.camera.background_color = "#0F0B1A"
        
        # 添加动态背景元素
        grid = NumberPlane(background_line_style={"stroke_color": "#261C3A"})
        self.add(grid)
        
        # 创建带渐变色的标题（使用中文）
        title = Text("看似复杂实则简单！", 
                   font="Microsoft YaHei",
                   font_size=48,
                   gradient=(BLUE_B, PINK)).shift(UP*1.5)
        
        # 放大公式并添加动态效果
        formula = MathTex(
            r"\sqrt{96 \times 97 \times 98 \times 99 + 1} = ?",
            font_size=42,
            color=GREEN
        )
        
        # 添加爆炸效果装饰
        explosion = Star(n=7, color=YELLOW).scale(0.4)
        explosion.next_to(formula, RIGHT)
        
        # 添加霓虹灯边框效果
        border = SurroundingRectangle(
            VGroup(title, formula),
            color=WHITE,
            buff=0.6,
            stroke_width=2,
            fill_color="#1A1029",
            fill_opacity=0.8,
            corner_radius=0.3
        )
        
        # 添加流动光效
        light = Line(LEFT*5, RIGHT*5, color=WHITE, stroke_width=2)
        light.set_opacity(0.3).shift(DOWN*0.5)
        light.add_updater(lambda m, dt: m.shift(RIGHT*0.5*dt))
        
        # 组合元素
        group = VGroup(border, title, formula, explosion, light)
        group.center()
        
        # 展示元素
        self.add(group)
        
        # 添加持续旋转的装饰元素
        rotating_star = Star(n=5, color=PINK).scale(0.2)
        rotating_star.add_updater(lambda m, dt: m.rotate(dt))
        rotating_star.move_to(UL*3)
        self.add(rotating_star)

# manim -pqh --format=png 圆形.py OptimizedFormula -r 1920,1080