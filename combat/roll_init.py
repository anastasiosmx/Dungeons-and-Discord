from random import randint
from data_structures.active_channels import active_channels


async def roll_init(message, channel_id, client_name):
    roll = randint(1, 20)
    active_channels[channel_id][client_name]['Roll'] = {}
    active_channels[channel_id][client_name].update({'Roll': str(roll)})

    await message.channel.send(f'You rolled {roll}! If everyone rolled their dice type **[^start_combat]**')
