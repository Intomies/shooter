from pygame import (
    FULLSCREEN,
    Surface,
    QUIT,
    quit,
    K_ESCAPE
)
from pygame.cursors import arrow, diamond, broken_x, tri_left, tri_right
from pygame.display import flip, set_caption, set_mode
from pygame.event import Event, get as get_event
from pygame.key import get_pressed, ScancodeWrapper
from pygame.mouse import set_cursor
from pygame.time import Clock
from sys import exit

from classes.state_machine.Machine import Machine
from classes.state_machine.State import State
from utils.config import Apps, Colors


class Engine:
    def __init__(self) -> None:
        self.display: Surface = set_mode((0, 0), FULLSCREEN)
        self.clock = Clock()
        self.fps: int = Apps.fps
        self.machine = Machine()

        set_caption(Apps.name)
        set_cursor(broken_x)


    def loop(self) -> None:
        while True:
            self.machine.update()
            events: list[Event] = get_event()
            keys: ScancodeWrapper = get_pressed()

            for event in events:
                if event.type == QUIT or keys[K_ESCAPE]:
                    self.exit_game()
                else:
                    self.machine.current_state.handle_event(event)
            
            self.display.fill(Colors.background)
            self.machine.current_state.run()
            
            flip()
            self.clock.tick(self.fps)

    
    def run(self, state: State) -> None:
        self.machine.current_state = state
        self.loop()


    def exit_game(self) -> None:
        quit()
        exit()