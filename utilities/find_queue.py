from data_structures.active_channels import active_channels
from operator import itemgetter


async def find_queue(channel_id):
    temp = {}
    for k1, v1 in active_channels.items():
        if k1 == channel_id:
            for k2, v2 in v1.items():
                if str(k2) == 'Title' or str(k2) == 'chapter' or str(k2) == 'combat_flag' or str(k2) == 'monster' or str(k2) == 'rounds' or str(k2) == 'death_flag':
                    continue

                if isinstance(v2, int):
                    continue

                for k3, v3 in v2.items():
                    if str(k3) == 'Roll':
                        temp.update({k2: v3})

    initiative_queue = [(k, v) for k, v in temp.items()]
    initiative_queue.sort(key=itemgetter(1), reverse=True)
    return initiative_queue
