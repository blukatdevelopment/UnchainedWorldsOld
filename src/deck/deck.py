import pygame

# Singleton for global stuff
class Deck:
    def __init__(self):
        # Init constants
        self.HEX_EDITOR = 0
        self.RES_X = 1920
        self.RES_Y = 1080

        # Init locals
        self.pygame = pygame
        self.programs = []
        self.active_program = None

        # Init pygame
        self.screen = self.pygame.display.set_mode((self.RES_X, self.RES_Y))
        self.clock = self.pygame.time.Clock()
        self.running = True
        self.pygame.display.set_caption('Interface')
        self.pygame.init()

# Public functions

    def update(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False
            else:
                self.active_program.handle_event(event)

        self.screen.fill("black")
        if self.active_program != None:
            self.active_program.update()
        self.pygame.display.flip()
        self.clock.tick(30)

    def quit():
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

