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


def can_move(x, y, grid, state):
    #Check if there is a wall one step away in given direction. If yes, deny move.
    state_g = state.g.get
    state_x = state.player.pos_x
    state_y = state.player.pos_y

    is_wall_right = state_g(state_x + 1, state_y)
    is_wall_up = state_g(state_x, state_y - 1)
    is_wall_left = state_g(state_x - 1, state_y)
    is_wall_down = state_g(state_x, state_y + 1)

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


def can_jump(x, y, grid, state):
    #Check if there is a wall in one or two steps in the given direction. If yes, deny jump.
    state_g = state.g.get
    state_x = state.player.pos_x
    state_y = state.player.pos_y

    is_wall_right = state_g(state_x + 2, state_y)
    is_wall_up = state_g(state_x, state_y - 2)
    is_wall_left = state_g(state_x - 2, state_y)
    is_wall_down = state_g(state_x, state_y + 2)
    is_wall_right1 = state_g(state_x + 1, state_y)
    is_wall_up1 = state_g(state_x, state_y - 1)
    is_wall_left1 = state_g(state_x - 1, state_y)
    is_wall_down1 = state_g(state_x, state_y + 1)

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


def dig(grid, state):
    #Check if there is a wall one step away in any direction. If yes and if you have a shovel, dig.
    state_c = state.g.clear
    state_g = state.g.get
    state_x = state.player.pos_x
    state_y = state.player.pos_y

    is_wall_right = state_g(state_x + 1, state_y)
    is_wall_up = state_g(state_x, state_y - 1)
    is_wall_left = state_g(state_x - 1, state_y)
    is_wall_down = state_g(state_x, state_y + 1)

    if is_wall_right == grid.wall and len(state.shovel_inventory) > 0:
        state_c(state_x + 1, state_y)
        state.shovel_inventory.pop()
        print(f"Wall gone!")
    elif is_wall_up == grid.wall and len(state.shovel_inventory) > 0:
        state_c(state_x, state_y - 1)
        state.shovel_inventory.pop()
        print(f"Wall gone!")
    elif is_wall_left == grid.wall and len(state.shovel_inventory) > 0:
        state_c(state_x - 1, state_y)
        state.shovel_inventory.pop()
        print(f"Wall gone!")
    elif is_wall_down == grid.wall and len(state.shovel_inventory) > 0:
        state_c(state_x, state_y + 1)
        state.shovel_inventory.pop()
        print(f"Wall gone!")
