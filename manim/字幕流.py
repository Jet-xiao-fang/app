from manim import *
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class MathLearningRoll(Scene):
    def construct(self):
        # ===== 1. 提前创建字幕内容 =====
        lines = [
            "数学学习路径：从基础到高级",
            '<span color="YELLOW">算术基础：</span>自然数、整数、分数、小数',
            '<span color="YELLOW">代数入门：</span>变量与表达式、一元一次方程、不等式',
            '<span color="YELLOW">几何基础：</span>点线面、三角形与四边形、圆的基本性质',
            '<span color="YELLOW">函数入门：</span>',
            "一次函数、二次函数、反比例函数、函数图像与性质",
            '<span color="YELLOW">概率统计：</span>数据收集与分析、概率计算、统计图表',
            '<span color="YELLOW">三角函数：</span>',
            "正弦、余弦、正切、诱导公式、解三角形",
            '<span color="YELLOW">解析几何：</span>坐标系、直线方程、圆锥曲线（圆/椭圆/双曲线）',
            '<span color="YELLOW">高等代数：</span>矩阵与行列式、向量空间、线性变换',
            '<span color="YELLOW">微积分：</span>',
            "极限与连续、导数与微分、积分与应用",
            "多元微积分、微分方程",
            '<span color="YELLOW">离散数学：</span>',
            "集合论、图论、数理逻辑、组合数学",
            '<span color="YELLOW">抽象代数：</span>群论、环论、域论、伽罗瓦理论',
            '<span color="YELLOW">拓扑学：</span>拓扑空间、连通性、紧致性、同伦论',
            '<span color="YELLOW">实变函数：</span>勒贝格测度、可测函数、积分理论',
            '<span color="YELLOW">泛函分析：</span>',
            "巴拿赫空间、希尔伯特空间、线性算子、谱理论",
            '<span color="YELLOW">微分几何：</span>曲线曲面论、黎曼几何、纤维丛',
            '<span color="YELLOW">代数几何：</span>代数簇、概形、上同调理论',
            '<span color="YELLOW">数论前沿：</span>',
            "模形式、椭圆曲线、朗兰兹纲领",
            "—— 数学的星辰大海 ——",
        ]
        font_size = 30
        line_spacing = 0.6

        # 创建字幕组
        credits = VGroup()
        
        for i, text in enumerate(lines):
            if i == 0:
                line = MarkupText(
                    text, 
                    font="Source Han Sans CN", 
                    font_size=48, 
                    color=RED,
                    stroke_width=1.5,
                    stroke_color=BLACK
                )
            else:
                line = MarkupText(
                    text, 
                    font="Source Han Sans CN", 
                    font_size=font_size,
                    stroke_width=1.0,
                    stroke_color=BLACK
                )
            
            credits.add(line)
            
        credits.arrange(DOWN, buff=line_spacing, aligned_edge=ORIGIN)
        
        # 添加背景矩形
        background_rect = Rectangle(
            width=config.frame_width * 0.9,
            height=credits.height * 1.1,
            fill_color=BLACK,
            fill_opacity=0.7,
            stroke_width=0
        )
        background_rect.move_to(credits)
        
        # 将背景和文本组合
        credits_group = VGroup(background_rect, credits)
        
        # 将字幕组放置在屏幕底部之外
        credits_group.move_to(DOWN * (config.frame_height / 2 + credits_group.height / 2))
        
        # ===== 2. 显示标题并无缝连接字幕滚动 =====
        tex = Tex(r"数学学习之路", color=YELLOW).scale(1.5)
        
        # 同时播放标题消失和字幕出现动画
        self.play(Write(tex), run_time=1.5)
        self.wait(0.5)
        
        # 计算滚动距离（使字幕完全移出屏幕）
        target_y = credits_group.get_height() + config.frame_height
        
        # 创建动画组实现无缝过渡
        self.play(
            AnimationGroup(
                FadeOut(tex, shift=UP * 0.5, run_time=1.0),
                credits_group.animate.shift(UP * (target_y + 1)),
                lag_ratio=0.3  # 标题淡出后稍微延迟再开始字幕滚动
            ),
            run_time=16,
            rate_func=linear
        )
        
        # 添加淡出效果
        self.play(FadeOut(credits_group, shift=UP*0.5), run_time=1.5)
        self.wait(0.5)
        
# manim -pqh 字幕流.py MathLearningRoll