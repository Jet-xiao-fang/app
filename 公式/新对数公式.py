from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantLogarithmicFormulas(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = GRAY_D
        
        # 2. 定义公式数据列表（每个元素是一个字典，包含公式、中文解释、颜色和缩放比例）
        items = [
            {"formula": r"\log_b(xy) = \log_b x + \log_b y", 
             "text": "对数乘法公式", 
             "color": BLUE,
             "scale": 0.9},
            {"formula": r"\log_b\left(\frac{x}{y}\right) = \log_b x - \log_b y", 
             "text": "对数除法公式", 
             "color": BLUE,
             "scale": 0.8},
            {"formula": r"\log_b(x^a) = a \cdot \log_b x", 
             "text": "对数幂公式", 
             "color": BLUE,
             "scale": 0.9},
            {"formula": r"\log_b b = 1", 
             "text": "底数对数", 
             "color": RED,
             "scale": 0.9},
            {"formula": r"\log_b 1 = 0", 
             "text": "1的对数", 
             "color": RED,
             "scale": 0.9},
            {"formula": r"b^{\log_b x} = x", 
             "text": "对数与指数的互逆关系", 
             "color": RED,
             "scale": 0.7},
            {"formula": r"\log_b a = \frac{1}{\log_a b}", 
             "text": "倒数关系", 
             "color": PINK,
             "scale": 0.7},
            {"formula": r"\log_b a = \frac{\log_c a}{\log_c b}", 
             "text": "换底公式", 
             "color": GREEN,
             "scale": 0.7},
            {"formula": r"\log_b x = \frac{\ln x}{\ln b}", 
             "text": "自然对数表达式", 
             "color": GREEN,
             "scale": 0.7},
            {"formula": r"\log_b x = \frac{\log_k x}{\log_k b}", 
             "text": "一般换底公式", 
             "color": GREEN,
             "scale": 0.7}
        ]
        
        info=items[0]
        name = Text(info["text"], font="STXingkai", font_size=54, color=info["color"])
        formula = MathTex(info["formula"], color=WHITE).scale(2)
        
        name.next_to(formula, DOWN, buff=0.5)
        
        Group(name, formula).move_to(ORIGIN)
        
        self.play(
            Write(name),
            FadeIn(formula, shift=UP * 0.3,scale=0.8),
            run_time=1
        )
        self.wait(0.5)
        
        for i in range(1, len(items)):
            old_name = name
            old_formula = formula
            
            info = items[i]
            name = Text(info["text"], font="STXingkai", font_size=54, color=info["color"])
            formula = MathTex(info["formula"], color=WHITE).scale(2)
            
            name.next_to(formula, DOWN, buff=0.5)
            Group(name, formula).move_to(ORIGIN)
            
            self.play(
                ReplacementTransform(old_name, name),
                ReplacementTransform(old_formula, formula),
                run_time=1
            )
        
# manim -pqh  新对数公式.py ImportantLogarithmicFormulas