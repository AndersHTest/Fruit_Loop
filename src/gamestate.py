from src.grid import Grid
from src.player import Player
from src import pickups


class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.player = Player(18, 6)  #Denna position talar om var spelaren börjar.
        self.score = 0  #Denna håller koll på antal poäng.
        self.inventory = []  #Denna lagerför alla grönsaker som har plockats upp.
        self.key_inventory = []  #Denna håller koll på hur många nycklar man har på sig.
        self.shovel_inventory = []
        self.endgame = False  #Denna ändras till True när man lyckas ta sig ut via 'E' och spelet avslutas.
        self.steps = 25  #Counter för att hålla koll på antal drag. När denna är på 0 produceras en ny grönsak.
        self.produced_vegetable_counter = 0  #Räknar totalt antal producerade grönsaker.

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g, self)