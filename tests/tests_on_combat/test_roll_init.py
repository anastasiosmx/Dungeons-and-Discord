import unittest
import asyncio
from combat.roll_init import roll_init
from data_structures.active_channels import active_channels


class TestHitChance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.message = False
        cls.rng = False
        cls.channel_id = -1
        cls.client_name = 'TestPlayer1'
        cls.control = "10"

    def test_roll_init(self):
        res = asyncio.run(roll_init(self.message, self.channel_id, self.client_name, self.rng))
        self.assertIn(self.control, active_channels[self.channel_id][self.client_name]['Roll'])


if __name__ == '__main__':
    unittest.main()
