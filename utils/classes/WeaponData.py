from dataclasses import dataclass


@dataclass
class WeaponData:
    name: str
    cooldown: int
    damage: int
    icon: str