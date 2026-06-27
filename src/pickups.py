
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]


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

def randomize(grid):
    #slumpar ut frukter, grönsaker och en köttbulle.
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
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
