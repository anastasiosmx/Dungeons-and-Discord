import discord
import random

TOKEN = ""
Client = discord.Client()
active_channels = {}
adventures_titles = [
    "Out of the Abyss",
    "Save the King!",
    "The dark ring",
    "Missing children"
]
characters = {
     'WARRIOR': {
        'HP': 100,
        'name': 'Aldway Wolfee',
        'Weapons': {
            'Great Sword': '1d10',
            'Small Dagger': '1d4'
        },
        'Spells': None,
        'Abilities': None,
        'Items': {
            'Great Shield': 80,
            'Great Armor': 100
        },
        'Description': 'Aldway Wolfee was born in a small village close to the capital. From very young age he liked to'
                       ' train with the sword of his grandfather.'
    }, 'WIZARD': {
        'HP': 40,
        'name': 'Richard Foerstnerg',
        'Weapons': None,
        'Spells': {
            'Fireball': '3d6',
            'Spikes': '1d6'
        },
        'Abilities': None,
        'Items': {
            'Wooden Shield': 30,
            'Lite Armor': 20
        },
        'Description': 'Richard Foerstnerg was born in the capital. He always tried to transform his little brother'
                       ' into a frog. He eventually went to Wizard school and became a Wizard'
    }, 'MONK': {
        'HP': 60,
        'name': 'Humbert Garverg',
        'Weapons': None,
        'Spells': None,
        'Abilities': {
            'Power Kick': '2d6',
            'Punch': '1d6'
        },
        'Items': {
            'Medium Shield': 50,
            'Medium Armor': 60
        },
        'Description': 'Humbert Garverg was born in a monastery up to the big mountains. After mastering the art of '
                       'karate he choose to fight for the weak and bring peace to the realm'
    }, 'CLERIC': {
        'HP': 120,
        'name': 'Jarl Beckete',
        'Weapons': None,
        'Spells': {
            'Power Healing': '3d4',
            'Music punch': '1d4'
        },
        'Abilities': None,
        'Items': {
            'Great Shield': 80,
            'Medium Armor': 60
        },
        'Description': 'Jarl Beckete was abandon when he was a child by his mother outside a church. He now fights'
                       'to save anyone who need him.'
    }}


def print_characters(char_type):
    char = char_type.upper()
    return(f'''**{char.lower()}**: 
    __Name__: {characters[char]['name']}
    __Total HP__: {characters[char]['HP']}
    __Weapons__: {characters[char]['Weapons']}
    __Spells__: {characters[char]['Spells']}
    __Abilities__: {characters[char]['Abilities']}
    __Items__: {characters[char]['Items']}
    __Description__: {characters[char]['Description']}
    ''')


async def send_welcome_msg(channel):
    await channel.send('''Welcome great adventurers!
            Ready to live a great adventure? If you don't want to fight alone you can invite your friends to this channel.
            In the meantime choose your character wisely...
            1. Warrior
            2. Wizard
            3. Monk
            4. Cleric
            To view more info about characters abilities, weapons and background type __^view_char Wizard__ 
            To choose a character type __^choose Wizard__
            To see all available commands type ^help''')


@Client.event
async def on_ready():
    print(f'We have logged in as {Client.user}')


@Client.event
async def on_message(message):
    user_id = message.author
    guild_id = message.guild.id
    guild = Client.get_guild(guild_id)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    if user_id == Client.user:
        return

    if message.content.startswith('^help'):
        await message.channel.send('''
        __Help__
        1. **^new_game** - Starts a new game.
        2. **^help**     - Prints this message.
        3. **^view_char [class name]** - Prints details about a character.
        4. **^choose [class name]** - Select character to play with.
        5. **^start** - Starts the game, be sure that everyone chose a class before starting.
        ''')

    if message.content.startswith('^new_game'):
        adv_title = random.choice(adventures_titles)
        category_exist = discord.utils.get(guild.categories, name='Dungeons & Discord')
        print(category_exist)

        if category_exist is None:
            category = await guild.create_category('Dungeons & Discord', overwrites=overwrites)
            channel = await guild.create_text_channel(adv_title, overwrites=overwrites, category=category)
        else:
            channel = await guild.create_text_channel(adv_title, overwrites=overwrites, category=category_exist)
        await message.channel.send("Close the lights! A new adventure begins...🐉")
        await send_welcome_msg(channel)

    if message.content.startswith('^view_char'):
        char_type = message.content.split()
        await message.channel.send(print_characters(char_type[1]))

    if message.content.startswith('^choose'):
        client_name = message.author.name
        channel_id = message.channel.id
        channel_name = message.channel.name
        char_selected = message.content.split()

        if channel_id not in active_channels:
            active_channels[channel_id] = {}
        active_channels[channel_id].update({'Title': channel_name})

        if client_name not in active_channels[channel_id]:
            active_channels[channel_id][client_name] = {}
        active_channels[channel_id].update({client_name: char_selected[1]})

        print(active_channels)
        await message.channel.send(f'You chose to play as {char_selected[1]}')

Client.run(TOKEN)
