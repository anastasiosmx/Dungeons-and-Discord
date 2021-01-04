async def send_welcome_msg(channel):
    await channel.send('''Welcome great adventurers!
            Ready to live a great adventure? If you don't want to fight alone you can invite your friends to this channel.
            In the meantime choose your character wisely...
            1. Warrior
            2. Wizard
            3. Monk
            4. Cleric
            To view more info about characters abilities, weapons and background type __^view_char Wizard__ 
            To choose a character type __^choose_char Wizard__
            To see all available commands type ^help''')
