from manim import *

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class MathClock(Scene):  # 类名修正为MathClock
    def construct(self):
        # 设置深蓝色背景
        self.camera.background_color = "#0F0F1A"
        
        # 创建钟面
        face_radius = 4.0
        face = Circle(radius=face_radius, color=WHITE, fill_color="#121223", 
                     fill_opacity=1, stroke_width=1).scale(0.8)
        
        # 添加金属边框
        border = Circle(radius=face_radius + 0.1, color="#D4AF37", 
                       stroke_width=6, fill_opacity=0).scale(0.8)
        
        titile = Tex("数学钟表",color=BLUE).next_to(border,UP,buff = 1.5)
        self.add(titile)
        
        # 创建枢轴中心点
        pivot = Circle(radius=0.12, color=BLACK, fill_color="#D4AF37", 
                      fill_opacity=1, stroke_width=1)
        
        # 正确添加时钟数字
        hour_numbers = VGroup()
        angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
        numbers = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        
        for angle, num in zip(angles, numbers):
            number = Text(num, font_size=36, color=WHITE)
            if num in ["12", "6"]:  # 重点标记12和6
                number.set_color("#FFD700")
                number.scale(1.2)
            
            # 计算位置 - 以90度为起点
            adjusted_angle = (90 - angle) * DEGREES
            dist = face_radius - 0.8
            pos = dist * np.array([np.cos(adjusted_angle), np.sin(adjusted_angle), 0])
            number.move_to(pos)
            hour_numbers.add(number)
        
        # 创建指针
        hand = Line(
            start=ORIGIN,
            end=[0, face_radius - 1.0, 0],
            color="#FF5555",
            stroke_width=10
        )
        hand.add_tip(tip_length=0.3)
        
        # 创建数字显示器背景
        display_bg = RoundedRectangle(
            width=3, height=1.5,
            corner_radius=0.3,
            fill_color="#1E1E3F",
            fill_opacity=1,
            stroke_width=3,
            stroke_color="#D4AF37"
        )
        display_bg.next_to(face, DOWN, buff=0.8)
        
        # 初始数字显示区域
        display_area = Rectangle(width=4, height=3, fill_opacity=0, stroke_opacity=0)
        display_area.move_to(display_bg)
        
        # 添加所有元素到场景
        self.add(face, border, pivot, hour_numbers, display_bg, display_area)
        
        # 初始位置（指向12）
        current_display = Tex("12", font_size=72, color="#FF5555")
        current_display.move_to(display_bg)
        self.add(current_display)
        
        self.wait(0.5)
        
        # 修正后的数学表达式列表
        numbers = [
            r"12", 
            r"\tan(45^\circ)", 
            r"\log_{10}(100)",
            r"\int_{1}^{2} 2x \, dx", 
            r"\left(2\sin\left(\frac{\pi}{2}\right)\right)^{2}", 
            r"\sqrt[3]{125}", 
            r"3!", 
            r"0111_{2}", 
            r"\prod_{k=0}^{1}(2k+2)", 
            r"\sqrt{81}", 
            r"\log_{2}(1024)", 
            r"\text{B}_{16}"  # 使用\text{}保持字母正体
        ]
        
        # 动画：指针从12移动到11
        for i, num in enumerate(numbers[1:]):  # 从1开始到11
            # 创建当前指针旋转动画
            move_hand = Rotate(
                hand, 
                angle=-30 * DEGREES,  # 顺时针旋转30度
                about_point=ORIGIN,
                rate_func=smooth,
                run_time=1.0
            )
            
            # 创建新的数字显示
            new_display = MathTex(num, font_size=42, color="#FF5555")
            new_display.move_to(display_bg)
            
            # 移除旧数字并添加新数字
            self.play(
                move_hand,
                FadeOut(current_display),
                run_time=1.0
            )
            self.play(
                FadeIn(new_display),
                run_time=0.2
            )
            
            # 更新当前显示
            current_display = new_display
            self.wait(0.3)
        
        self.wait(1)
# manim -pqh 数学钟表.py MathClock -r 1920,1080