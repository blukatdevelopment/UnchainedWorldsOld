# Set up deck, load programs into it.

from deck import Deck
deck = Deck()

PROGRAMS = []

# setup title screen
from title.screen import TitleScreen
PROGRAMS.append(TitleScreen(deck))

# setup hex editor
from hex.editor import HexEditor
PROGRAMS.append(HexEditor(deck))


deck.set_programs(PROGRAMS)
deck.set_active_program(deck.TITLE_SCREEN)

while deck.is_running():
    deck.update()

deck.quit()