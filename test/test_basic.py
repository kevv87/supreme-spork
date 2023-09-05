import unittest

class TestBasic(unittest.TestCase):
    
    def setUp(self) -> None:
        self.msg = create_msg("recuerdo")
    
    def test_should_create_message(self) -> None:
        self.assertTrue(self.msg)
    
    def test_message_should_have_specified_type(self) -> None:
        expect_type = "te amo"
        msg = create_msg(expect_type)
        self.assertEqual(msg.get_type(), expect_type)
    
    def test_when_type_is_outscoped_message_should_not_be_created(self) -> None:
        msg = create_msg("abcd")
        self.assertFalse(msg)

## Implementation

import enum 

class Type(enum.Enum):
    LOVE = "Te Amo"
    RECUERDO = "Recuerdo"
    LETRA = "Letra"
    


class Message:
    def __init__(self, type:str) -> None:
        self.type:str = type
    
    def get_type(self) -> str:
        return self.type


def create_msg(type:str) -> Message:
    return Message(type)
