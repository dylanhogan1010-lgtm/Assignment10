class GameMap:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid  # 2D list where '#' is wall, '.' is path

    def is_valid_move(self, x, y):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return self.grid[y][x] != '#'
        return False

# Two distinctly shaped maps with walls and obstacles
TOWN_MAP = GameMap("Town", [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', 'N', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
])

FOREST_MAP = GameMap("Dark Forest", [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '.', '.', 'M', '#'],
    ['#', '#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
])

MAPS = {
    "Town": TOWN_MAP,
    "Dark Forest": FOREST_MAP
}