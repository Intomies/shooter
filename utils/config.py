from dataclasses import dataclass
from os.path import join as os_path_join
from pygame.font import Font


@dataclass(frozen=True)
class Apps:
    name: str = 'Shooter'
    fps: int = 60
    tilesize: int = 64


class Animations:
    entity_speed: float = 0.15
    

@dataclass(frozen=True)
class BorderWidth:
    small: int = 2


@dataclass(frozen=True)
class ButtonSizes:
    small: tuple[int, int] = (160, 40)


@dataclass(frozen=True)
class ButtonTypes:
    styled: int = 0
    text: int = 1


@dataclass(frozen=True)
class Colors:
    background: str = '#2B2D42'
    title: str = '#782323'
    shadow: str = '#161616'
    button_idle: str = '#606060'
    button_hover: str = '#808080'
    button_pressed: str = '#404040'
    button_text: str = '#000000'


@dataclass(frozen=True)
class EntityAction:
    idle: str = 'idle'
    attack: str = 'attack'
    walk: str = 'walk'


@dataclass(frozen=True)
class Fonts:
    __main_font_path: str = './utils/font/Silkscreen/Silkscreen-Regular.ttf'
    large_font_size: int = 144
    medium_font_size: int = 72
    small_font_size: int = 36

    @classmethod
    def large(self) -> Font:
        return Font(self.__main_font_path, self.large_font_size)

    @classmethod
    def medium(self) -> Font:
        return Font(self.__main_font_path, self.medium_font_size)
    
    @classmethod
    def small(self) -> Font:
        return Font(self.__main_font_path, self.small_font_size)


@dataclass(frozen=True)
class HitboxInflate:
    player: int = -26
    

@dataclass(frozen=True)
class Padding:
    smaller: int = 20
    small: int = 50
    medium: int = 100
    large: int = 150
    huge: int = 200


@dataclass(frozen=True)
class Paths:
    graphics_parent: str = './data/graphics'
    player: str = 'player'
    weapons: str = 'weapons'

    @classmethod
    def player_graphics(self) -> str:
        return os_path_join(self.graphics_parent, self.player)
    
    @classmethod
    def player_action(self, action: str) -> str:
        return os_path_join(self.graphics_parent, self.player, action)
    
    @classmethod
    def weapon(self, weapon_name: str) -> str:
        return os_path_join(self.graphics_parent, self.weapons, weapon_name)
    

@dataclass(frozen=True)
class PlayerActions:
    idle: str = 'idle'
    attack: str = 'attack'
    walk: str = 'walk'


@dataclass(frozen=True)
class PlayerActionDirections:
    up: tuple[int, str] = 'up'
    down: tuple[int, str] = 'down'
    left: tuple[int, str] = 'left'
    right: tuple[int, str] = 'right'
    default: tuple[int, str] = 'down'


@dataclass(frozen=True)
class PlayerAnimations:
    up_walk: str = 'up_walk'
    down_walk: str = 'down_walk'
    left_walk: str = 'left_walk'
    right_walk: str = 'right_walk'
    up_idle: str = 'up_idle'
    down_idle: str = 'down_idle'
    left_idle: str = 'left_idle'
    right_idle: str = 'right_idle'
    up_attack: str = 'up_attack'
    down_attack: str = 'down_attack'
    left_attack: str = 'left_attack'
    right_attack: str = 'right_attack'


@dataclass(frozen=True)
class PlayerBaseStats:
    health: int = 100
    attack_cooldown: int = 400
    attack_power: int = 10
    move_speed: int = 5
    action_speed: int = 6
    invulnerability_duration: int = 500


@dataclass(frozen=True)
class SpriteType:
    invisible: str = 'invisible'
    grass: str = 'grass' 
    objects: str = 'objects'
    enemy: str = 'enemy'
    weapon: str = 'weapon'