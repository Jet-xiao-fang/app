# 配置全局 LaTeX 引擎和模板
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
# 生成视频
manim -pqh example5.py StaticCircle3 -r 1920,1080
# 生成图片
manim -pqh --format=png circle_static.py StaticCircle -r 1920,1080

# 添加标题和说明
title = Text("斐波那契数列的几何演示", font_size=40, color=BLUE)
caption = Text("正方形边长 = 斐波那契数 | 螺旋线趋近黄金分割", font_size=24, color=GRAY)
caption.next_to(title, DOWN)
        
self.play(
    Write(title),
    FadeIn(caption, shift=UP)
)