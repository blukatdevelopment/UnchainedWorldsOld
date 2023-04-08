from hex.cell import Cell
from hex.data import load_cells
import pygame, thorpy, random

TERRAIN = "Terrain"
HILLSIDE = "Hillside"
FOREST = "Forest"
DARKWOODS = "DarkWoods"
SWAMP = "Swamp"
DESERT = "Desert"
COASTAL_WATER = "Coastal Water"
OCEAN = "Ocean"
BAY = "Bay"
MOUNTAIN = "Mountain"
TERRAINS = [HILLSIDE, FOREST, DARKWOODS, SWAMP, DESERT, COASTAL_WATER, OCEAN, BAY, MOUNTAIN]
TERRAIN_COLORS = {
    HILLSIDE: (115, 222, 73),
    FOREST: (29, 84, 7),
    DARKWOODS: (15, 48, 2),
    SWAMP: (27, 54, 40),
    DESERT: (255, 234, 148),
    COASTAL_WATER: (59, 185, 255),
    OCEAN: (9, 79, 102),
    BAY: (144, 197, 214),
    MOUNTAIN: (255, 255, 255)
}

def terrain_function(self, terrain):
    return lambda: select_terrain(self, terrain)

def select_terrain(self, terrain):
    cell = self.get_selected()
    if cell == None:
        return
    
    cell.terrain = terrain
    color = TERRAIN_COLORS[terrain]
    (cell.r, cell.g, cell.b) = color
    self.show_side_panel()


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
        self.cells = load_cells()
        self.hovered_cell = None
        self._selected = None
        self.menu_hover = False
        self.panel_bg = None
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.init_needed = True
        self.cursor_color = pygame.Color(255, 0, 0)

    def init_thorpy(self):
        self.init_needed = False

    def show_side_panel(self, show=True):
        if not show or self.panel_bg != None:
            self.deck.remove_element(self.panel_bg)
            self.panel_bg = None
        
        if not show or self.get_selected() == None:
            return

        rx = self.deck.RES_X
        ry = self.deck.RES_Y
        ux = rx/10
        uy = ry/10
        cell = self.get_selected()
        color_buttons = self.make_color_buttons()
        name_label = thorpy.make_text("Active Hex: " + cell.name)
        name_label.set_font_size(32)
        name_label.set_font_color((255, 255, 255))
        name_label.set_topleft((0, 0))
        terrain_label = thorpy.make_text(cell.terrain)
        terrain_label.set_font_size(32)
        terrain_label.set_font_color(TERRAIN_COLORS[cell.terrain])
        terrain_label.set_topleft((0, 32))
        self.panel_bg = thorpy.Background(color=(0, 0, 255),elements = [name_label, terrain_label, color_buttons])
        self.panel_bg.set_topleft((rx-2*ux, 0))
        self.panel_bg.set_size((2*ux, ry))
        self.deck.menu(self.panel_bg)




    def make_color_buttons(self):
        rx = self.deck.RES_X
        ry = self.deck.RES_Y
        ux = rx/10
        uy = ry/10
        rt = "./hex/img/"
        ex = ".png"
        elements = []
        for i in range(len(TERRAINS)):
            t = TERRAINS[i]
            f = t.lower()
            f = f.replace(" ", "_")
            e = thorpy.make_image_button(rt+f+ex)
            c = TERRAIN_COLORS[t]
            e.terrain = t
            func = terrain_function(self, t)
            e.user_func = func
            elements.append(e)

        for i in range(len(elements)):
            el = elements[i]
            size = 40
            el.set_size((size, size))
            el.set_topleft((i * size, 0))
        
        color_bg = thorpy.Background(color=(0, 0, 0),                                    elements=elements)
        color_bg.set_size((2*ux, 40))
        color_bg.set_topleft((0, 70))
        return color_bg


    def set_selected(self, selected):
        self._selected = selected

    def get_selected(self):
        return self._selected

    def update(self, event_state):
        if self.init_needed:
            self.init_thorpy()
        if event_state.key_down(event_state.M_1):
            if not self.menu_hover:
                if self.get_selected() == self.hovered_cell or self.hovered_cell == None:
                    self.set_selected(None)
                    self.show_side_panel(False)
                else:
                    self.set_selected(self.hovered_cell)
                    self.show_side_panel()
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
        if (self.get_selected() != None and mx > rx - 2 * x_unit) or my > ry - y_unit:
            self.menu_hover = True
        else:
            self.menu_hover = False


        # Draw cells
        self.hovered_cell = None
        for cell in self.cells:
            self.draw_cell(cell, event_state)

        self.deck.update_menu()


    def draw_cell(self, cell, event_state):
        size = self.hex_size()
        x = (cell.x * size) + self.offset_x # Left
        y = (cell.y * size) + self.offset_y # top
        rect = pygame.Rect(x, y, size, size)
        color = pygame.Color(cell.r, cell.g, cell.b)
        mx = event_state.mouse_x
        my = event_state.mouse_y

        if self.menu_hover == False and mx > x and mx < x + size and my > y and my < y + size:
            color = self.cursor_color
            self.hovered_cell = cell
        if cell is self.get_selected():
            color = pygame.Color(255, 0, 0)

        self.pygame.draw.rect(self.screen, color, rect, 0)


    def hex_size(self):
        return 50 * self.zoom

    def draw_rect(self, rect, color):
        self.pygame.draw.rect(self.screen, color, rect, 0)

    def draw_text(self, text, pos, text_color, bg_color):
        text = self.font.render(text, True, text_color, bg_color)
        text_rect = text.get_rect()
        text_rect.left = pos[0]
        text_rect.top = pos[1]
        self.screen.blit(text, text_rect)