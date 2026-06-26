from src import pickups

fruits = ["apple", "cherry", "watermelon"]


def move_right(state):

    maybe_item = state.g.get(state.player.pos_x + 1, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x + 1, state.player.pos_y)

    state.player.move(1, 0)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def jump_right(state):
    maybe_item = state.g.get(state.player.pos_x + 2, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x + 2, state.player.pos_y)

    state.player.move(2, 0)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def move_left(state):

    maybe_item = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    state.player.move(-1, 0)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # We found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def jump_left(state):
    maybe_item = state.g.get(state.player.pos_x - 2, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x - 2, state.player.pos_y)

    state.player.move(-2, 0)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def move_down(state):

    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    state.player.move(0, 1)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # We found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def jump_down(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y + 2)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y + 2)

    state.player.move(0, 2)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def move_up(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    state.player.move(0, -1)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # We found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty


def jump_up(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y - 2)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y - 2)

    state.player.move(0, -2)
    state.score -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value * 2} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"You walked into a {maybe_trap.name}, {maybe_trap.penalty} points.")
        state.score += maybe_trap.penalty