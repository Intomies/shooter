from dataclasses import dataclass


@dataclass
class WeaponData:
    name: str
    cooldown: int
    damage: int
    icon: str
    image_type: str
    x_offset: int
    y_offset: int