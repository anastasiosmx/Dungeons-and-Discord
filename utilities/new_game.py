import discord
import random
from data_structures.adventures import adventures_titles
from utilities.send_welcome_msg import send_welcome_msg


async def new_game(guild, message):
    adv_title = random.choice(adventures_titles)
    category_exist = discord.utils.get(guild.categories, name='Dungeons & Discord')

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    if category_exist is None:
        category = await guild.create_category('Dungeons & Discord', overwrites=overwrites)
        channel = await guild.create_text_channel(adv_title, overwrites=overwrites, category=category)
    else:
        channel = await guild.create_text_channel(adv_title, overwrites=overwrites, category=category_exist)
    await message.channel.send("Close the lights! A new adventure begins...🐉")
    await send_welcome_msg(channel)
