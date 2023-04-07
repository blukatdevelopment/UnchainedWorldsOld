# Hold all the event info for a given frame
import pygame

KEYS = [
    pygame.K_RIGHT,
    pygame.K_LEFT,
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_SPACE,
    -1, # M_1
    -2, # M_2
    -3  # M_3
]

MOUSE_KEY_MAP = {
    1: -1,
    2: -2,
    3: -3
}

class EventState:
    def __init__(self, deck):
        self.deck = deck
        self.M_1 = -1 # Left mouse click
        self.M_2 = -2 # middle mouse click
        self.M_3 = -3 # Right mouse click
        self.DOWN = 0 # Just clicked
        self.HELD = 1 # preciously clicked, but not released
        self.UP = 2 # Just released
        self.UNHELD = 3 # previously up, but not clicked
        
        self.keys = {}
        self.keys_prev = {}

        for key in KEYS:
            self.keys[key] = self.UNHELD
            self.keys_prev[key] = self.UNHELD

        self.mouse_x = 0
        self.mouse_y = 0

    def get_key(self, keycode):
        if keycode in self.keys:
            return self.keys[keycode]

    def key_down(self, keycode):
        return keycode in self.keys and self.keys[keycode] == self.DOWN

    def key_held(self, keycode):
        return keycode in self.keys and self.keys[keycode] == self.HELD

    def key_up(self, keycode):
        return keycode in self.keys and self.keys[keycode] == self.UP

    def key_unheld(self, keycode):
        return keycode in self.keys and self.keys[keycode] == self.UNHELD

    # True if currently pressed, regardless of how long
    def key_state(self, keycode):
        return keycode in self.keys and self.keys[keycode] in [self.DOWN, self.HELD]

    # Shift current to previous
    # Assume all pressed keys are held, released keys are unheld
    def prepare_key_states(self):
        for key in KEYS:
            self.keys_prev[key] = self.keys[key]
            if self.keys_prev[key] == self.DOWN:
                self.keys[key] = self.HELD
            elif self.keys_prev[key] == self.UP:
                self.keys[key] = self.UNHELD

    def handle_events(self):
        self.prepare_key_states()
        (self.mouse_x, self.mouse_y) = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.deck.stop_running()
            elif event.type == pygame.KEYDOWN and event.key in KEYS:
                self.keys[event.key] = self.DOWN
            elif event.type == pygame.KEYUP and event.key in KEYS:
                self.keys[event.key] = self.UP
            elif event.type == pygame.MOUSEBUTTONUP:
                self.keys[MOUSE_KEY_MAP[event.button]] = self.UP
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.keys[MOUSE_KEY_MAP[event.button]] = self.DOWN