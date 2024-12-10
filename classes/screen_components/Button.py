from typing import Optional
from pygame import Rect, Surface
from pygame.draw import rect as draw_rect
from pygame.font import Font

from utils.config import BorderWidth, ButtonSizes, ButtonTypes, Colors, Fonts


class Button:
    def __init__(
            self,
            display: Surface,
            type: int,
            text: str,
            position: tuple[int, int],
            size: tuple[int, int],
            ):
        self.display = display
        self.type = type
        self.text = text
        self.position = position
        self.size = size
        
        self.hover: bool = False
        self.pressed: bool = False

        self.color: str = Colors.button_idle
        self.font: Font = self.__set_font()
        self.font_color: str = Colors.button_text

        self.surface = Surface(self.size)
        self.rect: Rect = self.surface.get_rect(center=self.position)

        self.shadow_surface= Surface(self.size)
        self.shadow_rect: Rect= self.shadow_surface.get_rect(topleft=(self.rect.left-3, self.rect.top-3))
        
        self.text_surface = self.font.render(str(self.text), True, self.font_color)
        self.text_rect: Rect = self.text_surface.get_rect(center=self.rect.center)


    def draw(self) -> None:
        if self.type == ButtonTypes.styled:
            self.__draw_styled()


    def __draw_styled(self) -> None:
        self.color = self.__set_color()

        shadow_true = self.display.blit(self.shadow_surface, self.shadow_rect)
        draw_rect(self.display, Colors.shadow, shadow_true, border_radius=10)
        
        self.display.blit(self.surface, self.rect)
        draw_rect(self.display, self.color, self.rect, border_radius=5)
        
        self.display.blit(self.text_surface, self.text_rect)



    def __set_color(self) -> str:
        if not self.hover and not self.pressed: return Colors.button_idle
        if self.pressed: return Colors.button_pressed

        return Colors.button_hover
    

    def set_hover(self, value: bool) -> None:
        self.hover = value


    def set_pressed(self, value: bool) -> None:
        self.pressed = value
 

    def __set_font(self) -> Font:
        match self.size:
            case ButtonSizes.small: return Fonts.small()
            case _: return Fonts.medium()