from hex.cell import Cell
from pygame import Rect, Color

class HexEditor:
    def __init__(self, deck):
        self.deck = deck
        self.pygame = deck.get_pygame()
        self.screen = deck.get_screen()

        self.cells = []
        self.populate_cells()

    def populate_cells(self):
        self.cells.append(Cell((0, 255, 0), (0, 0)))

    def update(self):
        self.screen.fill("blue")

        # Draw cells
        for cell in self.cells:
            self.draw_cell(cell)

    def handle_event(self, event):
        pass

    def draw_cell(self, cell):
        size = self.hex_size()
        rect = Rect(cell.x, cell.y, size, size)
        color = Color(cell.r, cell.g, cell.b)
        self.pygame.draw.rect(self.screen, color, rect, 0)

    def hex_size(self):
        return 50