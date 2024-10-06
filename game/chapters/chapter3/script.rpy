# Back ground image
image background_coffee = "images/chapter3/coffee.png"
# Solange
image solange = "images/chapter3/solange/sun_coffee.png"
image solange_h = "images/chapter3/solange/sun_coffee_happy.png"
image solange_hc = "images/chapter3/solange/sun_coffee_hc40.png"

# name of the character.

define solange = Character("Solange")
define person = Character("Unknown")

# The game starts here.

label chapter3:
    play music "audio/cafeteria.mp3" volume 0.5 fadein 2.0
    # Background scene
    scene background_coffee
    # Narrator
    person "*GLUP* *GLUP* *GLAP*"
    # Player
    player "What was that?"

    # Scream shake
    show layer master at scream_shake
    person "*Cough* *Cough*"
    pause 0.5 
    hide layer master

    # Player
    player "Are you okay?"

    # Scream shake
    show layer master at scream_shake
    person "*Cough* *Cough*"
    pause 0.5
    hide layer master

    # Player
    player "Yeah.."

    # Scream shake
    show layer master at scream_shake
    person "*Cough* *Cough*"
    pause 0.5
    hide layer master

    # Player
    player "..."

    # Solange
    show solange at center
    person "Yes"

    # Player
    player "Okay"

    # Player
    person "..."

    # Player diálogo
    menu:
        "So what's your name? What are you doing dressed like that?":
            call pathE
    return

label pathE:
    # Solange
    solange "My name is Solange, i am a pertinent citizen concerned about our climate, and a researcher
    finishing a project for NASA *NOISE OF PRIDE*"
    
    # Player
    player "...ok, and what are you doing here right now? Shouldn't you be in your lab?"

    # Solange
    solange "Yes hahaha..! I'm just taking a break, there's so much GLOBE Protocol data to analyze...I
    needed a coffee before cotinuing"

    # Player diálogo 2
    menu:
        "GLOBE Protocol??":
            call pathE1
        "Oh, that NASA sponsored GLOBE Protocol??":
            call pathE2
        "Oh yes, the GLOBE Protocol that defines global laws!":
            call pathE3
    return

label pathE1:
    # Solange
    hide solange
    show solange_hc
    solange "Yes, the GLOBE Protocol is a program where ordinary people collect environmental data,
    such as surface temperature, using scientific methods. My project simulates, on a small scale,
    what GLOBE studies globally. This helps understand how different surfaces affect local and global climate."

    player "So..what are your project based on?"

    hide solange_hc
    show solange
    solange "My project aims to measure the environmental impacts caused by temperature on the ground, as well
    as its variations depending on the location and materials affected by sunlight. I'll show you an example"
    call temperature_game

label pathE2:
    # Solange
    hide solange
    show solange_h at center
    solange "YES!! I don't believe i found someone who knows and cares about environmental issues!!
    Points for you!!"

    player "So..what are your project based on?"

    hide solange_h
    show solange
    solange "My project aims to measure the environmental impacts caused by temperature on the ground, as well
    as its variations depending on the location and materials affected by sunlight. I'll show you an example"
    call temperature_game

label pathE3:
    # Solange
    hide solange
    show solange_hc
    solange "No ! No, that's not it, if it were a test you'd get a zero hahaha"
    hide solange_hc
    show solange
    solange "Globe Protocol is not about global law programs, but rather a global
    effort to collect data about our environment, I'll show you an example!"
    call temperature_game

    return
