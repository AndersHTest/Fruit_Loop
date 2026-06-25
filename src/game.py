from status import print_status
from gamestate import GameState
from controls import *
from status import print_inventory


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        if command == "d" and state.player.can_move(1, 0, state.g, state):  # move right
            move_right(state)

        elif command == "w" and state.player.can_move(0, -1, state.g, state): # move up
            move_up(state)

        elif command == "a" and state.player.can_move(-1, 0, state.g, state): # move left
            move_left(state)

        elif command == "s" and state.player.can_move(0, 1, state.g, state): # move down
            move_down(state)

        elif command == "i":
            print_inventory(state)

        elif command == "t":    # Desarmera fällor runt om dig med knappen "t"!
            if isinstance (state.g.get(state.player.pos_x + 1, state.player.pos_y), pickups.Trap):
                state.g.clear(state.player.pos_x + 1, state.player.pos_y)
                print(f"You disarmed a trap to your right!")
            elif isinstance (state.g.get(state.player.pos_x - 1, state.player.pos_y), pickups.Trap):
                state.g.clear(state.player.pos_x -1, state.player.pos_y)
                print(f"You disarmed a trap to your left!")
            elif isinstance (state.g.get(state.player.pos_x, state.player.pos_y + 1), pickups.Trap):
                state.g.clear(state.player.pos_x, state.player.pos_y + 1)
                print(f"You disarmed a trap below you!")
            elif isinstance (state.g.get(state.player.pos_x, state.player.pos_y - 1), pickups.Trap):
                state.g.clear(state.player.pos_x, state.player.pos_y - 1)
                print(f"You disarmed a trap above you!")


    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
