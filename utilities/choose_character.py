from data_structures.active_channels import active_channels


async def choose_character(message, channel_id):
    client_name = message.author.name
    channel_name = message.channel.name
    char_selected = message.content.split()

    if channel_id not in active_channels:
        active_channels[channel_id] = {}
    active_channels[channel_id].update({'Title': channel_name})

    if client_name not in active_channels[channel_id]:
        active_channels[channel_id][client_name] = {}
    active_channels[channel_id].update({client_name: char_selected[1]})

    await message.channel.send(f'You chose to play as {char_selected[1]}')
