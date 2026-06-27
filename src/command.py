from src.status import print_status
from src.status import print_inventory
from src.player import *
from src.controls import *


def input_command(state):
    active = True
    st_g = state.g

    # Loopa tills användaren trycker Q eller X.
    while active:

        if state.endgame:
            break

        print_status(st_g, state)

        command_key = input("C = controls, Q/X = quit:")
        command_key = command_key.casefold()[:2]

        if command_key == "d" and can_move(1, 0, st_g, state):  # move right
            move_right(state)

        elif command_key == "jd" and can_jump(2, 0, st_g, state):
            jump_right(state)

        elif command_key == "w" and can_move(0, -1, st_g, state): # move up
            move_up(state)

        elif command_key == "jw" and can_jump(0, -2, st_g, state):
            jump_up(state)

        elif command_key == "a" and can_move(-1, 0, st_g, state): # move left
            move_left(state)

        elif command_key == "ja" and can_jump(-2, 0, st_g, state):
            jump_left(state)

        elif command_key == "s" and can_move(0, 1, st_g, state): # move down
            move_down(state)

        elif command_key == "js" and can_jump(0, 2, st_g, state):
            jump_down(state)

        elif command_key == "i":
            print_inventory(state)

        elif command_key == "c":
            print(f"\nUse WASD to move\nUse J+W/A/S/D to jump\nUse T to disarm trap\nUse I to show inventory")

        elif command_key == "t":    # Desarmera fällor runt om dig med knappen "t"!
            if isinstance (st_g.get(state.player.pos_x + 1, state.player.pos_y), pickups.Trap):
                state.g.clear(state.player.pos_x + 1, state.player.pos_y)
                print(f"You disarmed a trap to your right!")
            elif isinstance (st_g.get(state.player.pos_x - 1, state.player.pos_y), pickups.Trap):
                st_g.clear(state.player.pos_x - 1, state.player.pos_y)
                print(f"You disarmed a trap to your left!")
            elif isinstance (st_g.get(state.player.pos_x, state.player.pos_y + 1), pickups.Trap):
                st_g.clear(state.player.pos_x, state.player.pos_y + 1)
                print(f"You disarmed a trap beneath you!")
            elif isinstance (st_g.get(state.player.pos_x, state.player.pos_y - 1), pickups.Trap):
                st_g.clear(state.player.pos_x, state.player.pos_y - 1)
                print(f"You disarmed a trap above you!")

        elif command_key == "q" or command_key == "x":
            active = False
