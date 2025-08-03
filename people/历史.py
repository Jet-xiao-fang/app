from manim import *
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex
class MovieCreditRoll(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F1A"
        title=Text("淞沪会战部队番号",font="Source Han Sans CN")
        self.add(title)
    
# manim -pqh --format=png 历史.py MovieCreditRoll -r 1080,1920