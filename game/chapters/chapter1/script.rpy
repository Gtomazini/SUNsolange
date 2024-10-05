# The script of the game goes in this file.
image background_room = "images/quintal_sala.png"
image background_quintal = "images/quintal_quintal.png"
image background_solixo = "images/quintal_lixo.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Aunt Sol")
define u = Character("You")
#efects
transform scream_shake:
    ease 0.05 xoffset 10
    ease 0.05 xoffset -10
    ease 0.05 xoffset 10
    ease 0.05 xoffset 0
    repeat 5

# The game starts here.

label chapter1:
    scene background_room
    "it's a nice day"
    show layer master at scream_shake
    "CRACK CRACK BTHUMP"
    "What's this"
    "He looked out of the window and saw Aunt Sol lying on the ground"
    scene background_solixo
    u "It's Aunt SOL"
    u "What's she doing?"
    scene background_quintal
    "You hear strange noises"


    
    # This ends the game.

    return
