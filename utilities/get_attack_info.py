from data_structures.active_channels import active_channels


async def get_attack_info(channel_id, client_name):
    monster_name = active_channels[channel_id]['monster']['monster_name']
    monster_hp = int(active_channels[channel_id]['monster']['HP'])

    player_class = active_channels[channel_id][client_name]['Class']
    player_hp = active_channels[channel_id][client_name]['HP']

    total_rounds = active_channels[channel_id]['rounds']

    return monster_name, monster_hp, player_class, player_hp, total_rounds
