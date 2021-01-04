from data_structures.characters import characters


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
