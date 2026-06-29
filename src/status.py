from src import pickups

def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(f"{state.steps} steps until another vegetable spawn.")
    print(game_grid)


def print_inventory(state):
    """Visa inventory"""
    x = state.inventory
    if len(x) > 0:
        print(f"\nInventory: {', '.join(x)}.")
    else:
        print(f"\nYour inventory is empty.")


def end_game(state):

    save_pos_x = state.player.pos_x
    save_pos_y = state.player.pos_y

    state.player.pos_x = 0
    state.player.pos_y = 0

    dx = state.player.pos_x
    dy = state.player.pos_y

    for i in range(1,35):
        for j in range(1, 11):
            dx = i
            dy = j
            if isinstance(state.g.get(dx, dy), pickups.Item):
                state.vegetables_left.append(state.g.get(dx, dy))

    state.player.pos_x = save_pos_x
    state.player.pos_y = save_pos_y

    if len(state.vegetables_left) < 1:
        print_status(state.g, state)
        print(f"\nCongratulations, you completed the game with {state.score} points!\n")
        state.endgame = True
    elif len(state.vegetables_left) > 0:
        print(f"\nThere are still {len(state.vegetables_left)} vegetables left\n")
        state.vegetables_left.clear()
