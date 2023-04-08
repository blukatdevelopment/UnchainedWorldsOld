import pygame

class TitleScreen:
    def __init__(self, deck):
        self.deck = deck
        self.pygame = deck.get_pygame()
        self.screen = deck.get_screen()
        self.font = pygame.font.Font('freesansbold.ttf', 100)
        self.BLINK_DELAY = 15;
        self.blink_timer = self.BLINK_DELAY
        self.blink_on = True
        self.image = pygame.image.load("../../img/blukat_info.png").convert()

    def update(self, event_state):
        if event_state.key_pressed(pygame.K_SPACE):
            self.deck.set_active_program(self.deck.HEX_EDITOR)

        bg = (0, 0, 255)
        self.screen.fill(bg)
        self.blink_timer -= 1
        if self.blink_timer < 1:
            self.blink_on = not self.blink_on
            self.blink_timer = self.BLINK_DELAY

        self.screen.blit(self.image, (self.deck.RES_X/2 - 200, self.deck.RES_Y/3))
        text = "Howdy!"
        font = pygame.font.Font('freesansbold.ttf', 14)
        color = (0, 0, 0)
        pos = (self.deck.RES_X/2 - 200, self.deck.RES_Y/3)
        self.draw_text(text, pos, color, (0, 148, 255), font)

        text = "World Editor!"
        pos = (3 *(self.deck.RES_X/10), 0)
        color = (255, 238, 0) if self.blink_on else (255, 255, 255)
        self.draw_text(text, pos, color, bg)

        text = "[Press SPACE to begin]"
        pos = (self.deck.RES_X/4, self.deck.RES_Y - self.deck.RES_Y/5)
        color = (255, 238, 0) if self.blink_on else (255, 255, 255)
        self.draw_text(text, pos, color, bg)

    def draw_text(self, text, pos, text_color, bg_color, font = None):
        if font == None:
            font = self.font
        text = self.font.render(text, True, text_color, bg_color)
        text_rect = text.get_rect()
        text_rect.left = pos[0]
        text_rect.top = pos[1]
        self.screen.blit(text, text_rect)