from data_structures.active_channels import active_channels


async def find_max(channel_id, client_name):
    temp = ""
    for k1, v1 in active_channels.items():
        if k1 == channel_id:
            for k2, v2 in v1.items():
                if str(k2) == 'Title' or str(k2) == 'chapter':
                    continue
                for k3, v3 in v2.items():
                    if str(k3) == 'Roll':
                        temp = {k2: v3}

    initiative_queue = {k: v for k, v in sorted(temp.items(), key=lambda item: item[1])}

    return initiative_queue
