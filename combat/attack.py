from data_structures.active_channels import active_channels
from combat.hit_chance import hit_chance
from combat.death_check import monster_is_dead
from combat.death_check import player_is_dead
from utilities.get_attack_info import get_attack_info
from utilities.dice_utilities import get_players_dice
from utilities.dice_utilities import get_monsters_dice
from utilities.dice_utilities import roll_attack_dice
from utilities.reload_queue import reload_queue


async def monster_attack(monster_name, player_hp, channel_id, client_name, message):
    monster_dice_mult, monster_dice_type = await get_monsters_dice(monster_name)
    monster_attack_chance = await hit_chance()

    if monster_attack_chance:
        monster_roll = await roll_attack_dice(monster_dice_mult, monster_dice_type)
        player_hp -= monster_roll

        await message.channel.send(f'The monster makes you loose {monster_roll} HP')
        if await player_is_dead(message, player_hp, client_name, channel_id):
            return

        if 'HP' not in active_channels[channel_id][client_name]:
            active_channels[channel_id][client_name]['HP'] = {}
        active_channels[channel_id][client_name].update({'HP': player_hp})

        await reload_queue(channel_id)
        return

    await reload_queue(channel_id)
    await message.channel.send("The monster failed to hit you 😎")

# TODO check if healing items or healing spell is used
async def attack(message, channel_id, client_name, attack_type, action):
    monster_name, monster_hp, player_class, player_hp, total_rounds = await get_attack_info(channel_id, client_name)

    if total_rounds > 0:
        dice_multiplier, dice_type = await get_players_dice(player_class, attack_type, action)
        attack_chance = await hit_chance()

        if attack_chance:
            roll = await roll_attack_dice(dice_multiplier, dice_type)
            monster_hp -= roll

            await message.channel.send(f'You rolled: {roll}')

            if await monster_is_dead(message, channel_id, monster_hp):
                return

            if 'HP' not in active_channels[channel_id]['monster']:
                active_channels[channel_id]['monster']['HP'] = {}
            active_channels[channel_id]['monster'].update({'HP': monster_hp})

            await message.channel.send(f'You find your target! 😉')
            total_rounds -= 1
            active_channels[channel_id].update({'rounds': total_rounds})
            await monster_attack(monster_name, player_hp, channel_id, client_name, message)
            return

        total_rounds -= 1
        active_channels[channel_id].update({'rounds': total_rounds})
        await message.channel.send("You did not find your target 😭")
        return

    await message.channel.send('Its time for the monster to play!')
    await monster_attack(monster_name, player_hp, channel_id, client_name, message)
