import os
import sys

from aqt import gui_hooks, mw
from aqt.addcards import AddCards

sys.path.append(os.path.join(os.path.dirname(__file__), "vendor"))


def on_add_cards_did_init(addcards: AddCards) -> None:
    card = mw.reviewer and mw.reviewer.card
    if not card:
        return
    new_deck_id = card.current_deck_id()
    if new_deck_id != addcards.deck_chooser.selected_deck_id:
        addcards.deck_chooser.selected_deck_id = new_deck_id


gui_hooks.add_cards_did_init.append(on_add_cards_did_init)
