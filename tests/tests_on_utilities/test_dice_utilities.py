import unittest
import asyncio
from utilities.dice_utilities import *


class TestDiceUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.player_class = 'Wizard'
        cls.attack_type = 'Spells'
        cls.action = 'Fireball'
        cls.monster_name = 'Giant Crab'

    def test_get_players_dice(self):
        dice_multiplier, dice_type = asyncio.run(get_players_dice(self.player_class, self.attack_type, self.action))
        self.assertEqual(int(dice_multiplier), 3)
        self.assertEqual(int(dice_type), 6)

    def test_get_monsters_dice(self):
        monster_dice_mult, monster_dice_type = asyncio.run(get_monsters_dice(self.monster_name))
        self.assertEqual(int(monster_dice_mult), 3)
        self.assertEqual(int(monster_dice_type), 4)


if __name__ == '__main__':
    unittest.main()
