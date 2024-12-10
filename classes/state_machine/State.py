from pygame.event import Event


class State:
    def __init__(self, engine):
        self.engine = engine

        
    def handle_event(self, event: Event) -> None: pass
    def run(self) -> None: pass 