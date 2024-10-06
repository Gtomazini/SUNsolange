# The script of the game goes in this file.
image background_room = "images/chapter1/quintal_sala.png"
image background_quintal = "images/chapter1/quintal_quintal.png"
image background_solixo = "images/chapter1/quintal_lixo.png"
image AuntSol = "images/chapter3/solange/sun_coffee1.png"
image background_river = "images/chapter1/quintal_fundos.png" 
image solph = "images/chapter1/solange_ph.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sol = Character("Aunt Sol")
#efects
transform scream_shake:
    ease 0.05 xoffset 10
    ease 0.05 xoffset -10
    ease 0.05 xoffset 10
    ease 0.05 xoffset 0
    repeat 6

# The game starts here.

label chapter1:
    scene background_room
    #NARATOR
    "It's a nice day"
    "You hear strange noises"
    #Scream shakes
    show layer master at scream_shake
    #sound of shake
    "CRACK CRACK BTHUMP"
    #PLAYER
    player "What's this"
    #NArator
    "You looked out of the window"
    scene background_solixo
    player "It's Aunt SOL"
    player "What's she doing?"
    "Aunt Sol disappears and you hear strange noises again"
    scene background_quintal
    play music "audio/quintal.mp3" volume 0.5 fadein 2.0
    "You're going to open the fence door"
    #som de cerca abrindo
    show AuntSol at center
    "Aunt Sol look sad because my ph meter is broken"
    player "What's happening ?"
    "Aunt Sol have an idea and disappears"
    "Glass and plastic noises from unboxing"
    #SOL IMAGE WITH A NEW PH MESUIR
    sol "Here, take a sample for me"
    player "What?"
    sol "{fast}For a precise analysis of aquatic pH, we used a glass electrode combined with a silver/silver chloride reference electrode,
calibrated with phosphate and phthalate buffer solutions."
    sol "{fast} Potentiometric measurement is based on the Nernst equation, taking into account the activity of hydronium ions in solution. It is crucial to take into account ionic strength,
temperature and liquid junction effects. "
    sol "{fast}We use potentiometric titration techniques to determine alkalinity and acidity, using indicators such as phenolphthalein and methyl orange.
Data interpretation requires chemical speciation analysis, considering complex acid-base balances in natural aquatic systems,
including the carbonate system and the presence of humic and fulvic acids which can significantly affect the pH and buffering capacity of water"
    #NARRETOR
    "You DO NOT understand anything"
    #dialogue
    player "..."
    sol "..."
    sol "Sorry, let's do something fun"
    player "Fun? Let's Go"
    sol "Imagine you're a detective, but instead of solving crimes, you're investigating our planet!"
    sol "For example, you can measure the temperature, identify types of clouds in the sky, or even count how much it has rained!"
    sol "How about we start our scientific adventure right now?"
    sol "But first I'll teach you a little about water measurements"
    scene background_river
    #PICTURE OF PHMETER
    show solph at right
    sol "Did you know that water can be acidic, neutral, or alkaline? To find out, we use a device called a pH meter!"
    menu :
        "No":
            "No problem, you'll learn"
        "YESSS":   
            "Let's GOoooo"
    sol "The pH meter looks like a ruler with a needle that moves. When we dip the tip into the water, the needle shows a number that helps us know if the water is good to drink."
    sol "First, we need to make sure the pH meter is clean. Then, we take a glass of the water we want to test, like tap water or water from a lake."
    sol "Now, we dip the tip of the pH meter into the water and count to three. The needle starts to move and stops at a number. This number tells us if the water is acidic, neutral, or alkaline!"
    sol "If the needle stops at a number less than 7, the water is acidic, like lemon. If it stops at 7, the water is neutral,
like the water we drink. If the number is greater than 7, the water is alkaline, like baking soda."
    #o2 meter
    sol "Now let's learn about the water oxygen meter"
    sol "First, we need to prepare the meter. It should be nice and clean to work properly!"
    # Image of a glass of water
    sol "Now, let's get a glass of water. It  from the river. Let's go!"

    # Image of the oxygen meter being used
    sol "Great! Now, dip the tip of the oxygen meter into the water and count to five. Let's see what happens!"

    # Image of the meter showing the result
    sol "Look! The number that appears on the meter tells us if the water has enough oxygen. The higher, the better!"
    #thermal
    sol "And finally, let's learn about the water temperature gauge"
    # Image of the thermometer being prepared
    sol "First, we need to prepare the thermometer. Just like the oxygen meter, it also needs to be clean."
    # Image of a glass of water
    sol "Next, let's get a glass of water. It can be tap water or water from a lake. Let's use a full glass!"

    # Image of the thermometer being used
    sol "Now, dip the tip of the thermometer into the water and count to three. Let's see the temperature!"

    # Image of the thermometer showing the result
    sol "See! The number that appears on the thermometer tells us if the water is cold, warm, or hot."

    sol "Now to the challenge"
    #botão de iniciar

    # This ends the game.

    return
