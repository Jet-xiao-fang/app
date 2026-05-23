from manim import *
import numpy as np


def create_starfield(
    n_stars=150,
    radius_range=(0.015, 0.03),
    colors=None,
    twinkle=True,
    alpha_range=(0.2, 1.0),
    twinkle_speed_range=(0.6, 2.5),
    width=None,
    height=None,
):
    if colors is None:
        colors = [
            ("#FFE8C0", 0.08),   # 暖黄星
            ("#B8D4FF", 0.12),   # 蓝白星
            ("#E8ECFF", 0.80),   # 冷白星
        ]
    frame_w = (width or config.frame_width) / 2
    frame_h = (height or config.frame_height) / 2
    min_r, max_r = radius_range
    min_a, max_a = alpha_range
    min_s, max_s = twinkle_speed_range

    color_choices = []
    cumulative = 0.0
    for hex_color, prob in colors:
        cumulative += prob
        color_choices.append((cumulative, hex_color))
    total_weight = cumulative

    stars_group = VGroup()
    for _ in range(n_stars):
        x = np.random.uniform(-frame_w, frame_w)
        y = np.random.uniform(-frame_h, frame_h)
        radius = np.random.uniform(min_r, max_r)
        rng = np.random.random() * total_weight
        base_color_candidates = [(cum, color) for cum, color in color_choices if rng < cum]
        base_color = base_color_candidates[0][1] if base_color_candidates else color_choices[-1][1]
        star = Dot([x, y, 0], radius=radius, color=base_color, z_index=-1)
        star.base_alpha = np.random.uniform(min_a, max_a)
        star.set_opacity(star.base_alpha)

        if twinkle:
            star.twinkle_speed = np.random.uniform(min_s, max_s)
            star.twinkle_phase = np.random.uniform(0, TAU)

            def updater(mob, dt):
                mob.twinkle_phase += dt * mob.twinkle_speed
                mob.set_opacity(mob.base_alpha * (0.45 + 0.55 * np.abs(np.cos(mob.twinkle_phase))))

            star.add_updater(updater)

        stars_group.add(star)

    return stars_group


def add_logo(
    scene,
    text="TheMathFlow",
    font="Microsoft YaHei",
    font_size=18,
    color=GREY_D,
    stroke_color=WHITE,
    stroke_width=0.5,
    corner=UL,
    buff=0.5,
    animate=False,
):
    logo_text = Text(text, font=font, font_size=font_size, color=color, weight=BOLD)
    logo_text.set_stroke(color=stroke_color, width=stroke_width)
    logo_text.to_corner(corner, buff=buff)

    if animate:
        scene.play(FadeIn(logo_text, shift=RIGHT * 0.2), run_time=0.8)
    else:
        scene.add(logo_text)

    return logo_text
