import discord
from settings.settings import TOKEN
from utilities.new_game import new_game
from utilities.help_msg import help_msg
from utilities.choose_character import choose_character
from utilities.start_chapter import start_chapter
from utilities.print_characters import print_characters
from utilities.story_init import story_init


Client = discord.Client()


@Client.event
async def on_ready():
    print(f'We have logged in as {Client.user}')


@Client.event
async def on_message(message):
    user_id = message.author
    guild_id = message.guild.id
    guild = Client.get_guild(guild_id)
    channel_id = message.channel.id

    if user_id == Client.user:
        return

    if message.content.startswith('^help'):
        await help_msg(message)

    if message.content.startswith('^new_game'):
        await new_game(guild, message)

    if message.content.startswith('^view_char'):
        char_type = message.content.split()
        await message.channel.send(print_characters(char_type[1]))

    if message.content.startswith('^choose_char'):
        await choose_character(message, channel_id)

    if message.content.startswith('^start'):
        option_tmp = 1
        await story_init(channel_id)
        await start_chapter(channel_id, message, option_tmp)

    if message.content.startswith('^choose_opt'):
        option_tmp = message.content.split()
        option = option_tmp[1]

        await start_chapter(channel_id, message, option)

Client.run(TOKEN)
