# Declarações de imagens
image water = "images/chapter3/water.png"
image thermo = "images/chapter3/thermo.png"
image sun_thermo = "images/chapter3/solange/sun_thermo.png"
image sun_confused = "images/chapter3/solange/sun_confused.png"
label temperature_game:

    $ score = 0
    $ questions = 3

    scene background_coffee with fade
    scene water with fade
    solange "There! A good example to explain a little about my project."

    menu:
        "So..to measure the earth surface they use glasses?":
            call pathE4
        
    label pathE4:
        hide solange
        show sun_confused at center
        "*SOLANGE SEENS CONFUSED ABOUT YOUR QUESTION*"
        show layer master at scream_shake
        solange "No, wait! The glasses are just a demonstration. GLOBE uses special sensors to measure the
        temperature of the Earth's surface."
        hide sun_confused
        show solange at center
        solange "These sensors are much more precise and can be used on different types of terrain. Our experiment
        with the glasses is just a simple way of understanding the basic concept of how different surfaces
        absorb and retain heat differently."

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
        hide solange
        show sun_thermo at right
        menu:
            solange "Which of the three glasses is the hottest??"
            "The one in the table":
                $ renpy.play("audio/sucess.mp3", channel="sound")
                $ score += 1
                hide sun_thermo
                show solange_h at center
                solange "That's right! The wooden table retains more heat and transfers it to the glass more
                than the others."
            "The one in the cup holder":
                $ renpy.play("audio/ERROU.mp3", channel="sound")
                show layer master at scream_shake
                solange "Try again! The cup holder, despite having received heat from the sun, is an excellent
                thermal insulator. It heats up, but doesn't transfer heat efficiently to the cup like the
                wooden table, keeping the bottom of the cup relatively insulated."
                jump .quiz1
            "The other one on the table, but which has a metallic sound when it's been placed":
                $ renpy.play("audio/ERROU.mp3", channel="sound")
                show layer master at scream_shake
                solange "Almost! This glass have a aluminum foil under him. Even though aluminum
                is a good conductor, its reflective surface means that it absorbs less heat from
                direct sunlight, which means that the first glass directly on the wooden table heats
                up more quickly than this glass on the aluminum foil."
                jump .quiz1

    label .quiz2:
        $ questions -= 1
        hide solange_h
        show sun_confused at right
        solange "Now let's see if you understand the different surface temperatures."
        menu:
            solange "Three surfaces are exposed to direct sunlight for 30 minutes: one of asphalt, one of grass and one of sand.
                    Which surface will get hotter?"
            "Sand":
                $ renpy.play("audio/ERROU.mp3", channel="sound")
                show layer master at scream_shake
                solange "Wrong! Sand also gets very hot, but not as hot as asphalt."
                player "But I also burn my feet when I go to the beach and step on the sand!"
                solange "Sand is usually lighter in color than asphalt, so it absorbs less heat because it reflects more sunlight than asphalt."
                solange "Sand also loses heat more quickly and is less dense than asphalt."
                jump .quiz2
            "Grass":
                $ renpy.play("audio/ERROU.mp3", channel="sound")
                show layer master at scream_shake
                solange "Incorrect! Grass absorbs less heat and also cools down due to moisture evaporation."
                jump .quiz2
            "Asphalt":
                $ renpy.play("audio/sucess.mp3", channel="sound")
                hide sun_confused
                show solange_h at center
                $ score += 1
                solange "That's right! Asphalt tends to be warmer in this scenario due to its dark color and low capacity to reflect solar radiation."

    label .quiz3:
        $ questions -= 1
        hide solange_h
        show sun_confused at right
        solange "Imagine that you have a sheet of white paper and a metal plate placed side by side in bright sunlight."
        menu:
            solange "After 20 minutes, which one will show the greatest change in temperature compared to the initial environment?"
            "Metal plate":
                $ renpy.play("audio/ERROU.mp3", channel="sound")
                show layer master at scream_shake
                solange "Wanna try put your hand at a metal plate after getting sunlight for 20 minutes?"
                player "Ehh...better not!!"
                jump .quiz3
            "Sheet of white paper":
                $ renpy.play("audio/sucess.mp3", channel="sound")
                hide sun_confused
                show solange_h at center
                $ score += 1
                solange "You are right again! White is the color that reflects almost all frequencies of visible light, making it highly reflective."
                solange "While the metal plate also reflects visible light, it absorbs a lot of infrared radiation (which is the non-visible portion
                that carries heat), resulting in a greater temperature variation!"
    hide solange_h
    show solange at center
    solange "Well, I enjoyed meeting you, but now I have to finish my project, I hope we can meet again! Bye bye!"
    
    jump start
