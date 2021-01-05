import random
from data_structures.active_channels import active_channels
from data_structures.monsters import monsters
from data_structures.characters import characters
from combat.hit_chance import hit_chance
from utilities.find_queue import find_queue


async def monster_attack(monster_name, player_hp, channel_id, client_name, message):
    monster_dice = monsters[monster_name]['Attack']
    monster_dice_mult = monster_dice[0]
    monster_dice_type = monster_dice[2]

    monster_attack_chance = await hit_chance()

    if monster_attack_chance:
        monster_roll = 0
        for x in range(int(monster_dice_mult)):
            monster_roll += random.randint(1, int(monster_dice_type))

        print(f'Player HP before dmg = {player_hp}')
        player_hp -= monster_roll
        print(f'Player HP after dmg = {player_hp}')

        if player_hp <= 0:
            await message.channel.send(f'{client_name} DIED ☠️')
            return
            # TODO Add to each player a died key so they can be blocked to do anything if they die

        await message.channel.send(f'The monster makes you loose {monster_roll} HP')

        if 'HP' not in active_channels[channel_id][client_name]:
            active_channels[channel_id][client_name]['HP'] = {}
        active_channels[channel_id][client_name].update({'HP': player_hp})

        queue = await find_queue(channel_id)
        rounds = len(queue)
        active_channels[channel_id].update({'rounds': rounds})
        print(active_channels)
        return

    queue = await find_queue(channel_id)
    rounds = len(queue)
    active_channels[channel_id].update({'rounds': rounds})
    await message.channel.send("The monster failed to hit you 😎")


async def attack(message, channel_id, client_name, attack_type, action):
    monster_name = active_channels[channel_id]['monster']['monster_name']
    monster_hp = int(active_channels[channel_id]['monster']['HP'])

    player_class = active_channels[channel_id][client_name]['Class']
    player_hp = active_channels[channel_id][client_name]['HP']

    total_rounds = active_channels[channel_id]['rounds']

    if total_rounds > 0:
        dice = characters[player_class.upper()][attack_type][action]
        dice_multiplier = dice[0]
        dice_type = dice[2]
        attack_chance = await hit_chance()

        if attack_chance:
            roll = 0
            for x in range(int(dice_multiplier)):
                roll += random.randint(1, int(dice_type))

            await message.channel.send(f'You rolled: {roll}')
            print(f'Monster HP before dmg = {monster_hp}')
            monster_hp -= roll
            print(f'Monster HP after dmg = {monster_hp}')

            if monster_hp <= 0:
                await message.channel.send(f'You destroyed this monster! Quick we must move on to the next challenge!')
                active_channels[channel_id].update({'combat_flag': 0})
                del active_channels[channel_id]['monster']
                del active_channels[channel_id]['rounds']
                print(active_channels)
                return

            if 'HP' not in active_channels[channel_id]['monster']:
                active_channels[channel_id]['monster']['HP'] = {}
            active_channels[channel_id]['monster'].update({'HP': monster_hp})
            print('CHANGED MONSTER HP')
            print(active_channels)

            await message.channel.send(f'You find your target! 😉')
            total_rounds -= 1
            active_channels[channel_id].update({'rounds': total_rounds})
            await monster_attack(monster_name, player_hp, channel_id, client_name, message)
            print(active_channels)
            return

        total_rounds -= 1
        active_channels[channel_id].update({'rounds': total_rounds})
        await message.channel.send("You did not find your target 😭")
        print(active_channels)
        return

    await message.channel.send('Its time for the monster to play!')
    await monster_attack(monster_name, player_hp, channel_id, client_name, message)
