from data_structures.active_channels import active_channels


async def monster_is_dead(message, channel_id, monster_hp):
    if monster_hp <= 0:
        await message.channel.send(f'You destroyed this monster! Quick we must move on to the next challenge!')

        active_channels[channel_id].update({'combat_flag': 0})
        del active_channels[channel_id]['monster']
        del active_channels[channel_id]['rounds']

        return True
    return False


async def player_is_dead(message, player_hp, client_name, channel_id):
    if player_hp <= 0:
        await message.channel.send(f'{client_name} DIED ☠️')

        if 'death_flag' not in active_channels[channel_id][client_name]:
            active_channels[channel_id][client_name]['death_flag'] = {}
        active_channels[channel_id][client_name].update({'death_flag': 1})

        return True
    return False
