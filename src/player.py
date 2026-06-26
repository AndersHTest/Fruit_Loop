class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren - "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid, state):
        is_wall_right = state.g.get(state.player.pos_x + 1, state.player.pos_y)
        is_wall_up = state.g.get(state.player.pos_x, state.player.pos_y - 1)
        is_wall_left = state.g.get(state.player.pos_x - 1, state.player.pos_y)
        is_wall_down = state.g.get(state.player.pos_x, state.player.pos_y + 1)

        if is_wall_right == grid.wall and x == 1:
            return False
        elif is_wall_up == grid.wall and y == -1:
            return False
        elif is_wall_left == grid.wall and x == -1:
            return False
        elif is_wall_down == grid.wall and y == 1:
            return False
        else:
            return True


    def can_jump(self, x, y, grid, state):

        is_wall_right = state.g.get(state.player.pos_x + 2, state.player.pos_y)
        is_wall_up = state.g.get(state.player.pos_x, state.player.pos_y - 2)
        is_wall_left = state.g.get(state.player.pos_x - 2, state.player.pos_y)
        is_wall_down = state.g.get(state.player.pos_x, state.player.pos_y + 2)
        is_wall_right1 = state.g.get(state.player.pos_x + 1, state.player.pos_y)
        is_wall_up1 = state.g.get(state.player.pos_x, state.player.pos_y - 1)
        is_wall_left1 = state.g.get(state.player.pos_x - 1, state.player.pos_y)
        is_wall_down1 = state.g.get(state.player.pos_x, state.player.pos_y + 1)

        if (is_wall_right == grid.wall and x == 2) or (is_wall_right1 == grid.wall and x == 2):
            return False
        elif (is_wall_up == grid.wall and y == -2) or (is_wall_up1 == grid.wall and y == -2):
            return False
        elif (is_wall_left == grid.wall and x == -2) or (is_wall_left1 == grid.wall and x == -2):
            return False
        elif (is_wall_down == grid.wall and y == 2) or (is_wall_down1 == grid.wall and y == 2):
            return False
        else:
            return True

