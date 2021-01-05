import random
from utilities.find_queue import find_queue
from data_structures.monsters import monsters
from data_structures.active_channels import active_channels


async def init_combat(message, channel_id):
    queue = await find_queue(channel_id)
    await message.channel.send(f'The queue is: {queue}')

    rounds = len(queue)
    if 'rounds' not in active_channels[channel_id]:
        active_channels[channel_id]['rounds'] = {}
    active_channels[channel_id].update({'rounds': rounds})

    monster = random.choice(list(monsters))
    monster_hp = int(monsters[monster]['HP'])

    if 'monster' not in active_channels[channel_id]:
        active_channels[channel_id]['monster'] = {}

    if 'monster_name' not in active_channels[channel_id]['monster']:
        active_channels[channel_id]['monster']['monster_name'] = {}
    active_channels[channel_id]['monster'].update({'monster_name': monster})

    if 'HP' not in active_channels[channel_id]['monster']:
        active_channels[channel_id]['monster']['HP'] = {}
    active_channels[channel_id]['monster'].update({'HP': monster_hp})

    await message.channel.send(f'You hear a strange noise and in a matter of seconds you see a {monster} behind you!'
                               f' What are you going to do? [Type ^com_hlp for help on how to combat]')

