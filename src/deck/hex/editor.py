from hex.cell import Cell
import pygame
import random

class HexEditor:
    def __init__(self, deck):
        self.deck = deck
        self.pygame = deck.get_pygame()
        self.screen = deck.get_screen()
        self.offset_x = 0
        self.offset_y = 0
        self.ZOOM_MIN = 0.8
        self.ZOOM_MAX = 4
        self.zoom = 1
        self.scroll_speed = 10;

        self.cells = []
        self.populate_cells()

    def populate_cells(self):
        for x in range(50):
            for y in range(50):
                self.cells.append(Cell((0, random.randint(0, 255), 0), (x, y)))

    def update(self, event_state):
        if event_state.key_down(event_state.M_3):
            print("Right click")
        if event_state.key_pressed(pygame.K_RIGHT):
            self.offset_x -= self.scroll_speed
        if event_state.key_pressed(pygame.K_LEFT):
            self.offset_x += self.scroll_speed
        if event_state.key_pressed(pygame.K_UP):
            self.offset_y += self.scroll_speed
        if event_state.key_pressed(pygame.K_DOWN):
            self.offset_y -= self.scroll_speed
        

        space = event_state.key_pressed(pygame.K_SPACE)
        m1 = event_state.key_pressed(event_state.M_1)
        if space and m1:
            # Dragging while holding space
            self.offset_x += event_state.mouse_x_rel
            self.offset_y += event_state.mouse_y_rel

        if space:
            self.scroll_speed = 30
        else:
            self.scroll_speed = 10


        self.zoom += (event_state.mousewheel_x * 0.1)
        self.zoom = self.ZOOM_MIN if self.zoom < self.ZOOM_MIN else self.zoom
        self.zoom = self.ZOOM_MAX if self.zoom > self.ZOOM_MAX else self.zoom            
        print(f"zoom: {self.zoom}")
        # Draw cells
        for cell in self.cells:
            self.draw_cell(cell)

    def draw_cell(self, cell):
        size = self.hex_size()
        x = (cell.x * size) + self.offset_x
        y = (cell.y * size) + self.offset_y
        rect = pygame.Rect(x, y, size, size)
        color = pygame.Color(cell.r, cell.g, cell.b)
        self.pygame.draw.rect(self.screen, color, rect, 0)

    def hex_size(self):
        return 50 * self.zoom