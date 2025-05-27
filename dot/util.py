from manim import *

def create_point_with_label(
    axes,
    coords,
    name,
    color=RED,
    name_size=None,      # 名称标签字体大小（优先级高于name_scale）
    coord_size=None,     # 坐标标签字体大小（优先级高于coord_scale）
    name_scale=1.0,      # 名称标签缩放比例
    coord_scale=1.0,     # 坐标标签缩放比例
    name_buff=0.2,       # 名称标签间距
    coord_buff=0.2       # 坐标标签间距
):
    point = Dot(axes.c2p(*coords), color=color)
    
    # 名称标签
    name_label = Tex(name, font_size=name_size) if name_size else Tex(name)
    name_label.scale(name_scale).next_to(point, UP, buff=name_buff)
    
    # 坐标标签
    coord_text = f"({coords[0]}, {coords[1]})"
    coord_label = MathTex(coord_text, font_size=coord_size) if coord_size else MathTex(coord_text)
    coord_label.scale(coord_scale).next_to(point, DOWN, buff=coord_buff)
    
    return VGroup(point, name_label, coord_label)