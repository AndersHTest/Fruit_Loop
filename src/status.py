def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(f"{state.steps} steps until another vegetable spawn.")
    print(game_grid)


def print_inventory(state):
    """Visa inventory"""
    x = state.inventory
    print(f"\nInventory: {', '.join(x)}.")