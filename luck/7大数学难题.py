from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MillenniumProblems(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#0F0F1A"
        
        # 1. 创建标题
        title = Text("千禧年七大数学难题", 
                    font="Microsoft YaHei",
                    font_size=48,
                    color=YELLOW).to_edge(UP, buff=1.5)
        
        # 2. 创建难题列表
        problems = [
            MathTex(r"\text{P vs NP问题}"),
            MathTex(r"\text{纳维-斯托克斯方程}"),
            MathTex(r"\text{庞加莱猜想}"),
            MathTex(r"\text{黎曼假设}"),
            MathTex(r"\text{杨-米尔斯理论}"),
            MathTex(r"\text{贝赫-斯维讷通-戴尔猜想}"),
            MathTex(r"\text{霍奇猜想}")
        ]
        
        # 难题的描述（分多行显示）
        descriptions = [
            VGroup(
                Text("是否所有能被计算机快速验证解的问题", font="Microsoft YaHei", font_size=20, color=BLUE),
                Text("也能被计算机快速求解？", font="Microsoft YaHei", font_size=20, color=BLUE)
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("描述流体运动的方程在三维空间中", font="Microsoft YaHei", font_size=20, color=GREEN),
                Text("是否存在始终光滑的解？", font="Microsoft YaHei", font_size=20, color=GREEN)
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("一个封闭的三维空间，若其中任意", font="Microsoft YaHei", font_size=20, color=YELLOW),
                Text("闭合曲线都能收缩为一点，是否必然", font="Microsoft YaHei", font_size=20, color=YELLOW),
                Text("是一个三维球面？（已解决）", font="Microsoft YaHei", font_size=20, color=YELLOW)
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("黎曼ζ函数的所有非平凡零点", font="Microsoft YaHei", font_size=20, color=PINK),
                Text("的实部是否都是1/2？", font="Microsoft YaHei", font_size=20, color=PINK)
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("描述基本粒子相互作用的杨-米尔斯理论", font="Microsoft YaHei", font_size=20, color=ORANGE),
                Text("在数学上能否严格成立？为何粒子", font="Microsoft YaHei", font_size=20, color=ORANGE),
                Text("具有质量（质量间隙）？", font="Microsoft YaHei", font_size=20, color=ORANGE)
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("能否通过一个代数方程的有理数解", font="Microsoft YaHei", font_size=20, color=PURPLE),
                Text("判断其对应的椭圆曲线的性质？", font="Microsoft YaHei", font_size=20, color=PURPLE)
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("复杂几何对象的形状（拓扑性质）", font="Microsoft YaHei", font_size=20, color=RED),
                Text("能否用特定代数方程的组合来描述？", font="Microsoft YaHei", font_size=20, color=RED)
            ).arrange(DOWN, buff=0.1)
        ]
        
        # 3. 调整问题大小
        for problem in problems:
            problem.scale(0.8)
        
        # 4. 创建序号列表
        indices = [Tex(f"{i+1}.", font_size=36) for i in range(7)]
        
        # 5. 创建完整的问题行（序号+问题+描述）
        problem_rows = []
        for i in range(7):
            # 创建问题和描述的组合
            problem_group = VGroup(problems[i], descriptions[i]).arrange(DOWN, buff=0.3)
            
            # 创建完整行（序号在左侧）
            row = VGroup(indices[i], problem_group).arrange(RIGHT, buff=0.5)
            problem_rows.append(row)
        
        # 6. 创建垂直布局（所有问题行垂直排列）
        all_rows = VGroup(*problem_rows).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        all_rows.next_to(title, DOWN, buff=0.8).to_edge(LEFT, buff=1.0)
        
        # 9. 动画展示
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)
        
        # 逐个展示问题行（带延迟）
        for i in range(7):
            self.play(
                FadeIn(indices[i], shift=RIGHT),
                FadeIn(problems[i], shift=UP),
                FadeIn(descriptions[i], shift=UP),
                run_time=1.5
            )
            self.wait(0.3)
        self.wait(1)
        # 清楚数据
        self.clear_scene()
        self.show_describe()
        
    def clear_scene(self):
        # 淡出所有内容，但保留背景色
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
    def show_describe(self):
        # 创建标题
        title = Text("千禧年七大数学难题", 
                    font="Microsoft YaHei", 
                    font_size=42, 
                    color=YELLOW,
                    weight=BOLD)
        title.shift(UP * 3.5)
        
        # 添加装饰线
        underline = Line(LEFT, RIGHT, color=BLUE_E).scale(1.5)
        underline.next_to(title, DOWN, buff=0.3)
        underline.set_stroke(width=3)
        
        # 添加副标题
        subtitle = Text("克雷数学研究所 · 2000年提出", 
                    font="Microsoft YaHei", 
                    font_size=28, 
                    color=GREY_B)
        subtitle.next_to(underline, DOWN, buff=0.3)
        
        # 动画展示标题部分
        self.play(
            FadeIn(title, shift=DOWN),
            run_time=1.2
        )
        self.play(
            Create(underline),
            Write(subtitle),
            run_time=1.5
        )
        self.wait(0.8)
        
        # 奖金信息 - 使用更醒目的设计
        prize_box = Rectangle(
            width=6, height=3,
            color=GOLD_E,
            fill_color=BLACK,
            fill_opacity=0.7,
            stroke_width=3
        )
        prize_box.next_to(subtitle, DOWN, buff=1.0)
        
        dollar_sign = Tex(r"\$", font_size=72, color=GOLD).move_to(prize_box.get_left() + RIGHT*0.8)
        million = Text("1,000,000", font_size=36, color=GOLD).next_to(dollar_sign, RIGHT, buff=0.1)
        prize_text = Text("每个问题的解决奖金", 
                        font="Microsoft YaHei", 
                        font_size=26, 
                        color=WHITE).next_to(million, DOWN, buff=0.3)
        
        prize_group = VGroup(prize_box, dollar_sign, million, prize_text)
        
        # 展示奖金信息
        self.play(
            DrawBorderThenFill(prize_box),
            run_time=1.2
        )
        self.play(
            FadeIn(dollar_sign, scale=1.5),
            FadeIn(million, shift=LEFT),
            run_time=1.0
        )
        self.play(
            Write(prize_text),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 已解决信息 - 使用卡片式设计
        solved_card = RoundedRectangle(
            width=9, height=1.8,
            color=GREEN_C,
            fill_color=BLACK,
            fill_opacity=0.7,
            corner_radius=0.2,
            stroke_width=3
        )
        solved_card.next_to(prize_box, DOWN, buff=1.2)
        
        solved_text = VGroup(
            Text("庞加莱猜想", font="Microsoft YaHei", font_size=24, color=GREEN_B),
            Text("格里戈里·佩雷尔曼 2003年解决", font="Microsoft YaHei", font_size=22, color=GREEN_C),
            Text("拒绝菲尔兹奖与百万美元奖金", font="Microsoft YaHei", font_size=20, color=GREY_B)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(solved_card)
        
        # 展示已解决信息
        self.play(
            DrawBorderThenFill(solved_card),
            run_time=1.0
        )
        self.play(
            LaggedStart(
                FadeIn(solved_text[0], shift=UP*0.3),
                FadeIn(solved_text[1], shift=UP*0.3),
                FadeIn(solved_text[2], shift=UP*0.3),
                lag_ratio=0.3
            ),
            run_time=2.0
        )
        self.wait(1.5)
        
        
        
        
        

# 运行命令：manim -pqh --format=png 7大数学难题.py MillenniumProblems -r 1920,1080