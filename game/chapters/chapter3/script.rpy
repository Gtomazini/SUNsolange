# Back ground image
image background_coffee = "images/chapter3/coffee.png"

# name of the character.

define solange = ("Solange")

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

return