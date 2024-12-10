from typing import Callable, Optional
from pygame import Rect, Surface, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP

from classes.screen_components.Button import Button
from classes.screen_components.TextDisplay import TextDisplay
from classes.screens.levels.Slums import Slums
from classes.state_machine.State import State
from utils.config import Apps, ButtonSizes, ButtonTypes, Colors, Fonts, Padding


class MainMenu(State):
    def __init__(self, engine):
        super().__init__(engine)

        self.display: Surface = self.engine.display
        self.display_rect: Rect = self.display.get_rect(topleft=(0,0))
        self.screen_width: int = self.display.get_width()
        self.screen_height: int = self.display.get_height()
        
        self.headline: Optional[TextDisplay] = None
        self.buttons: dict[Button, Callable] | None = None

        self.init_screen()


    def init_screen(self) -> None:
        self.create_screen()


    def handle_event(self, event) -> None:
        if event.type == MOUSEMOTION:
            for button, action in self.buttons.items():
                button.set_hover(button.rect.collidepoint(event.pos))

        if event.type == MOUSEBUTTONDOWN:
            for button, action in self.buttons.items():
                if button.rect.collidepoint(event.pos):
                    button.set_pressed(True)
                    action()
                    break
        
        if event.type == MOUSEBUTTONUP:
            for button, action in self.buttons.items():
                button.set_pressed(False)


    def create_screen(self) -> None:
        self.headline = TextDisplay(self.display, Apps.name, Fonts.large(), self.display_rect.center, Colors.title)
        menu_buttons_y = self.headline.rect.bottom + Padding.medium
        
        quit_button_x = self.headline.rect.centerx - Padding.medium
        quit_button = Button(self.display, ButtonTypes.styled, 'Quit', (quit_button_x, menu_buttons_y), ButtonSizes.small)
        
        play_button_x = self.headline.rect.centerx + Padding.medium
        play_button = Button(self.display, ButtonTypes.styled, 'Start', (play_button_x, menu_buttons_y), ButtonSizes.small)
        
        self.buttons = {
            quit_button: lambda: self.engine.exit_game(),
            play_button: lambda: setattr(self.engine.machine, 'next_state', Slums(self.engine))
        }


    def update(self) -> None:
        pass


    def draw(self) -> None:
        self.headline.draw_static_text()
        for button in self.buttons: button.draw()


    def run(self) -> None:
        self.update()
        self.draw()