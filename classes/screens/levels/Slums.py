from typing import Optional, Union
from pygame import Rect, Surface
from pygame.event import Event
from pygame.sprite import Group

from classes.entities.Weapon import Weapon
from classes.entities.Player import Player
from classes.entities.YSortCameraGroup import YSortCameraGroup
from classes.state_machine.State import State
from utils.classes.WeaponData import WeaponData
from utils.support import read_item_data_from_json


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
        self.attack_sprites = Group()

        self.player: Optional[Player] = None
        self.current_attack: Optional[Weapon] = None

        self.weapon_data: Optional[list[WeaponData]] = None


        self.init_screen()


    def init_screen(self) -> None:
        self.create_screen()


    def handle_event(self, event: Event) -> None:
        self.player.set_event(event)

    
    def create_screen(self) -> None:
        weapon_data_json = read_item_data_from_json('weapons')
        self.weapon_data = [WeaponData(**data_item) for data_item in weapon_data_json] 
        self.player = Player(
            display=self.display,
            groups=[self.visible_sprites],
            obstacle_sprites=self.obstacle_sprites,
            position=self.display_rect.center,
            weapon_data=self.weapon_data,
            create_attack=self.create_attack,
            destroy_attack=self.destroy_attack
        )

    def create_attack(self) -> None:
        if not self.current_attack:
            self.current_attack = Weapon(player=self.player, groups=[self.visible_sprites, self.attack_sprites])
            self.current_attack.update_position()

    
    def destroy_attack(self) -> None:
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None


    def update(self) -> None: pass
    
    
    def run(self) -> None:
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()