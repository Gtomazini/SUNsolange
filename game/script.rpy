# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    # Menu principal com três opções
    menu:
        "Escolha um capítulo:"
        
        "Capítulo 1":
            call chapter1
        
        "Capítulo 2":
            call chapter2
        
        "Capítulo 3":
            call chapter3
    
    # Após retornar de um capítulo, volta ao menu principal
    jump start

    return

# Define o label para chamar o script do Capítulo 1
label chapter1_script:
    call chapter1
    return

# Define o label para chamar o script do Capítulo 1
label chapter2_script:
    call chapter2
    return

# Define o label para chamar o script do Capítulo 1
label chapter3_script:
    call chapter3
    return