# Declarações de imagens
image water = "images/chapter3/water.png"
image thermo = "images/chapter3/thermo.png"
image stratus_cloud = "images/chapter3/stratus_cloud.jpg"
label star_temp_game:


    $ score = 0
    $ questions = 3

    scene water
    solange "There! A good example to explain a little about my project."

    menu:
        "So..to measure the earth surface they use glasses?":
            call pathE4
        
    label pathE4:
        "*SOLANGE SEENS CONFUSED ABOUT YOUR QUESTION"
        solange "No, wait! The glasses are just a demonstration. GLOBE uses special sensors to measure the temperature of the Earth's surface.
        These sensors are much more precise and can be used on different types of terrain. Our experiment with the glasses is just a simple way
        of understanding the basic concept of how different surfaces absorb and retain heat differently."

        menu:
            "So how do glasses fit into this?":
                call pathE5

    label pathE5:
        solange "Great question! A table without a cup holder is like exposed soil, it heats up quickly. The cup holder on the table is like an
        area with plants, it heats up slowly."

        player "Got it. And does that help scientists?"

        solange "Yes, it helps to understand things like heat islands in cities and changes in the local climate."

        player "Cool! And people can help with that?"

        solange "Of course! People like you collect data for GLOBE, contributing to global temperature studies."

        player "It makes me think about my own city..."

        solange "Great! Think about how different surfaces in your community affect temperature. This is how we connect our simple experiment with the larger work of GLOBE!"

        player "So how can we check the difference between these glasses and their temperature?"

        solange "Hold on."

        "*SHE MOVES THE GLASSES, LEAVING 1 ON THE CUP HOLDER AND THE OTHER 2 DIRECTLY ON THE TABLE, BUT ONE OF THEM SEEMS TO HAVE A METALLIC SOUND WHEN PLACED...*"

        solange "Let's wait a few minutes!"

        "*15 MINUTES LATER*"

        show thermo at center
        solange "Let's use my infrared thermometer, it will be enough to explain."

    label .quiz1:
        $ questions -= 1
        hide thermo
        menu:
            solange "Which of the three glasses is the hottest??"
            "The one in the table":
                $ score += 1
                solange "That's right! The wooden table retains more heat and transfers it to the glass more than the others."
            "The one in the cup holder":
                "Try again! The cup holder, despite having received heat from the sun, is an excellent thermal insulator. It heats up,
                but doesn't transfer heat efficiently to the cup like the wooden table, keeping the bottom of the cup relatively insulated."
                jump .quiz1
            "The other one on the table, but which has a metallic sound when it's been placed":
                "Almost! This glass have a aluminum foil under him. Even though aluminum is a good conductor, its reflective surface means that
                it absorbs less heat from direct sunlight, which means that the first glass directly on the wooden table heats up more quickly than this glass on the aluminum foil."
                jump .quiz1

    label .quiz2:
        $ questions -= 1
        show altocumulus_cloud at truecenter
        menu:
            "Que tipo de nuvem é esta?"
            "Cirrus":
                "Incorreto. Estas são nuvens Altocumulus. Vamos tentar novamente."
                jump .quiz2
            "Altocumulus":
                $ score += 1
                "Correto! Estas são nuvens Altocumulus."
            "Stratus":
                "Incorreto. Estas são nuvens Altocumulus. Vamos tentar novamente."
                jump .quiz2

    label .quiz3:
        $ questions -= 1
        show stratus_cloud at truecenter
        menu:
            "Que tipo de nuvem é esta?"
            "Cirrus":
                "Incorreto. Estas são nuvens Stratus. Vamos tentar novamente."
                jump .quiz3
            "Altocumulus":
                "Incorreto. Estas são nuvens Stratus. Vamos tentar novamente."
                jump .quiz3
            "Stratus":
                $ score += 1
                "Correto! Estas são nuvens Stratus."

    "Parabéns! Você completou o Quiz de Nuvens. Sua pontuação final é [score] de 3."

    return