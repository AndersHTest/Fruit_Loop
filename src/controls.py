from src import pickups
from src.status import print_status

#Lista med frukter, dessa är värda mer än övriga saker man kan hitta på banan.
fruits = ["apple", "cherry", "watermelon"]


def move_player(state, x, y):

    new_x = state.player.pos_x + x
    new_y = state.player.pos_y + y

    maybe_item = state.g.get(new_x, new_y)
    maybe_trap = state.g.get(new_x, new_y)
    maybe_end = state.g.get(new_x, new_y)
    maybe_key = state.g.get(new_x, new_y)
    maybe_chest = state.g.get(new_x, new_y)
    maybe_shovel = state.g.get(new_x, new_y)

    state.player.move(x, y)
    state.score -= 1
    state.grace_period -= 1
    if state.grace_period < 0:
        state.steps -= 1

    if isinstance(maybe_item, pickups.Item):  # Om du klev på en grönsak..
        # we found something
        if maybe_item.name in fruits:  # Kolla om det är en frukt. I så fall - dubbla poäng!
            state.score += maybe_item.value * 2
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value * 2} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.grace_period = 5

        else:  # Är det en vanlig grönsak? Vanliga poäng
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name)

            print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.\n")
            # g.set(player.pos_x, player.pos_y, g.empty)
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.grace_period = 5

    elif isinstance(maybe_trap, pickups.Trap):  # Du klev i en fälla - minuspoäng
        print(f"\nYou walked into a {maybe_trap.name}, {maybe_trap.penalty} points.\n")
        state.score += maybe_trap.penalty

    elif isinstance(maybe_end, pickups.End):  # Om alla grönsaker var upplockade när du klev på 'E' så avslutas spelet
        if state.produced_vegetable_counter == len(state.inventory):
            print_status(state.g, state)
            print(f"\nCongratulations, you completed the game!\n")
            state.endgame = True

    elif isinstance(maybe_key, pickups.Keys):  # Du klev på en nyckel - plocka upp den
        state.key_inventory.append(maybe_key.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a key, now go look for a chest.\n")

    elif isinstance(maybe_chest, pickups.Chest):  # Du klev på en kista - försök låsa upp den
        if len(state.key_inventory) > 0:
            state.g.clear(state.player.pos_x, state.player.pos_y)
            state.score += maybe_chest.value
            state.key_inventory.pop()
            print(f"\nYou unlocked a chest and found a treasure worth {maybe_chest.value} points!\n")
        elif len(state.key_inventory) < 1:
            print(f"\nYou found a chest, but it's locked... Try to find a key.\n")

    elif isinstance(maybe_shovel, pickups.Shovel):  # Du klev på en spade - plocka upp den
        state.shovel_inventory.append(maybe_shovel.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        print(f"\nYou found a shovel!\n")
