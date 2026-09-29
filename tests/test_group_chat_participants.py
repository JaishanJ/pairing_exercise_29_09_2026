from lib.group_chat_participants import *

def test_returns_empty():
    result = group_chat_names([])
    
    assert result == ""

def test_returns_one_name():
    assert group_chat_names(["Bart"]) == "Bart"

def test_returns_two_names():
    assert group_chat_names(["Bart", "Lisa"]) == "Bart & Lisa"

def test_returns_multiple():
    assert group_chat_names(["Bart", "Lisa", "Maggie", "Bob"]) == "Bart, Lisa, Maggie & Bob"