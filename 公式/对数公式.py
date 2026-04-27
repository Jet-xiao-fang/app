from manim import *

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantLogarithmicFormulas(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        
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
        
        # 3. 分割成左右两列（前5个左列，后5个右列）
        left_items = items[:5]   # 第1-5个公式
        right_items = items[5:]  # 第6-10个公式
        
        # 4. 创建左列的公式行
        left_formula_rows = []
        for i, item in enumerate(left_items):
            # 创建公式
            formula = MathTex(item["formula"])
            formula.scale(item["scale"])
            
            # 创建中文解释
            chinese_text = Text(item["text"], 
                               font="Microsoft YaHei", 
                               font_size=18, 
                               color=item["color"])
            
            # 创建序号
            index = Tex(f"{i+1}.", font_size=48)
            
            # 创建公式和中文的组合
            formula_group = VGroup(formula, chinese_text).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(index, formula_group).arrange(RIGHT, buff=0.2)
            left_formula_rows.append(row)
        
        # 5. 创建右列的公式行
        right_formula_rows = []
        for i, item in enumerate(right_items):
            # 创建公式
            formula = MathTex(item["formula"])
            formula.scale(item["scale"])
            
            # 创建中文解释
            chinese_text = Text(item["text"], 
                               font="Microsoft YaHei", 
                               font_size=18, 
                               color=item["color"])
            
            # 创建序号（序号从6开始）
            index = Tex(f"{i+6}.", font_size=48)
            
            # 创建公式和中文的组合
            formula_group = VGroup(formula, chinese_text).arrange(DOWN, buff=0.2)
            
            # 创建完整行（序号在左侧）
            row = VGroup(index, formula_group).arrange(RIGHT, buff=0.2)
            right_formula_rows.append(row)
        
        # 6. 垂直排列左右两列
        left_column = VGroup(*left_formula_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        right_column = VGroup(*right_formula_rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # 7. 将左右两列并排放置
        VGroup(left_column, right_column).arrange(RIGHT, buff=1.5)
        
        
        # 10. 收集所有需要动画的对象
        all_indices = []
        all_formulas = []
        all_chinese_texts = []
        
        # 收集左列的对象
        for row in left_formula_rows:
            all_indices.append(row[0])
            all_formulas.append(row[1][0])
            all_chinese_texts.append(row[1][1])
        
        # 收集右列的对象
        for row in right_formula_rows:
            all_indices.append(row[0])
            all_formulas.append(row[1][0])
            all_chinese_texts.append(row[1][1])
        
        # 逐个展示所有公式行（先左列后右列）
        for i in range(10):
            self.play(
                Write(all_indices[i]),
                Write(all_formulas[i]),
                FadeIn(all_chinese_texts[i], shift=UP*0.3),
                run_time=2
            )
            self.wait(0.2)
    
        self.wait(2)
        
# manim -pqh  对数公式.py ImportantLogarithmicFormulas