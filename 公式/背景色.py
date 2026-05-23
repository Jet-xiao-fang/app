from manim import *
from Logo import LogoScene
from starfield import create_starfield

config.tex_compiler = "xelatex"
config.tex_template = TexTemplateLibrary.ctex


class ImportantPhysicsFormulas(LogoScene):
    def construct(self):
        self.camera.background_color = "#020212"
        self.add_logo()

        stars = create_starfield(n_stars=180)
        self.add(stars)
        self.wait(8)

# manim -pqh 背景色.py ImportantPhysicsFormulas
