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
        self.bomb_inventory = []
        self.endgame = False  #Denna ändras till True när man lyckas ta sig ut via 'E' och spelet avslutas.
        self.steps = 25  #Counter för att hålla koll på antal drag. När denna är på 0 produceras en ny grönsak.
        self.grace_period = 0   #Uppdateras om man kliver på en grönsak - steg räknas ej om variabeln är mellan 0 - 5.
        self.bomb_placerad = 0  #Uppdateras till 3 om en bomb blivit placerad.
        self.bomb_placerad_x = 0 #X-position uppdateras när bomb placeras
        self.bomb_placerad_y = 0 #Y-position uppdateras när bomb placeras
        self.vegetables_left = []

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g, self)