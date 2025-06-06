from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class StaticFormula(Scene):
    def construct(self):
        # 设置深色背景
        self.camera.background_color = "#0F0B1A"
        
        # 1. 创建文字元素 - 添加中文支持
        title = Text("数据分析", 
                    font="Microsoft YaHei",
                    font_size=48,
                    color=BLUE)
        
        text_col1_1 = Text("统计模型", 
                          font="Microsoft YaHei",
                          font_size=36,
                          color=YELLOW)
        
        text_col1_2 = Text("回归分析", 
                          font="Microsoft YaHei",
                          font_size=36,
                          color=YELLOW)
        
        text_col2_1 = Text("决策树", 
                          font="Microsoft YaHei",
                          font_size=36,
                          color=GREEN)
        
        text_col2_2 = Text("随机森林", 
                          font="Microsoft YaHei",
                          font_size=36,
                          color=GREEN)
        
        # 2. 构建列布局
        # 第一列垂直排列
        col1 = VGroup(text_col1_1, text_col1_2).arrange(
            DOWN, buff=0.8, aligned_edge=RIGHT
        )
        
        # 第二列垂直排列
        col2 = VGroup(text_col2_1, text_col2_2).arrange(
            DOWN, buff=0.8, aligned_edge=LEFT
        )
        
        # 关键修正：使用VGroup包裹两列并水平排列 ✅
        columns = VGroup(col1, col2).arrange(
            RIGHT, buff=2.0, aligned_edge=ORIGIN
        )
        
        # 3. 创建整体布局
        layout = VGroup(title, columns).arrange(
            DOWN, buff=1.5, aligned_edge=ORIGIN
        ).to_edge(UP).shift(DOWN*0.5)

        self.add(layout)
        
        # 4. 添加装饰元素
        line1 = Line(columns.get_left(), columns.get_right(), color=BLUE_D)
        line2 = Line(columns.get_left(), columns.get_right(), color=BLUE_D).shift(DOWN*1.5)
        
        # 5. 动画展示
        self.play(
            FadeIn(title.scale(1.2), shift=DOWN, run_time=1.5),
            Create(line1, run_time=1.0),
            Create(line2, run_time=1.0)
        )
        self.wait(0.5)
        
        # 第一列动画
        self.play(
            Write(text_col1_1, run_time=1.0),
            text_col1_1.animate.set_color(ORANGE)
        )
        self.play(
            Write(text_col1_2, run_time=1.0),
            text_col1_2.animate.set_color(ORANGE)
        )
        self.wait(0.5)
        
        # 第二列动画
        self.play(
            Write(text_col2_1, run_time=1.0),
            text_col2_1.animate.set_color(PURPLE)
        )
        self.play(
            Write(text_col2_2, run_time=1.0),
            text_col2_2.animate.set_color(PURPLE)
        )
        self.wait(1)
        
        # 6. 添加最终效果
        final_box = SurroundingRectangle(layout, color=BLUE, buff=0.8)
        self.play(Create(final_box), run_time=2)
        
        # 7. 版权信息
        copyright = Text("@数据分析师",
                        font="Microsoft YaHei",
                        font_size=24,
                        color=GREY).to_edge(DOWN)
        
        self.play(FadeIn(copyright, shift=UP), run_time=1.5)
        self.wait(3)

# 运行命令：manim -pqh --format=png 封面模板.py StaticFormula -r 1920,1080