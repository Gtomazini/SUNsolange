# The script of the game goes in this file.
image background_quintal = "images/quintal_sala.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Aunt Sol")
#efects
transform scream_shake:
    xoffset 10  # Mova 10 pixels à direita
    linear 0.05 xoffset -10  # Mova 10 pixels à esquerda
    linear 0.05 xoffset 10  # Repete o movimento
    repeat 5  # Repete o movimento 5 vezes (ajuste conforme necessário)

# The game starts here.

label chapter1:

    scene background_quintal
    "it's a nice day"
    scene background_quintal with scream_shake
    "CRACK CRACK BTHUMP"

#Olhar para a janela SOLANGE CAIDA NA LIXEIRA
    show eileen happy
    e "It's Aunt SOL"
    e "What's she doing"
    
    # This ends the game.

    return
