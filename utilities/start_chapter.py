from data_structures.active_channels import active_channels


async def start_chapter(channel_id, message, option):
    chapter_count = int(active_channels[channel_id]["chapter"])
    with open(f'./campaigns/{active_channels[channel_id]["Title"]}_{chapter_count}_{option}.txt', 'r') as campaign:
        story = campaign.read()
    campaign.close()

    await message.channel.send(story)

    chapter_count = 1 + chapter_count
    chapter_tmp = {"chapter": str(chapter_count)}
    active_channels[channel_id].update(chapter_tmp)
