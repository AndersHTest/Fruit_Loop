from status import print_status
from controls import *
from status import print_inventory


def input_command(state):


    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("C = controls, Q/X = quit:")
        command = command.casefold()[:2]

        if command == "d" and state.player.can_move(1, 0, state.g, state):  # move right
            move_right(state)

        elif command == "jd" and state.player.can_jump(2, 0, state.g, state):
            jump_right(state)

        elif command == "w" and state.player.can_move(0, -1, state.g, state): # move up
            move_up(state)

        elif command == "jw" and state.player.can_jump(0, -2, state.g, state):
            jump_up(state)

        elif command == "a" and state.player.can_move(-1, 0, state.g, state): # move left
            move_left(state)

        elif command == "ja" and state.player.can_jump(-2, 0, state.g, state):
            jump_left(state)

        elif command == "s" and state.player.can_move(0, 1, state.g, state): # move down
            move_down(state)

        elif command == "js" and state.player.can_jump(0, 2, state.g, state):
            jump_down(state)

        elif command == "i":
            print_inventory(state)

        elif command == "c":
            print(f"\nUse WASD to move\nUse J+W/A/S/D to jump\nUse T to disarm trap\nUse I to show inventory")

        elif command == "t":    # Desarmera fällor runt om dig med knappen "t"!
            if isinstance (state.g.get(state.player.pos_x + 1, state.player.pos_y), pickups.Trap):
                state.g.clear(state.player.pos_x + 1, state.player.pos_y)
                print(f"You disarmed a trap to your right!")
            elif isinstance (state.g.get(state.player.pos_x - 1, state.player.pos_y), pickups.Trap):
                state.g.clear(state.player.pos_x -1, state.player.pos_y)
                print(f"You disarmed a trap to your left!")
            elif isinstance (state.g.get(state.player.pos_x, state.player.pos_y + 1), pickups.Trap):
                state.g.clear(state.player.pos_x, state.player.pos_y + 1)
                print(f"You disarmed a trap beneath you!")
            elif isinstance (state.g.get(state.player.pos_x, state.player.pos_y - 1), pickups.Trap):
                state.g.clear(state.player.pos_x, state.player.pos_y - 1)
                print(f"You disarmed a trap above you!")