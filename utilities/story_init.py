from data_structures.active_channels import active_channels


async def story_init(channel_id):
    active_channels[channel_id]["chapter"] = {}
    active_channels[channel_id].update({"chapter": 1})
