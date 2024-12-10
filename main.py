from pygame import init as init_game

from classes.screens.MainMenu import MainMenu
from classes.state_machine.Engine import Engine


def main() -> None:
    init_game()
    engine = Engine()
    engine.run(MainMenu(engine))


if __name__ == '__main__':
    main()