# Set up deck, load programs into it.

from deck import Deck
deck = Deck()

PROGRAMS = []

# setup hex editor
from hex.editor import HexEditor
PROGRAMS.append(HexEditor(deck))


deck.set_programs(PROGRAMS)
deck.set_active_program(deck.HEX_EDITOR)

while deck.is_running():
    deck.update()

deck.quit()