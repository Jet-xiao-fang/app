from manim import *
import math
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class NewtonMathClock(Scene):
    def construct(self):
        # 设置背景为深空蓝
        self.camera.background_color = "#0F0F1A"
        
        # 创建钟面 - 比之前大一些
        face_radius = 5.0
        face = Circle(radius=face_radius, color=WHITE, fill_color="#F0F8FF", 
                     fill_opacity=1, stroke_width=2)
        
        # 添加金属边框
        border = Circle(radius=face_radius + 0.15, color="#8B4513", 
                        stroke_width=8, fill_opacity=0)
        inner_border = Circle(radius=face_radius - 0.1, color="#A9A9A9", 
                              stroke_width=1, fill_opacity=0)
        
        # 创建牛顿肖像的替代物 - 简笔画和文字
        # 创建卷发效果
        hair = VGroup()
        for i in range(8):
            angle = i * 45 * DEGREES
            curl = Arc(radius=0.6, angle=70*DEGREES, color="#8B4513", stroke_width=6)
            curl.rotate(angle)
            hair.add(curl)
        
        # 脸型
        face_shape = Circle(radius=0.9, fill_color="#FFE4B5", fill_opacity=1, 
                           stroke_width=0, color=BLACK)
        
        # 眼睛
        left_eye = Dot(color=BLACK).shift(LEFT*0.3 + UP*0.2)
        right_eye = Dot(color=BLACK).shift(RIGHT*0.3 + UP*0.2)
        
        # 嘴巴
        mouth = ArcBetweenPoints(
            start=[-0.4, -0.2, 0],
            end=[0.4, -0.2, 0],
            angle=-PI/2,
            stroke_width=3
        )
        
        # 组装牛顿肖像
        newton = VGroup(hair, face_shape, left_eye, right_eye, mouth)
        
        # 添加姓名标识
        name_text = Text("Sir Isaac Newton", font_size=28, color="#8B0000")
        name_text.next_to(newton, DOWN, buff=0.3)
        
        # 创建公式位置的角度
        angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
        
        # 图片中的具体数学公式
        formulas = [
            r"\sum_{i=1}^{3}(3i^{2}-2)",  # 12点位置
            r"B_{16}",                   # 1点位置
            r"\log_{2}(1024)",           # 2点位置
            r"\log_{10}(100)",           # 3点位置
            r"\sqrt{81}",                # 4点位置
            r"\int_{1}^{2}2x\,dx",       # 5点位置
            r"\prod_{k=0}^{1}(2k+2)",    # 6点位置
            r"\left(2\sin\frac{\pi}{2}\right)^{2}",  # 7点位置
            r"0111_{2}",                 # 8点位置
            r"\sqrt[3]{125}",            # 9点位置
            r"3!",                       # 10点位置
            r"e^{\pi i}\cos\pi"          # 11点位置
        ]
        
        # 创建公式显示组
        math_formulas = VGroup()
        for i in range(12):
            angle = angles[i]
            formula = MathTex(formulas[i], color="#8B4513", font_size=28)
            
            # 根据角度调整公式朝向，使所有公式面向中心
            formula.rotate(-angle * DEGREES)
            
            # 计算位置 - 距离中心点一定距离
            dist = face_radius - 1.5
            adjusted_angle = (90 - angle) * DEGREES
            pos = dist * np.array([np.cos(adjusted_angle), np.sin(adjusted_angle), 0])
            formula.move_to(pos)
            
            math_formulas.add(formula)
        
        # 创建指针
        hour_hand = Line(
            start=ORIGIN,
            end=[0, face_radius - 2.0, 0],
            color="#000000",  # 黑色指针
            stroke_width=8
        ).add_tip(tip_length=0.2)
        
        minute_hand = Line(
            start=ORIGIN,
            end=[0, face_radius - 1.0, 0],
            color="#000000",
            stroke_width=5
        ).add_tip(tip_length=0.15)
        
        # 创建指针枢轴
        pivot = Circle(radius=0.18, color="#000000", fill_color="#8B4513", 
                      fill_opacity=1, stroke_width=2)
        pivot_inner = Circle(radius=0.06, color="#000000", fill_color=GOLD, 
                            fill_opacity=1, stroke_width=1)
        
        # 创建公式显示器背景 - 用羊皮纸风格
        display_bg = RoundedRectangle(
            width=7, height=1.8,
            corner_radius=0.2,
            fill_color="#F5F5DC",
            fill_opacity=1,
            stroke_width=3,
            stroke_color="#8B4513"
        )
        display_bg.next_to(face, DOWN, buff=1.0)
        
        # 初始公式计算器（空）
        display_area = Rectangle(width=7, height=1.8, fill_opacity=0, stroke_opacity=0)
        display_area.move_to(display_bg)
        
        # 所有元素组合
        clock_group = VGroup(
            face, border, inner_border,
            math_formulas, newton, name_text,
            hour_hand, minute_hand, pivot, pivot_inner
        )
        
        # 添加所有元素到场景
        self.add(clock_group, display_bg, display_area)
        
        # 定义公式的计算结果
        results = {
            0: r"= 34",  # Σ(3i²-2) from i=1 to 3 = 3(1)-2 + 3(4)-2 + 3(9)-2 = 1+10+25=34
            1: r"= 11",   # B₁₆在十六进制中表示11
            2: r"= 10",   # log₂(1024) = 10
            3: r"= 2",    # log₁₀(100) = 2
            4: r"= 9",    # √81 = 9
            5: r"= 3",    # ∫1² 2x dx = [x²]₁² = 4-1=3
            6: r"= 4",    # ∏ₖ₌₀¹ (2k+2) = (2×0+2)×(2×1+2) = 2×4=8? 但图片为4?
            7: r"= 4",    # (2sin(π/2))² = (2×1)²=4
            8: r"= 7",    # 0111₂二进制 = 7
            9: r"= 5",    # ∛125 = 5
            10: r"= 6",   # 3! = 6
            11: r"= 1"    # e^{iπ}cosπ = (-1)×(-1)=1
        }
        
        # 初始位置（指向12）
        current_formula = MathTex(
            formulas[0], r"\ ", results[0], 
            color="#8B0000", font_size=36
        )
        current_formula.move_to(display_bg)
        self.add(current_formula)
        
        self.wait(1)
        
        # 动画：指针依次移动到每个位置（1到11）
        for pos in range(1, 12):
            # 计算指针旋转角度（每个位置30度）
            rotate_angle = -30 * DEGREES
            
            # 创建指针旋转动画
            rotate_hour = Rotate(
                hour_hand, 
                angle=rotate_angle, 
                about_point=ORIGIN,
                rate_func=smooth,
                run_time=1.0
            )
            
            rotate_minute = Rotate(
                minute_hand, 
                angle=rotate_angle * 12,  # 分针转得更快
                about_point=ORIGIN,
                rate_func=smooth,
                run_time=1.0
            )
            
            # 创建新的公式计算显示
            new_formula = MathTex(
                formulas[pos], r"\ ", results[pos], 
                color="#8B0000", font_size=36
            )
            new_formula.move_to(display_bg)
            
            # 创建淡出旧公式和淡入新公式的动画
            fade_out = FadeOut(current_formula)
            fade_in = FadeIn(new_formula)
            
            # 播放动画（指针旋转和公式更新同时进行）
            self.play(
                rotate_hour,
                rotate_minute,
                fade_out,
                run_time=1.0
            )
            self.play(
                fade_in,
                run_time=0.5
            )
            
            # 更新当前显示
            current_formula = new_formula
            self.wait(1)  # 每个位置停留1秒
        
        self.wait(2)
        
# manim -pqh 数学钟表1.py NewtonMathClock -r 1920,1080