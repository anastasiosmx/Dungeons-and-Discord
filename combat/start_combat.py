import random
from utilities.find_queue import find_queue
from data_structures.monsters import monsters
from data_structures.active_channels import active_channels


async def start_combat(message, channel_id):
    queue = await find_queue(channel_id)
    await message.channel.send(f'The queue is: {queue}')

    monster = random.choice(list(monsters))

    active_channels[channel_id]['Monster'] = {}
    active_channels[channel_id].update({'Monster': monster})

    await message.channel.send(f'You hear a strange noise and in a matter of seconds you see a {monster} behind you!')

