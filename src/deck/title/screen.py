import pygame, thorpy

def nav_editor(self):
    self.init_needed = True
    self.deck.set_active_program(self.deck.HEX_EDITOR)

class TitleScreen:
    def __init__(self, deck):
        self.deck = deck
        self.pygame = deck.get_pygame()
        self.screen = deck.get_screen()
        self.font = pygame.font.Font('freesansbold.ttf', 100)
        self.image = pygame.image.load("../../img/blukat_info.png").convert()
        self.init_needed = True

    def init_thorpy(self):
        blukat = self.deck.thorpy_image("../../img/blukat_info.png")
        blukat.set_topleft((self.deck.RES_X/2 - 200, self.deck.RES_Y/3))
        howdy = thorpy.make_text("Howdy!")
        howdy.set_font_size(100)
        howdy.set_topleft((self.deck.RES_X/2 - 200, self.deck.RES_Y/3))
        load_button = thorpy.make_image_button(
                "./title/img/load.png", 
                "./title/img/load_hover.png", 
                "./title/img/load_hover.png",
                                    alpha=255,
                                    colorkey=(255,255,255))
        load_button.set_topleft((self.deck.RES_X/10, self.deck.RES_Y/3))
        load_button.user_func = lambda: nav_editor(self)
        create_button = thorpy.make_image_button(
                "./title/img/create.png", 
                "./title/img/create_hover.png", 
                "./title/img/create_hover.png",
                                    alpha=255,
                                    colorkey=(255,255,255))
        create_button.set_topleft((self.deck.RES_X-400, self.deck.RES_Y/3))
        self.background = thorpy.Background(color=(0, 0, 255),
                                    elements=[blukat,
                                    howdy,  load_button, create_button
                                    ])
        self.deck.menu(self.background)
        

    def update(self, event_state):
        if self.init_needed:
            self.init_thorpy()
            self.init_needed = False
        self.deck.update_menu()

    def draw_text(self, text, pos, text_color, bg_color, font = None):
        if font == None:
            font = self.font
        text = self.font.render(text, True, text_color, bg_color)
        text_rect = text.get_rect()
        text_rect.left = pos[0]
        text_rect.top = pos[1]
        self.screen.blit(text, text_rect)