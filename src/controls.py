from src import pickups

#Lista med frukter, dessa är värda mer än övriga saker man kan hitta på banan.
fruits = ["apple", "cherry", "watermelon"]


#Flytta ett steg åt höger
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty


#Flytta två steg åt höger
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty


#Flytta ett steg åt vänster
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty


#Flytta två steg åt vänster
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty


#Flytta ett steg ner
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty


#Flytta två steg ner
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

#Flytta ett steg upp
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty


#Flytta två steg upp
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
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty