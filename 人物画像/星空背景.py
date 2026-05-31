from manim import *
import numpy as np

def add_starry_sky(
    scene,
    num_stars: int = 300,
    star_size_range: tuple = (0.02, 0.12),
    color_scheme: str = "natural",  # "natural", "cold", "warm", "rainbow"
    twinkle: bool = True,
    twinkle_speed_range: tuple = (1.0, 3.0),
    twinkle_intensity_range: tuple = (0.4, 1.0),
    random_seed: int = None,
):
    """
    为 Manim 场景添加星空背景
    
    参数:
        scene: Manim 场景对象
        num_stars: 星星数量 (默认: 300)
        star_size_range: 星星大小范围 (半径) (默认: (0.02, 0.12))
        color_scheme: 颜色方案 
            - "natural": 小星星偏白蓝，大星星偏暖黄
            - "cold": 冷色调 (白、蓝、淡紫)
            - "warm": 暖色调 (白、黄、橙)
            - "rainbow": 彩虹色 (随大小变化)
        twinkle: 是否启用闪烁效果 (默认: True)
        twinkle_speed_range: 闪烁速度范围 (默认: (1.0, 3.0))
        twinkle_intensity_range: 闪烁强度范围，即最小透明度 (默认: (0.4, 1.0))
        random_seed: 随机种子，用于复现效果 (默认: None)
    
    返回:
        stars: 创建的星星对象列表
    """
    
    # 设置随机种子
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # ======== 颜色方案定义 ========
    def get_color_by_size(size_ratio, scheme):
        """根据大小比例和颜色方案返回颜色"""
        if scheme == "natural":
            if size_ratio < 0.3:
                return WHITE
            elif size_ratio < 0.7:
                return BLUE_D
            else:
                return YELLOW
        elif scheme == "cold":
            if size_ratio < 0.33:
                return WHITE
            elif size_ratio < 0.66:
                return BLUE_D
            else:
                return PURPLE
        elif scheme == "warm":
            if size_ratio < 0.33:
                return WHITE
            elif size_ratio < 0.66:
                return YELLOW
            else:
                return ORANGE
        elif scheme == "rainbow":
            # 彩虹色: 红橙黄绿蓝靛紫
            colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
            idx = int(size_ratio * len(colors))
            idx = min(idx, len(colors) - 1)
            return colors[idx]
        else:
            return WHITE
    
    stars = []
    star_params = []
    
    for _ in range(num_stars):
        # 随机位置
        x = np.random.uniform(-config.frame_width/2, config.frame_width/2)
        y = np.random.uniform(-config.frame_height/2, config.frame_height/2)
        
        # 随机大小 (使用指数分布使小星星更多)
        size_ratio = np.random.exponential(scale=0.3)
        size_ratio = min(1.0, size_ratio)
        radius = star_size_range[0] + size_ratio * (star_size_range[1] - star_size_range[0])
        
        # 颜色
        color = get_color_by_size(size_ratio, color_scheme)
        
        # 闪烁参数
        twinkle_speed = np.random.uniform(twinkle_speed_range[0], twinkle_speed_range[1])
        twinkle_intensity = np.random.uniform(twinkle_intensity_range[0], twinkle_intensity_range[1])
        
        # 创建星星
        star = Circle(radius=radius, color=color, fill_opacity=1, stroke_width=0)
        star.move_to([x, y, 0])
        scene.add(star)
        stars.append(star)
        star_params.append({
            "speed": twinkle_speed,
            "min_opacity": twinkle_intensity,
            "phase": np.random.uniform(0, 2 * np.pi)
        })
    
    # 添加闪烁效果
    if twinkle:
        for star, params in zip(stars, star_params):
            def update_opacity(mob, dt, speed=params["speed"], min_op=params["min_opacity"], phase=params["phase"]):
                if not hasattr(mob, "star_time"):
                    mob.star_time = 0
                mob.star_time += dt
                t = mob.star_time * speed + phase
                opacity = (np.sin(t) + 1) / 2
                opacity = min_op + (1 - min_op) * opacity
                mob.set_fill(opacity=opacity)
            star.add_updater(update_opacity)
    
    return stars


# ============ 使用示例 ============
class StarrySkyExample(Scene):
    def construct(self):
        # 添加星空背景 - 自然风格，带闪烁
        add_starry_sky(
            self,
            num_stars=500,
            star_size_range=(0.01, 0.15),
            color_scheme="natural",
            twinkle=True,
            twinkle_speed_range=(0.8, 2.5),
            random_seed=42
        )
        
        # 添加一些前景元素
        title = Text("星空背景", font_size=48, color=WHITE)
        title.to_edge(UP)
        self.add(title)
        
        self.wait(10)


class ColdStarrySky(Scene):
    def construct(self):
        # 冷色调星空，不闪烁
        add_starry_sky(
            self,
            num_stars=400,
            color_scheme="cold",
            twinkle=False,
            random_seed=123
        )
        
        text = Text("冷色调星空", color=WHITE)
        self.add(text)
        self.wait(5)


class WarmRainbowExample(Scene):
    def construct(self):
        # 暖色调 + 彩虹混合
        add_starry_sky(
            self,
            num_stars=600,
            star_size_range=(0.02, 0.18),
            color_scheme="rainbow",
            twinkle=True,
            twinkle_speed_range=(1.5, 4.0),
            random_seed=999
        )
        
        title = Text("彩虹星空", color=WHITE, font_size=48)
        title.to_edge(UP)
        self.add(title)
        
        self.wait(10)