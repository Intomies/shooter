from dataclasses import fields
from typing import Optional
from pygame import Surface, K_w, K_a, K_s, K_d
from pygame.image import load as load_image
from pygame.key import get_pressed, ScancodeWrapper
from pygame.sprite import Group

from classes.entities.Entity import Entity
from utils.config import HitboxInflate, Paths, PlayerActionDirections, PlayerActions, PlayerAnimations
from utils.support import get_graphics_images_from_folder


class Player(Entity):
    def __init__(
            self, 
            display: Surface,
            groups: list[Group], 
            obstacle_sprites: Group,
            position: tuple[int, int]
            ):
        super().__init__(groups, obstacle_sprites)

        self.display = display
        self.display_width = self.display.get_width()
        self.display_height = self.display.get_height()
        self.image: Surface = load_image(f'{Paths.player_graphics()}/down_idle/idle_down.png')
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, HitboxInflate.player)

        self.assets: dict[str, Optional[list[Surface]]] = { action.name: get_graphics_images_from_folder(Paths.player_action(action.name)) for action in fields(PlayerAnimations) }

        self.facing: str = f'{PlayerActionDirections.down}'
        self.action: str = f'{PlayerActions.idle}'
        self.status: str = f'{self.facing}_{self.action}'
        self.attacking: bool = False



    def handle_input(self) -> None:
        keys: ScancodeWrapper = get_pressed()
        walk: str = PlayerActions.walk

        if self.attacking: return

        if keys[K_w]:
            self.direction.y = -1
            self.action = PlayerActions.walk
        elif keys[K_s]:
            self.direction.y = 1
            self.action = PlayerActions.walk
        else: 
            self.direction.y = 0
        if keys[K_a]:
            self.direction.x = -1
            self.action = PlayerActions.walk
        elif keys[K_d]:
            self.direction.x = 1
            self.action = PlayerActions.walk
        else: 
            self.direction.x = 0

        if self.direction == (0,0): self.action = PlayerActions.idle 

        self.status = f'{self.facing}_{self.action}'


    def handle_direction(self, mouse_x: int, mouse_y: int):
        # Determine quadrant and triangle
        if mouse_y > (self.display_height / self.display_width) * mouse_x:  # Below top-left to bottom-right
            if mouse_y > (-self.display_height / self.display_width) * mouse_x + self.display_height:  # Below top-right to bottom-left
                self.facing = PlayerActionDirections.down
            else:
                self.facing = PlayerActionDirections.left
        else:
            if mouse_y > (-self.display_height / self.display_width) * mouse_x + self.display_height:  # Below top-right to bottom-left
                self.facing = PlayerActionDirections.right
            else:
                self.facing = PlayerActionDirections.up

        self.status = f'{self.facing}_{self.action}'


    def animate(self) -> None:
        animation: list[Surface] = self.assets[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation): self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]

        self.image.set_alpha(255)



    def update(self) -> None:
        self.handle_input()
        self.animate()