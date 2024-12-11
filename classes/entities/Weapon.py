from typing import Optional
from pygame import Rect, Surface
from pygame.image import load as load_image
from pygame.math import Vector2
from pygame.sprite import Sprite, Group

from classes.entities.Player import Player
from utils.config import Apps, Paths, PlayerActionDirections, SpriteType


class Weapon(Sprite):
    def __init__(self, groups: list[Group], player: Player) -> None:
        super().__init__(groups)

        self.player = player
        self.sprite_type = SpriteType.weapon
        self.x_offset: int = player.selected_weapon.x_offset
        self.y_offset: int = player.selected_weapon.y_offset
        self.rect: Optional[Rect] = None
        self.update_position()

    def update_position(self) -> None:
        self.facing: str = self.player.facing
        self.image_path: str = f'{Paths.weapon(self.player.selected_weapon.name)}/{self.facing}.{self.player.selected_weapon.image_type}'
        self.image: Surface = load_image(self.image_path).convert_alpha()

        if self.facing == PlayerActionDirections.right:
            self.rect = self.image.get_rect(midleft=self.player.rect.midright + Vector2(-self.x_offset, self.y_offset))

        elif self.facing == PlayerActionDirections.left:
            self.rect = self.image.get_rect(midright=self.player.rect.midleft + Vector2(self.x_offset, self.y_offset))

        elif self.facing == PlayerActionDirections.down:
            self.rect = self.image.get_rect(midtop=self.player.rect.midbottom + Vector2(-self.x_offset, -self.y_offset))

        else:  # Up
            self.rect = self.image.get_rect(midbottom=self.player.rect.midtop + Vector2(self.x_offset, self.y_offset))