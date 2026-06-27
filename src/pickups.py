import random

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("cabbage")]


class Trap:
    """Representerar fällor."""

    def __init__(self, name, penalty=-10, symbol="#"):
        self.name = name
        self.penalty = penalty
        self.symbol = symbol

    def __str__(self):
        return self.symbol

traps = [Trap("pitfall"), Trap("jaw trap")]


class End:
    """Representerar målet"""

    def __init__(self, name, symbol="E"):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

hurra = [End("E")]


class Chest:
    """Representerar en kista"""

    def __init__(self, name, value=100, symbol="±"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

kistor = [Chest("kista"), Chest("kista")]


class Keys:
    """Representerar en nyckel"""

    def __init__(self, name, symbol="¬"):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

nycklar = [Keys("nyckel 1"), Keys("nyckel 2")]


class Shovel:
    """Representerar en spade"""

    def __init__(self, name, symbol="Î"):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

spade = [Shovel("spade 1")]


def randomize(grid, state):
    #slumpar ut frukter, grönsaker och en köttbulle.
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                state.produced_vegetable_counter += 1
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

    #slumpar ut fällor
    for trap in traps:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, trap)
                break

    #slumpar ut en utväg(end)
    for end in hurra:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, end)
                break

    #slumpar ut kistor
    for kista in kistor:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, kista)
                break

    #slumpar ut nycklar
    for nyckel in nycklar:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, nyckel)
                break

    #slumpar ut en spade (förberett för att placera ut flera spadar)
    for i in spade:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, i)
                break

def randomize_vegetable(grid, state):
    random_vegetable = random.choice(pickups)

    x = grid.get_random_x()
    y = grid.get_random_y()
    if grid.is_empty(x, y):
        grid.set(x, y, random_vegetable)
        state.produced_vegetable_counter += 1