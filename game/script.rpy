# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    # Chama o script do Capítulo 1
    #call chapter1_script

    # O código abaixo só será executado após o retorno do chapter1_script
    scene bg room
    show eileen happy

    e "Agora estamos no loop main"
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return

# Define o label para chamar o script do Capítulo 1
label chapter1_script:
    call chapter1
    return