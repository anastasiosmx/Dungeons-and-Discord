from data_structures.active_channels import active_channels
from utilities.story_init import story_init

# TODO Create stop combat --> active_channels[channel_id]['combat_flag'] set to 0 from 1 to unlock story continue
async def start_chapter(channel_id, message, option, start):
    if start == 1:
        active_channels[channel_id]['combat_flag'] = {}
        await story_init(channel_id)

    if active_channels[channel_id]['combat_flag'] == 1:
        print('I AM HERE')
        return

    chapter_count = int(active_channels[channel_id]["chapter"])
    with open(f'./campaigns/{active_channels[channel_id]["Title"]}_{chapter_count}_{option}.txt', 'r') as campaign:
        story = campaign.read()
    campaign.close()

    chapter_count = 1 + chapter_count
    chapter_tmp = {"chapter": str(chapter_count)}
    active_channels[channel_id].update(chapter_tmp)

    # Combat mode: ON
    if story[0] == 'O':
        active_channels[channel_id].update({'combat_flag': 1})
        await message.channel.send("Something bad is going to happen....Roll for initiative! [^roll_init]")
        return

    await message.channel.send(story)
