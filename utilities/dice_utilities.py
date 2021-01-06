import random
from data_structures.characters import characters
from data_structures.monsters import monsters


async def get_players_dice(player_class, attack_type, action):
    dice = characters[player_class.upper()][attack_type.upper()][action.upper()]
    dice_multiplier = dice[0]
    dice_type = dice[2]

    return dice_multiplier, dice_type


async def get_monsters_dice(monster_name):
    monster_dice = monsters[monster_name]['Attack']
    monster_dice_mult = monster_dice[0]
    monster_dice_type = monster_dice[2]

    return monster_dice_mult, monster_dice_type


async def roll_attack_dice(dice_multiplier, dice_type):
    attack_roll = 0
    for x in range(int(dice_multiplier)):
        attack_roll += random.randint(1, int(dice_type))

        return attack_roll
