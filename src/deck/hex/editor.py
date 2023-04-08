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
        self.ZOOM_MIN = 0.5
        self.ZOOM_MAX = 4
        self.zoom = 1
        self.scroll_speed = 10;

        self.cells = []
        self.hovered_cell = None
        self.selected_cell = None
        self.menu_hover = False
        self.populate_cells()
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def populate_cells(self):
        for x in range(50):
            for y in range(50):
                self.cells.append(Cell((0, random.randint(0, 255), 0), (x, y)))

    def update(self, event_state):
        if event_state.key_down(event_state.M_1):
            if not self.menu_hover:
                if self.selected_cell == self.hovered_cell:
                    self.selected_cell = None
                else:
                    self.selected_cell = self.hovered_cell
        if event_state.key_down(event_state.M_3):
            if not self.menu_hover:
                self.selected_cell = None
        if event_state.key_pressed(pygame.K_RIGHT):
            self.offset_x -= self.scroll_speed
        if event_state.key_pressed(pygame.K_LEFT):
            self.offset_x += self.scroll_speed
        if event_state.key_pressed(pygame.K_UP):
            self.offset_y += self.scroll_speed
        if event_state.key_pressed(pygame.K_DOWN):
            self.offset_y -= self.scroll_speed
        

        space = event_state.key_pressed(pygame.K_SPACE)
        m1 = event_state.key_pressed(event_state.M_3)
        if m1 and not self.menu_hover:
            # Dragging while holding space
            self.offset_x += event_state.mouse_x_rel
            self.offset_y += event_state.mouse_y_rel

        if space:
            self.scroll_speed = 30
        else:
            self.scroll_speed = 10

        # Handle zoom
        self.zoom += (event_state.mousewheel_x * 0.1)
        self.zoom = self.ZOOM_MIN if self.zoom < self.ZOOM_MIN else self.zoom
        self.zoom = self.ZOOM_MAX if self.zoom > self.ZOOM_MAX else self.zoom            

        mx = event_state.mouse_x
        my = event_state.mouse_y
        rx = self.deck.RES_X
        ry = self.deck.RES_Y
        x_unit = rx / 10
        y_unit = ry / 10
        
        # Detect if mouse on a menu
        if (self.selected_cell != None and mx > rx - 2 * x_unit) or my > ry - y_unit:
            self.menu_hover = True
        else:
            self.menu_hover = False


        # Draw cells
        self.hovered_cell = None
        for cell in self.cells:
            self.draw_cell(cell, event_state)

        self.draw_footer()
        self.draw_side_panel()


    def draw_cell(self, cell, event_state):
        size = self.hex_size()
        x = (cell.x * size) + self.offset_x # Left
        y = (cell.y * size) + self.offset_y # top
        rect = pygame.Rect(x, y, size, size)
        color = pygame.Color(cell.r, cell.g, cell.b)
        mx = event_state.mouse_x
        my = event_state.mouse_y

        if self.menu_hover == False and mx > x and mx < x + size and my > y and my < y + size:
            color = pygame.Color(255, 0, 0)
            self.hovered_cell = cell
        if cell is self.selected_cell:
            color = pygame.Color(255, 0, 0)

        self.pygame.draw.rect(self.screen, color, rect, 0)


    def hex_size(self):
        return 50 * self.zoom

    def draw_side_panel(self):
        if self.selected_cell == None:
            return
        bg = (0, 0, 255)
        rx = self.deck.RES_X
        ry = self.deck.RES_Y
        ux = rx/10
        uy = ry/10
        panel_bg = (255, 0, 255)
        self.draw_rect((rx - 2*ux, 0, 2 * ux, ry), bg)


    def draw_footer(self):
        y_unit = self.deck.RES_Y/10
        bg = (0, 0, 255)
        self.draw_rect((0, self.deck.RES_Y - y_unit, self.deck.RES_X, y_unit), bg)
        text = "" if self.selected_cell == None else f"Selected cell: ({self.selected_cell.x},{self.selected_cell.y})"
        self.draw_text(text, (self.deck.RES_X/2, self.deck.RES_Y-y_unit), (255, 255, 255), bg)

    def draw_rect(self, rect, color):
        self.pygame.draw.rect(self.screen, color, rect, 0)

    def draw_text(self, text, pos, text_color, bg_color):
        text = self.font.render(text, True, text_color, bg_color)
        text_rect = text.get_rect()
        text_rect.left = pos[0]
        text_rect.top = pos[1]
        self.screen.blit(text, text_rect)