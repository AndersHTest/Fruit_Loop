from src.status import print_inventory, print_status
from src.player import *
from src.controls import move_player, place_bomb
from src import pickups


def input_command(state):
    active = True
    st_g = state.g

    # Loopa tills användaren trycker Q eller X.
    while active:

        if state.endgame:   # Kollar om endgame-variabeln är True. I så fall, avsluta loopen.
            break

        if state.steps < 1:    # Efter 25 drag produceras en ny grönsak och läggs på banan
            pickups.randomize_vegetable(st_g, state)
            state.steps = 25

        print_status(st_g, state) # Antal poäng visas och spelplanen ritas på nytt

        command_key = input("C = controls, Q/X = quit:")
        command_key = command_key.casefold()[:2]

        if command_key == "d" and can_move(1, 0, st_g, state):  # move right
            move_player(state, 1, 0)

        elif command_key == "jd" and can_jump(2, 0, st_g, state): # jump right
            move_player(state, 2, 0)

        elif command_key == "w" and can_move(0, -1, st_g, state): # move up
            move_player(state, 0, -1)

        elif command_key == "jw" and can_jump(0, -2, st_g, state): # jump up
            move_player(state, 0, -2)

        elif command_key == "a" and can_move(-1, 0, st_g, state): # move left
            move_player(state, -1, 0)

        elif command_key == "ja" and can_jump(-2, 0, st_g, state): # jump left
            move_player(state, -2, 0)

        elif command_key == "s" and can_move(0, 1, st_g, state): # move down
            move_player(state, 0, 1)

        elif command_key == "js" and can_jump(0, 2, st_g, state): # jump down
            move_player(state, 0, 2)

        elif command_key == "i": # print inventory
            print_inventory(state)

        elif command_key == "b": # place bomb

            if len(state.bomb_inventory) > 0 and not isinstance(st_g.get(state.player.pos_x, state.player.pos_y), pickups.End):

                if state.bomb_placerad <= 0:
                    place_bomb(st_g, state)

                elif state.bomb_placerad > 0:
                    print("\nWait for the other bomb to explode before placing a new bomb.\n")

            elif len(state.bomb_inventory) == 0:
                print("\nYou have no bombs available.\n")

            elif isinstance(st_g.get(state.player.pos_x, state.player.pos_y), pickups.End):
                print("\nYou can't place the bomb on the only way out!\n")

        elif command_key == "c": # print controls
            print(f"\nUse WASD to move\nUse J+W/A/S/D to jump\nUse T to disarm trap\nUse I to show inventory\nUse G to dig\nUse B to place a bomb")
            print(f"\nSymbols:\nInactive bomb = 'b'\nActive bomb = 'B'\nChest = '±'\nKey = '¬'\nShovel = 'Î'\nTrap = #\nWall = '■'\nWay out = 'E'\nVegetable = '?'\nYou = '@'\n")

        elif command_key == "g": # Gräv genom en vägg till höger, vänster, upp eller ner.
            dig(st_g, state)

        elif command_key == "t":    # Desarmera fällor runt om dig med knappen "t"!
            if isinstance (st_g.get(state.player.pos_x + 1, state.player.pos_y), pickups.Trap):
                state.g.clear(state.player.pos_x + 1, state.player.pos_y)
                print(f"\nYou disarmed a trap to your right!\n")
            elif isinstance (st_g.get(state.player.pos_x - 1, state.player.pos_y), pickups.Trap):
                st_g.clear(state.player.pos_x - 1, state.player.pos_y)
                print(f"\nYou disarmed a trap to your left!\n")
            elif isinstance (st_g.get(state.player.pos_x, state.player.pos_y + 1), pickups.Trap):
                st_g.clear(state.player.pos_x, state.player.pos_y + 1)
                print(f"\nYou disarmed a trap beneath you!\n")
            elif isinstance (st_g.get(state.player.pos_x, state.player.pos_y - 1), pickups.Trap):
                st_g.clear(state.player.pos_x, state.player.pos_y - 1)
                print(f"\nYou disarmed a trap above you!\n")

        elif command_key == "q" or command_key == "x":  # Avsluta spelet
            active = False
