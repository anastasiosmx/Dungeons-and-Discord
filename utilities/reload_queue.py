from data_structures.active_channels import active_channels
from utilities.find_queue import find_queue


async def reload_queue(channel_id):
    queue = await find_queue(channel_id)

    rounds = len(queue)
    if 'rounds' not in active_channels[channel_id]:
        active_channels[channel_id]['rounds'] = {}
    active_channels[channel_id].update({'rounds': rounds})

    return queue
