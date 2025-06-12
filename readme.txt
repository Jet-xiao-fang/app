# 配置全局 LaTeX 引擎和模板
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
# 生成视频
manim -pqh example5.py StaticCircle3 -r 1920,1080
# 覆盖上次生成的图片
manim -pqh --format=png 测试.py test -r 1920,1080 --output_file test
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
版本 Manim Community v0.19.0
更改了DNS解析为8.8.8.8后访问外部网络更加稳定了。但是要刷新CDN和重新启动电脑，不需要外网也ok
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080