from lib.group_chat_participants import *

def test_returns_empty():
    result = group_chat_names([])
    
    assert result == ""