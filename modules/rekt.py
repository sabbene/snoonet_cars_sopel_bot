import sopel
import unicodedata
import random

rekt_list = ['Rekt', 'Really Rekt', 'Tyrannosaurus Rekt', 'Cash4Rekt.com', 'Grapes of Rekt', 'Ship Rekt', 'Rekt markes the spot', 'Caught rekt handed', 'The Rekt Side Story', 'Singin\' In The Rekt', 'Painting The Roses Rekt', 'Rekt Van Winkle', 'Parks and Rekt', 'Lord of the Rekts: The Reking of the King', 'Star Trekt', 'The Rekt Prince of Bel-Air', 'A Game of Rekt', 'Rektflix', 'Rekt it like it\'s hot', 'RektBox 360', 'The Rekt-men', 'School Of Rekt', 'I am Fire, I am Rekt', 'Rekt and Roll', 'Professor Rekt', 'Catcher in the Rekt', 'Rekt-22', 'Harry Potter: The Half-Rekt Prince', 'Great Rektspectations', 'Paper Scissors Rekt', 'RektCraft', 'Grand Rekt Auto V', 'Call of Rekt: Modern Reking 2', 'Legend Of Zelda: Ocarina of Rekt', 'Rekt It Ralph', 'Left 4 Rekt', 'Pokemon: Fire Rekt',
        'The Shawshank Rektemption', 'The Rektfather', 'The Rekt Knight', 'Fiddler on the Rekt', 'The Rekt Files', 'The Good, the Bad, and The Rekt', 'Forrekt Gump', 'The Silence of the Rekts', 'The Green Rekt', 'Gladirekt', 'Spirekted Away', 'Terminator 2: Rektment Day', 'The Rekt Knight Rises', 'The Rekt King', 'REKT-E', 'Citizen Rekt', 'Requiem for a Rekt', 'REKT TO REKT ass to ass', 'Star Wars: Episode VI - Return of the Rekt', 'Braverekt', 'Batrekt Begins', '2001: A Rekt Odyssey', 'The Wolf of Rekt Street', 'Rekt\'s Labyrinth', '12 Years a Rekt', 'Gravirekt', 'Finding Rekt', 'The Arekters', 'There Will Be Rekt', 'Christopher Rektellston', 'Hachi: A Rekt Tale', 'The Rekt Ultimatum', 'Shrekt', 'Rektal Exam', 'Rektium for a Dream', 'The Hunt for Rekt October', 'Oedipus rekt']

@sopel.module.commands('rekt')


def rekt(bot, trigger):
    random.seed()
    if trigger.group(2):

        out = trigger.group(2) + ': ' + (rekt_list[random.randrange(74)]) + '\n'
    else:
        out = (rekt_list[random.randrange(74)]) + '\n'
    return bot.say(out)
    
