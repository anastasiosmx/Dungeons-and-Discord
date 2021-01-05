import random


async def hit_chance():
    attacker = random.randint(1, 20)
    defender = random.randint(1, 20)

    if attacker > defender:
        return True

    False
