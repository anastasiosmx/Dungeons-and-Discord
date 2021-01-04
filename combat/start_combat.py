from utilities.find_max import find_max


async def start_combat(message, channel_id, client_name):
    queue = await find_max(channel_id, client_name)
    await message.channel.send(f'The queue is: {queue}')
