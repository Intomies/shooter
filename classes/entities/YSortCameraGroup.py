from pygame import Surface, Rect
from pygame.display import get_surface
from pygame.image import load as load_image
from pygame.math import Vector2
from pygame.sprite import Group

from classes.entities.Player import Player

# from classes.Enemy import Enemy

class YSortCameraGroup(Group):
    def __init__(self):
        super().__init__()
        
        self.display_surface: Surface = get_surface()
        self.half_width: int = self.display_surface.get_size()[0] // 2
        self.half_height: int = self.display_surface.get_size()[1] // 2
        self.offset: Vector2 = Vector2()
        # self.ground_file_path: str = Path.tilemap(MapGraphicsFile.ground)
        # self.floor_surface: Surface = load_image(self.ground_file_path).convert()
        # self.floor_rect: Rect = self.floor_surface.get_rect(topleft=(0, 0))
        
        
    # def custom_draw(self, player: Player):
    #     self.offset.x = player.rect.centerx - self.half_width
    #     self.offset.y = player.rect.centery - self.half_height
        
    #     floor_offset_position: tuple = self.floor_rect.topleft - self.offset
    #     self.display_surface.blit(self.floor_surface, floor_offset_position)
        
    #     for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
    #         offset_position: int = sprite.rect.topleft - self.offset
    #         self.display_surface.blit(sprite.image, offset_position)


    def custom_draw(self, player: Player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_offset_position: tuple = self.display_surface.get_rect(topleft=(0,0)).topleft - self.offset
        self.display_surface.blit(self.display_surface, floor_offset_position)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position: int = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)        