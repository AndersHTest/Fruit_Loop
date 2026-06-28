from src import pickups
from src.status import print_status

#Lista med frukter, dessa är värda mer än övriga saker man kan hitta på banan.
fruits = ["apple", "cherry", "watermelon"]


#Flytta ett steg åt höger
def move_right(state):
    maybe_item = state.g.get(state.player.pos_x + 1, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x + 1, state.player.pos_y)
    maybe_end = state.g.get(state.player.pos_x + 1, state.player.pos_y)
    maybe_key = state.g.get(state.player.pos_x + 1, state.player.pos_y)
    maybe_chest = state.g.get(state.player.pos_x + 1, state.player.pos_y)
    maybe_shovel = state.g.get(state.player.pos_x + 1, state.player.pos_y)

    state.player.move(1, 0)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):     #Om du klev på en grönsak..
        # we found something
        if maybe_item.name in fruits:           #Kolla om det är en frukt. I så fall - dubbla poäng!
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:                                   #Är det en vanlig grönsak? Vanliga poäng
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):     # Du klev i en fälla - minuspoäng
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):       # Om alla grönsaker var upplockade när du klev på 'E' så avslutas spelet
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):  # Du klev på en nyckel - plocka upp den
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest): # Du klev på en kista - försök låsa upp den
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):     #Du klev på en spade - plocka upp den
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")

#Övriga riktningar:

#Flytta två steg åt höger
def jump_right(state):
    maybe_item = state.g.get(state.player.pos_x + 2, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x + 2, state.player.pos_y)
    maybe_end = state.g.get(state.player.pos_x + 2, state.player.pos_y)
    maybe_key = state.g.get(state.player.pos_x + 2, state.player.pos_y)
    maybe_chest = state.g.get(state.player.pos_x + 2, state.player.pos_y)
    maybe_shovel = state.g.get(state.player.pos_x + 2, state.player.pos_y)


    state.player.move(2, 0)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")


#Flytta ett steg åt vänster
def move_left(state):
    maybe_item = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    maybe_end = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    maybe_key = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    maybe_chest = state.g.get(state.player.pos_x - 1, state.player.pos_y)
    maybe_shovel = state.g.get(state.player.pos_x - 1, state.player.pos_y)

    state.player.move(-1, 0)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # We found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)
            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)
            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")


#Flytta två steg åt vänster
def jump_left(state):
    maybe_item = state.g.get(state.player.pos_x - 2, state.player.pos_y)
    maybe_trap = state.g.get(state.player.pos_x - 2, state.player.pos_y)
    maybe_end = state.g.get(state.player.pos_x - 2, state.player.pos_y)
    maybe_key = state.g.get(state.player.pos_x - 2, state.player.pos_y)
    maybe_chest = state.g.get(state.player.pos_x - 2, state.player.pos_y)
    maybe_shovel = state.g.get(state.player.pos_x - 2, state.player.pos_y)

    state.player.move(-2, 0)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")


#Flytta ett steg ner
def move_down(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    maybe_end = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    maybe_key = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    maybe_chest = state.g.get(state.player.pos_x, state.player.pos_y + 1)
    maybe_shovel = state.g.get(state.player.pos_x, state.player.pos_y + 1)

    state.player.move(0, 1)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # We found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)
            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)
            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")


#Flytta två steg ner
def jump_down(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y + 2)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y + 2)
    maybe_end = state.g.get(state.player.pos_x, state.player.pos_y + 2)
    maybe_key = state.g.get(state.player.pos_x, state.player.pos_y + 2)
    maybe_chest = state.g.get(state.player.pos_x, state.player.pos_y + 2)
    maybe_shovel = state.g.get(state.player.pos_x, state.player.pos_y + 2)

    state.player.move(0, 2)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")

#Flytta ett steg upp
def move_up(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    maybe_end = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    maybe_key = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    maybe_chest = state.g.get(state.player.pos_x, state.player.pos_y - 1)
    maybe_shovel = state.g.get(state.player.pos_x, state.player.pos_y - 1)

    state.player.move(0, -1)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # We found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)
            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)
            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")


#Flytta två steg upp
def jump_up(state):
    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y - 2)
    maybe_trap = state.g.get(state.player.pos_x, state.player.pos_y - 2)
    maybe_end = state.g.get(state.player.pos_x, state.player.pos_y - 2)
    maybe_key = state.g.get(state.player.pos_x, state.player.pos_y - 2)
    maybe_chest = state.g.get(state.player.pos_x, state.player.pos_y - 2)
    maybe_shovel = state.g.get(state.player.pos_x, state.player.pos_y - 2)

    state.player.move(0, -2)
    state.score -= 1
    state.steps -= 1

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if maybe_item.name in fruits:
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)

    elif isinstance (maybe_trap, pickups.Trap):
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance (maybe_end, pickups.End):
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance (maybe_key, pickups.Keys):
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance (maybe_chest, pickups.Chest):
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance (maybe_shovel, pickups.Shovel):
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")
