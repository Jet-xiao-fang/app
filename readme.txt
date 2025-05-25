# 配置全局 LaTeX 引擎和模板
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
# 生成视频
manim -pqh example5.py StaticCircle3 -r 1920,1080
# 生成图片
manim -pqh --format=png circle_static.py StaticCircle -r 1920,1080