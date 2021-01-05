from data_structures.active_channels import active_channels
from data_structures.characters import characters


async def choose_character(message, channel_id, client_name):
    channel_name = message.channel.name
    char_selected = message.content.split()
    client_hp = characters[char_selected[1].upper()]['HP']

    if channel_id not in active_channels:
        active_channels[channel_id] = {}
    active_channels[channel_id].update({'Title': channel_name})

    if client_name not in active_channels[channel_id]:
        active_channels[channel_id][client_name] = {}
    active_channels[channel_id][client_name].update({'Class': char_selected[1]})

    if 'HP' not in active_channels[channel_id][client_name]:
        active_channels[channel_id][client_name]['HP'] = {}
    active_channels[channel_id][client_name].update({'HP': client_hp})

    await message.channel.send(f'You chose to play as {char_selected[1]}')
