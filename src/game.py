from src import pickups
from status import print_status
from gamestate import GameState
from controls import *


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        if command == "d" and state.player.can_move(1, 0, state.g):  # move right
            move_right(state)

        elif command == "w" and state.player.can_move(0, -1, state.g):
            move_up(state)

        elif command == "a" and state.player.can_move(-1, 0, state.g):
            move_left(state)

        elif command == "s" and state.player.can_move(0, 1, state.g):
            move_down(state)

    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
