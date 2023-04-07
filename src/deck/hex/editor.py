from hex.cell import Cell
import pygame

class HexEditor:
    def __init__(self, deck):
        self.deck = deck
        self.pygame = deck.get_pygame()
        self.screen = deck.get_screen()
        self.offset_x = 0
        self.offset_y = 0
        self.zoom = 1

        self.cells = []
        self.populate_cells()

    def populate_cells(self):
        self.cells.append(Cell((0, 255, 0), (5, 5)))

    def update(self, event_state):
        self.screen.fill("blue")
        if event_state.key_down(event_state.M_1):
            print("Click")
        # Draw cells
        for cell in self.cells:
            self.draw_cell(cell)

    def draw_cell(self, cell):
        size = self.hex_size()
        rect = pygame.Rect(cell.x * size, cell.y * size, size, size)
        color = pygame.Color(cell.r, cell.g, cell.b)
        self.pygame.draw.rect(self.screen, color, rect, 0)

    def hex_size(self):
        return 50 * self.zoom