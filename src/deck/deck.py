import pygame, thorpy
from event import EventState
from thorpy.painting.painters.imageframe import ImageFrame
from thorpy.elements.element import Element

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
        self._menu = thorpy.BasicMenu(fps=self.FRAMERATE)

# Public functions

    def update(self):
        self.event_state.handle_events(self._menu)
        self.screen.fill("black")
        if self.active_program != None:
            self.active_program.update(self.event_state)
        self.pygame.display.flip()
        self.clock.tick(self.FRAMERATE)

    def quit(self):
        self.pygame.quit()

    def menu(self, element):
        self._menu.add_to_population(element)
        element.surface = self.screen
        return element

    def update_menu(self):
        self._menu.blit_and_update()

    def thorpy_image(self, path):
        e = Element(finish=False)
        painter = ImageFrame(path)
        e.set_painter(painter)
        e.finish()
        return e



# Some access functions
    def set_programs(self, programs):
        self.programs = programs

    def set_active_program(self, program_id):
        elements = self._menu._elements
        for element in elements:
            self._menu.remove_from_population(element)
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


