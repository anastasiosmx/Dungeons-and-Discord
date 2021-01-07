import unittest
import asyncio
from combat.hit_chance import hit_chance


class TestHitChance(unittest.TestCase):

    def test_hit_chance(self):
        res = asyncio.run(hit_chance(False))
        self.assertTrue(res, True)
    

if __name__ == '__main__':
    unittest.main()


