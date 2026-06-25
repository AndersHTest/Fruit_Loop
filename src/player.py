class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid, state):
        iswall_right = state.g.get(state.player.pos_x + 1, state.player.pos_y)
        iswall_up = state.g.get(state.player.pos_x, state.player.pos_y - 1)
        iswall_left = state.g.get(state.player.pos_x - 1, state.player.pos_y)
        iswall_down = state.g.get(state.player.pos_x, state.player.pos_y + 1)

        if iswall_right == grid.wall and x == 1:
            return False
        elif iswall_up == grid.wall and y == -1:
            return False
        elif iswall_left == grid.wall and x == -1:
            return False
        elif iswall_down == grid.wall and y == 1:
            return False
        else:
            return True


