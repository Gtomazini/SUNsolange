# Back ground image
image background_coffee = "images/chapter3/coffee.png"
# Solange
image solange = "images/chapter3/solange/sun_coffee_empty.png"
# Solange
image solange_h = "images/chapter3/solange/sun_coffee_happy.png"

# name of the character.

define solange = Character("Solange")
define person = Character("Unknown")

# The game starts here.

label chapter3:
    play music "audio/cafeteria.mp3" volume 0.5 fadein 2.0
    # Background scene
    scene background_coffee
    # Narrator
    person "*GLASH* *GLUP* *GLAP*"
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
    solange ""

    return

label pathE2:
    # Solange
    show solange_h at center
    solange "YES!! I don't believe i found someone who knows and cares about environmental issues!!
    Points for you!!"

    return

label pathE3:
    # Solange
    solange ""
