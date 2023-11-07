import os
import sys
from typing import Optional

from aqt import dialogs, gui_hooks, mw
from aqt.addcards import AddCards
from aqt.browser.browser import Browser

sys.path.append(os.path.join(os.path.dirname(__file__), "vendor"))


def on_add_cards_did_init(addcards: AddCards) -> None:
    card = mw.reviewer and mw.reviewer.card
    if not card:
        browser: Optional[Browser] = dialogs._dialogs["Browser"][1]
        if browser and browser.selected_cards():
            card = mw.col.get_card(browser.selected_cards()[0])
        else:
            return
    new_deck_id = card.current_deck_id()
    if new_deck_id != addcards.deck_chooser.selected_deck_id:
        addcards.deck_chooser.selected_deck_id = new_deck_id


gui_hooks.add_cards_did_init.append(on_add_cards_did_init)
