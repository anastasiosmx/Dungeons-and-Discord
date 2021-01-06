import random
from utilities.reload_queue import reload_queue
from data_structures.monsters import monsters
from data_structures.active_channels import active_channels


async def init_combat(message, channel_id):
    queue = await reload_queue(channel_id)
    await message.channel.send(f'The queue is: {queue}')

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

