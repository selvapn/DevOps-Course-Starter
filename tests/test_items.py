from todo_app.data.session_items import TRELLO_DOING, TRELLO_DONE, get_list, get_cards,TRELLO_TODO
from todo_app.data.view import ViewModel
import json
import unittest

def test_get_todo_card():
    view=ViewModel(TRELLO_TODO)
    items = view.get_todo_card()
    for itm in items:
        assert itm.get('idList') == TRELLO_TODO


def test_get_doing_card():
    view=ViewModel(TRELLO_DOING)
    items = view.get_doing_cards()
    for itm in items:
        assert itm.get('idList') == TRELLO_DOING


def test_get_doing_card():
    view=ViewModel(TRELLO_DONE)
    items = view.get_done_cards()
    for itm in items:
        assert itm.get('idList') == TRELLO_DONE
