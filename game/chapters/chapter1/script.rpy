# The script of the game goes in this file.
image background_quintal = "images/quintal_sala.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Aunt Sol")
#efects
transform scream_shake:
    ease 0.05 xoffset 10
    ease 0.05 xoffset -10
    ease 0.05 xoffset 10
    ease 0.05 xoffset 0
    repeat 5

# The game starts here.

label chapter1:

    scene background_quintal
    "it's a nice day"
    scene background_quintal
    show layer master at scream_shake
    "CRACK CRACK BTHUMP"

#Olhar para a janela SOLANGE CAIDA NA LIXEIRA
    show eileen happy
    e "It's Aunt SOL"
    e "What's she doing"
    
    # This ends the game.

    return
