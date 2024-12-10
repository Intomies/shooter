from pygame import Surface, Rect
from pygame.draw import rect as draw_rect
from pygame.font import Font

from utils.config import Colors, BorderWidth

class TextDisplay:
    def __init__(
            self, 
            display: Surface,
            text: str, 
            font_style: Font, 
            position: tuple[int, int],
            color: str | tuple[int, int, int]
            ) -> None:
        self.display = display
        self.text = text
        self.font_style = font_style
        self.position = position
        self.color = color
        self.surface: Surface = self.font_style.render(str(self.text), True, self.color)
        self.rect: Rect = self.surface.get_rect(center=self.position)

    # Draws basic texts on display
    def draw_static_text(self) -> None:
        value: Surface = self.font_style.render(str(self.text), True, self.color)
        value_rect: Rect = value.get_rect(center=self.position)
        self.display.blit(value, value_rect)


    def draw(self, active: bool) -> None:
        color = Colors.active if active else Colors.passive
        draw_rect(
            self.surface, 
            Colors.active if active else Colors.passive, 
            self.rect, 
            BorderWidth.small
        )
        self.display.blit(self.surface, self.rect)