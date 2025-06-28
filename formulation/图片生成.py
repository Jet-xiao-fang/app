from manim import *

# 配置使用xelatex编译和中文支持
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class PrincipleOfLeastActionStatic(Scene):
    def construct(self):
        # 设置背景颜色为浅灰色（提高可读性）
        self.camera.background_color = "#F5F5F5"
        
        # 创建标题（增大字体尺寸）
        title = Text("最小作用量原理参数解释", font_size=60, color="#B22222", weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # 添加标题下划线
        underline = Line(LEFT, RIGHT, color=BLUE_D, stroke_width=3)
        underline.width = title.width * 1.1
        underline.next_to(title, DOWN, buff=0.2)
        
        # 创建公式（增大公式尺寸，添加边框）
        formula_box = Rectangle(
            width=14,
            height=4,
            color=BLUE_D,
            stroke_width=2,
            fill_color="#E6F2FF",
            fill_opacity=0.8
        )
        
        explanation = VGroup(
            Text("δS: 作用量的变分", color="#8B0000", font_size=38),  # 深红
            Text("S: 作用量泛函", color="#006400", font_size=38),      # 深绿
            Text("L: 拉格朗日量", color="#00008B", font_size=38),      # 深蓝
            Text("T: 动能, V: 势能", color="#8B4513", font_size=38)   # 深棕
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        formula_box.move_to(ORIGIN)
        explanation.move_to(formula_box)
        
        # 添加拉格朗日量说明（增大尺寸）
        lagrange_def = MathTex(
            r"L = T - V \quad \text{(拉格朗日量)}",
            color=BLUE_D,
            font_size=36
        )
        lagrange_def.next_to(formula_box, DOWN, buff=0.8)
        
        # 添加版权信息（今日头条需要版权标识）
        footer = Text("© 爱物理的小方", font_size=24, color="#808080")
        footer.to_edge(DOWN, buff=0.3)
        
        # 将所有元素添加到场景
        content = VGroup(
            title,
            underline,
            formula_box,
            explanation,
            lagrange_def,
            footer
        )
        
        self.add(content)
        
    
# manim -pqh --format=png 测试.py PrincipleOfLeastActionStatic -r 1920,1080