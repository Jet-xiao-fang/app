from manim import *
from Logo import LogoScene

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex

class ImportantPhysicsFormulas(LogoScene):
    def construct(self):
        self.camera.background_color = "#FFF8E7"
        # self.camera.background_color = "#FFF5E0"
        # self.camera.background_color = "#FDF5E6"
        # self.camera.background_color = "#FAF0E6"
        self.add_logo()
        self.wait(5)
        
# manim -pqh 背景色.py ImportantPhysicsFormulas