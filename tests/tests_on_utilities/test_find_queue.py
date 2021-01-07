import asyncio
import unittest
from utilities.find_queue import find_queue


class TestDiceUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.channel_id = -2
        cls.control = [
            ('TestPlayer2', '5'),
            ('TestPlayer1', '3')
        ]

    def test_find_queue(self):
        case = asyncio.run(find_queue(self.channel_id))
        self.assertEqual(self.control, case)


if __name__ == '__main__':
    unittest.main()
