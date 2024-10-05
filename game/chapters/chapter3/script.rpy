# Back ground image
image background_coffee = "images/chapter3/coffee.png"
# Solange
image solange = "images/chapter3/solange/sun_coffee1.png"

# name of the character.

define solange = Character("Solange")
define person = Character("Unknown")

# The game starts here.

label chapter3:
    # Background scene
    scene background_coffee
    # Narrator
    person "*GLASH* *GLUP* *GLAP*"
    # Player
    "What was that?"

    # Scream shake
    show layer master at scream_shake
    person "*Cough* *Cough*"
    pause 0.5 
    hide layer master

    # Player
    "Are you okay?"

    # Scream shake
    show layer master at scream_shake
    person "*Cough* *Cough*"
    pause 0.5
    hide layer master

    # Player
    "Yeah.."

    # Scream shake
    show layer master at scream_shake
    person "*Cough* *Cough*"
    pause 0.5
    hide layer master

    # Player
    "..."

    # Solange
    show solange at center
    person "Yes"

    # Player
    "Okay"

    # Player
    "..."


    return