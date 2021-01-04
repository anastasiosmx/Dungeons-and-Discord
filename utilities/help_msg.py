async def help_msg(message):
    await message.channel.send('''
            __Help__
            1. **^new_game** - Starts a new game.
            2. **^help**     - Prints this message.
            3. **^view_char [class name]** - Prints details about a character.
            4. **^choose_char [class name]** - Select character to play with.
            5. **^start** - Starts the game, be sure that everyone chose a class before starting.
            6. **^choose_opt [Number]** - Select an option
            ''')