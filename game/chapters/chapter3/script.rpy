# Back ground image
image background_coffee = "images/chapter3/coffee.png"
# Solange
image solange = "../Concepts/sun_coffee"

# name of the character.

define solange = Character("Solange")

# The game starts here.

label chapter3:
    # Background scene
    scene background_coffee
    # Narrator
    "GLASH GLUP GLAP"
    # Player
    "What was that?"

    # Scream shake
    show layer master at scream_shake
    "TOSSE TOSSE"
    pause 0.5 
    hide layer master

    # Player
    "Are you okay?"

    # Scream shake
    show layer master at scream_shake
    "TOSSE TOSSE"
    pause 0.5
    hide layer master

    # Player
    "Yeah.."

    # Scream shake
    show layer master at scream_shake
    "TOSSE TOSSE"
    pause 0.5
    hide layer master

    # Player
    "..."

    # Solange
    show sun at center
    "Sim"

    # Player
    "Tá"

    # Player
    "..."


    return