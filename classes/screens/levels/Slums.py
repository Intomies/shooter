from typing import Optional
from pygame import MOUSEMOTION, Rect, Surface
from pygame.event import Event
from pygame.mouse import get_pos as get_mouse_pos
from pygame.sprite import Group

from classes.entities.Player import Player
from classes.entities.YSortCameraGroup import YSortCameraGroup
from classes.state_machine.State import State


class Slums(State):
    def __init__(self, engine):
        super().__init__(engine)

        self.display: Surface = self.engine.display
        self.display_rect: Rect = self.display.get_rect(topleft=(0,0))
        self.screen_width: int = self.display.get_width()
        self.screen_height: int = self.display.get_height()
        self.event: Optional[Event] = None

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = Group()

        self.player: Optional[Player] = None

        self.init_screen()


    def init_screen(self) -> None:
        self.create_screen()


    def handle_event(self, event: Event) -> None:
        self.event = event

    
    def create_screen(self) -> None: 
        self.player = Player(
            display=self.display,
            groups=[self.visible_sprites],
            obstacle_sprites=self.obstacle_sprites,
            position=self.display_rect.center
        )


    def update(self) -> None: pass
    
    
    def run(self) -> None:
        self.player.update(self.event)
        self.visible_sprites.custom_draw(self.player)