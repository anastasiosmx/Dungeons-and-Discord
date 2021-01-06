import unittest
import asyncio
from combat.death_check import *


class TestDeathCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.monster_hp_neg = -1
        cls.monster_hp_pos = 1
        cls.channel_id_with_death_flag = -1
        cls.channel_id_without_death_flag = -2
        cls.message = False

        cls.player_hp_neg = -1
        cls.player_hp_pos = 1
        cls.client_name = 'Test'

    def test_monster_is_dead_true(self):
        res = asyncio.run(monster_is_dead(self.message, self.channel_id_with_death_flag, self.monster_hp_neg))
        self.assertTrue(res)
        self.assertNotIn('monster', active_channels[self.channel_id_with_death_flag])
        self.assertNotIn('rounds', active_channels[self.channel_id_with_death_flag])
        self.assertEqual(active_channels[self.channel_id_with_death_flag]['combat_flag'], 0)

    def test_monster_is_dead_false(self):
        res = asyncio.run(monster_is_dead(self.message, self.channel_id_with_death_flag, self.monster_hp_pos))
        self.assertFalse(res)
        self.assertIn('monster', active_channels[self.channel_id_with_death_flag])
        self.assertIn('rounds', active_channels[self.channel_id_with_death_flag])
        self.assertEqual(active_channels[self.channel_id_with_death_flag]['combat_flag'], 1)

    def test_player_is_dead_true(self):
        res = asyncio.run(player_is_dead(self.message, self.player_hp_neg, self.client_name, self.channel_id_with_death_flag))
        self.assertTrue(res)
        self.assertEqual(active_channels[self.channel_id_with_death_flag][self.client_name]['death_flag'], 1)

    def test_player_is_dead_false(self):
        res = asyncio.run(player_is_dead(self.message, self.player_hp_pos, self.client_name, self.channel_id_with_death_flag))
        self.assertFalse(res)
        self.assertEqual(active_channels[self.channel_id_with_death_flag][self.client_name]['death_flag'], 0)

    def test_player_has_no_death_flag(self):
        res = asyncio.run(player_is_dead(self.message, self.player_hp_neg, self.client_name, self.channel_id_without_death_flag))
        self.assertTrue(res)
        self.assertTrue(active_channels[self.channel_id_without_death_flag][self.client_name]['death_flag'])


if __name__ == '__main__':
    unittest.main()