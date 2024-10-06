# The game starts here.
define player = Character("[player_name]")
image movie = Movie(channel="movie", play="videos/sun_dust_particles_byDanCristianPădureț.webm")
label start:
    play music "audio/begin_calm.mp3" volume 0.5 fadein 2.0

    scene movie
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


    call menu

    # Retorna ao menu principal após os créditos
    jump start

label menu:
    $ chapters_completed = set()

    while len(chapters_completed) < 3:
        menu:
            "Escolha um capítulo:"
            
            "Capítulo 1" if "1" not in chapters_completed:
                call chapter1
                $ chapters_completed.add("1")
            
            "Capítulo 2" if "2" not in chapters_completed:
                call chapter2
                $ chapters_completed.add("2")
            
            "Capítulo 3" if "3" not in chapters_completed:
                call chapter3
                $ chapters_completed.add("3")
            
            "Voltar ao menu principal":
                jump start

    # Após completar todos os capítulos, mostra os créditos
    call credits

label credits:
    scene black
    with fade

    show text "{size=40}Créditos{/size}" at truecenter
    with dissolve
    pause 2.0

    show text "{size=30}Desenvolvido por:\nSua Equipe{/size}" at truecenter
    with dissolve
    pause 2.0

    show text "{size=30}Agradecimentos especiais:\nNASA\nGLOBE Program{/size}" at truecenter
    with dissolve
    pause 2.0

    show text "{size=30}Música:\nCompositor X\nCompositor Y{/size}" at truecenter
    with dissolve
    pause 2.0

    show text "{size=40}Obrigado por jogar!{/size}" at truecenter
    with dissolve
    pause 3.0

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