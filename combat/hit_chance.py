import random


async def hit_chance(rng):
    if rng is True:
        attacker = random.randint(1, 20)
        defender = random.randint(1, 20)
    else:
        attacker = 10
        defender = 5

    if attacker > defender:
        return True

    False
