import pygame
from event import EventState

# Singleton for global stuff
class Deck:
    def __init__(self):
        # Init constants
        self.TITLE_SCREEN = 0
        self.HEX_EDITOR = 1
        self.RES_X = 1920
        self.RES_Y = 1080
        self.FRAMERATE = 30

        # Init locals
        self.pygame = pygame
        self.programs = []
        self.active_program = None
        self.event_state = EventState(self)

        # Init pygame
        self.screen = self.pygame.display.set_mode((self.RES_X, self.RES_Y))
        self.clock = self.pygame.time.Clock()
        self.running = True
        self.pygame.display.set_caption('World Editor')
        self.pygame.init()

# Public functions

    def update(self):
        self.event_state.handle_events()
        self.screen.fill("black")
        if self.active_program != None:
            self.active_program.update(self.event_state)
        self.pygame.display.flip()
        self.clock.tick(self.FRAMERATE)

    def quit(self):
        self.pygame.quit()

# Some access functions
    def set_programs(self, programs):
        self.programs = programs

    def set_active_program(self, program_id):
        self.active_program = self.programs[program_id]

    def is_running(self):
        return self.running

    def get_pygame(self):
        return self.pygame

    def get_screen(self):
        return self.screen

    def stop_running(self):
        self.running = False
        print("Running? {self.running}")


