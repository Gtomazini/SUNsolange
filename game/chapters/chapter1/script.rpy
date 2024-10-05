# The script of the game goes in this file.
image background_room = "images/chapter1/quintal_sala.png"
image background_quintal = "images/chapter1/quintal_quintal.png"
image background_solixo = "images/chapter1/quintal_lixo.png"
image AuntSol = "images/chapter1/Auntsol.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sol = Character("Aunt Sol")
#efects
transform scream_shake:
    ease 0.05 xoffset 10
    ease 0.05 xoffset -10
    ease 0.05 xoffset 10
    ease 0.05 xoffset 0
    repeat 5

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
    "You looked out of the window and saw Aunt Sol lying on the ground"
    scene background_solixo
    player "It's Aunt SOL"
    player "What's she doing?"
    scene background_quintal
    "Aunt Sol disappears and you hear strange noises again"
    "You're going to open the fence door"
        #som de cerca abrindo
    show sol at center
    sol "I'm sad because my ph meter is broken"
    player "What's happening ?"
    "Aunt Sol have an idea and disappears"
    "Glass and plastic noises from unboxing"
    #SOL IMAGE WITH A NEW PH MESUIR
    sol "Here, take a sample for me"
    player "What?"
    sol "{fast}For a precise analysis of aquatic pH, we used a glass electrode combined with a silver/silver chloride reference electrode, calibrated with phosphate and phthalate buffer solutions. Potentiometric measurement is based on the Nernst equation, taking into account the activity of hydronium ions in solution. It is crucial to take into account ionic strength, temperature and liquid junction effects. We use potentiometric titration techniques to determine alkalinity and acidity, using indicators such as phenolphthalein and methyl orange. Data interpretation requires chemical speciation analysis, considering complex acid-base balances in natural aquatic systems, including the carbonate system and the presence of humic and fulvic acids which can significantly affect the pH and buffering capacity of water"
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
    #PICTURE OF PHMETER
    sol "Did you know that water can be acidic, neutral or alkaline? And to find out, we use a very cool device called a pH meter!"
    sol "Imagine you have a pH meter in your hands. It looks like a ruler with a needle that moves.
When you dip the tip of this device into the water, the needle shows you a number that helps you understand whether the water is good to drink or whether there's something wrong with it."
    sol "First, we need to make sure that the pH meter is clean. That way, it can measure properly! Then we take a glass of the water we want to test, either tap water or water from a lake."
    sol "Then we dip the tip of the pH meter into the water and count to three. Look how magical it is: the needle starts to move and, after a little while, stops at a number on the scale.
This number tells us whether the water is acidic, neutral or alkaline!"
    sol "If the needle stops at a number less than 7, it means that the water is acidic, like lemon. If it stops at exactly 7, the water is neutral,
like the water we drink. And if the number is greater than 7, the water is alkaline, like bicarbonate."
    sol "Now to the challenge"
    #botão de iniciar

    # This ends the game.

    return
