from random import randint
from data_structures.active_channels import active_channels


async def roll_init(message, channel_id, client_name, rng):
    roll = randint(1, 20)
    if 'Roll' not in active_channels[channel_id][client_name]:
        active_channels[channel_id][client_name]['Roll'] = {}

    if rng is True:
        active_channels[channel_id][client_name].update({'Roll': str(roll)})

    if rng is False:
        active_channels[channel_id][client_name].update({'Roll': '10'})

    if message:
        await message.channel.send(f'You rolled {roll}! If everyone rolled their dice type **[^init_combat]**')
