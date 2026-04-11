# 配置全局 LaTeX 引擎和模板
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
#这个背景色可以
config.background_color = "#1F2430"
# 生成视频
manim -pqh example5.py StaticCircle3 -r 1080,1920
# 覆盖上次生成的图片
manim -pqh --format=png 测试.py test -r 1080,1920 --output_file test
# 生成图片
manim -pqh --format=png circle_static.py StaticCircle -r 1080,1920

排版优化，确保所有元素（标题、坐标轴、余弦曲线、泰勒公式）清晰可见且互不遮挡。
