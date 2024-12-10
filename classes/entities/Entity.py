from typing import Optional
from pygame import Rect
from pygame.sprite import Group, Sprite
from pygame.math import Vector2
from pygame.time import get_ticks

from utils.config import Animations


class Entity(Sprite):
    def __init__(
            self, 
            groups: list[Group],
            obstacle_sprites: Group
            ):
        super().__init__(*groups)

        self.obstacle_sprites = obstacle_sprites

        self.frame_index: int = 0
        self.direction: Vector2 = Vector2()
        self.animation_speed = Animations.entity_speed
        
        self.rect: Optional[Rect] = None
        self.hitbox: Optional[Rect] = None
        
        self.collision_direction_vertical: str = 'vertical'
        self.collision_direction_horizontal: str = 'horizontal'

    
    def move(self, speed: float) -> None:
        if self.direction.magnitude() != 0:
            self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision(self.collision_direction_horizontal)

        self.hitbox.y += self.direction.y * speed
        self.collision(self.collision_direction_vertical)

        self.rect.center = self.hitbox.center


    def collision(self, direction: str) -> None:
        if direction == self.collision_direction_horizontal:
            for sprite in self.obstacle_sprites:
                
                if not sprite.hitbox.colliderect(self.hitbox): continue
                if self.direction.x > 0: self.hitbox.right = sprite.hitbox.left
                if self.direction.x < 0: self.hitbox.left = sprite.hitbox.right

        if direction == self.collision_direction_vertical:
            for sprite in self.obstacle_sprites:
                
                if not sprite.hitbox.colliderect: continue
                if self.direction.y > 0: self.hitbox.bottom = sprite.hitbox.top
                if self.direction.y < 0: self.hitbox.top = sprite.hitbox.bottom
        