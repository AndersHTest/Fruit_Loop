from src.grid import Grid
from src.player import Player
from src import pickups


class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.player = Player(18, 6)
        self.score = 0
        self.inventory = []
        self.key_inventory = []
        self.endgame = False
        self.steps = 0

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g)