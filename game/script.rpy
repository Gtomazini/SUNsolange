﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[player_name]")
image movie = Movie(channel="movie", play="videos/sun_dust_particles_byDanCristianPădureț.webm")





# The game starts here.

label start:
    play music "audio/begin_calm.mp3" volume 0.5 fadein 2.0


    scene movie
    # ele vai digitar aos poucos
    "{cps=30}Just as the heat of the sun warms our faces regardless of distance, this is a story of mine, yours and ours.{/cps}"


    # Requests the player's name
    $ player_name = renpy.input("What's your name?")
    # If it's empty, you'll put a 'Player' name on it
    $ player_name = player_name.strip() or "Player" 
    # Request the player's age
    $ player_age = renpy.input("How old are you?")
    
    # Checks if the value entered is a number
    while not player_age.isdigit():
        $ player_age = renpy.input("Please enter a valid number for your age.")
    # Convert age to an integer
    $ player_age = int(player_age)

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