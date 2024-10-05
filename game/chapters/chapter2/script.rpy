# Back ground image
image background_escola = "images/corredor_escola.png"

# name of the character.

define solange = ("Solange")

# The game starts here.

label chapter2:
# Background scene
    scene background_escola
# Scream shake
    show layer master at scream_shake
# Narrator
    "CRAMB CRAMB TCHUMM"
# Player
    player "What was that?!"
# Image of the fallen veteran
#
    player "'What's she doing?'"
    player "Hey..."    
# Image of the frightened veteran 
#
# Scream shake
    show layer master at scream_shake
    solange "YAHAH!!!!"


    return