import discord
from settings.settings import TOKEN
from utilities.new_game import new_game
from utilities.help_msg import help_msg
from utilities.choose_character import choose_character
from utilities.start_chapter import start_chapter
from utilities.print_characters import print_characters
from combat.roll_init import roll_init
from combat.init_combat import init_combat
from combat.attack import attack


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
    client_name = message.author.name

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
        await choose_character(message, channel_id, client_name)

    if message.content.startswith('^start'):
        option_tmp = 1
        start = 1
        await start_chapter(channel_id, message, option_tmp, start)

    if message.content.startswith('^choose_opt'):
        start = 0
        option_tmp = message.content.split()
        option = option_tmp[1]
        await start_chapter(channel_id, message, option, start)

    if message.content.startswith('^roll_init'):
        await roll_init(message, channel_id, client_name, True)

    if message.content.startswith('^init_combat'):
        await init_combat(message, channel_id)

    if message.content.startswith('^use'):
        msg_tmp = message.content.split()
        attack_type = msg_tmp[1].upper()
        action = msg_tmp[2].upper()
        await attack(message, channel_id, client_name, attack_type, action)

Client.run(TOKEN)
