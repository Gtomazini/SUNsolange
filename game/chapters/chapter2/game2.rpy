# Images
image cirrus_cloud = "images/chapter2/cirrus_cloud.jpg"
image altocumulus_cloud = "images/chapter2/altocumulus_cloud.jpg"
image stratus_cloud = "images/chapter2/stratus_cloud.jpg"
image instruction_cloud = "images/chapter2/cloud_chart.png"
label game2:
    "Welcome to the Cloud Quiz! Let's test your knowledge of cloud types."

    call .instructions
    
    call .question

    "Congratulations! You have completed the Cloud Quiz!"
    
    "Remember! Identification will not always be simple, our friend the sun can have an impact 
    on the development of formats, this happens up there for those who see from the satellites too."

    return

label .question:
    call .question1
    call .question2
    call .question3 
    return

label .question1:
    show cirrus_cloud at truecenter
    menu:
        "What kind of cloud is it?"
        "Cirrus":
            "That's right! These are Cirrus clouds."
        "Altocumulus":
            jump .wrong_answer1
        "Stratus":
            jump .wrong_answer1
    return

label .wrong_answer1:
    "Incorrect. Let's try again."
    jump .question1        

label .question2:
    show altocumulus_cloud at truecenter
    menu:
        "How about that?"
        "Cirrus":
            jump .wrong_answer2
        "Altocumulus":
            "That's right! These are Altocumulus clouds."
        "Stratus":
            jump .wrong_answer2
    return

label .wrong_answer2:
    "Incorrect. Let's try again."
    jump .question2     

label .question3:
    show stratus_cloud at truecenter
    menu:
        "The final question! What kind of cloud is it?"
        "Cirrus":
            jump .wrong_answer3
        "Altocumulus":
            jump .wrong_answer3
        "Stratus":
            "That's right! These are Stratus clouds."
    return

label .wrong_answer3:
    "Incorrect. Let's try again."
    return

label .correct_answer:
    play sound "sucess.mp3" volume 0.5
    if question == 1:
        "That's right! These are Cirrus clouds."
    if question == 2:
        "That's right! These are Altocumulus clouds."
    if question == 3:
        "That's right! These are Stratus clouds."
    $ question += 1

label .instructions:

    show sol_default at center
    

    solange "Let's start with some explanations"

    solange "Regardless of the area you're interested in in the GLOBE program, observation is one of the key points"

    hide sol_default

    show instruction_cloud at truecenter:
        zoom 0.5   

    solange "So to illustrate, let's use an image like this one:"



    solange "It can be found in the cloud types section in Globe Program observability"

    solange "take a closer look"

    #aqui precisa remover a barra de dialogo por uma ação de click pelo menos

        # Remove a barra de diálogo
    window hide

    # Pausa até que o jogador clique
    pause

    # Mostra a barra de diálogo novamente
    window show

    solange "Observing clouds is not an exact assessment due to various factors."

    solange "There are several classifications, but for practical purposes we'll summarize a few"

    solange "Let's start with Cirrus. Like the top of the pyramid, it's one of the highest, so it tends to be very thin."

    solange "Now let's take a medium height one, like Altocumulus, which is known for tending to have a shape."

    solange "And finally, a lower one, the Stratus is known for being uniform and looking like a fog."

    solange "Now let's reinforce this explanation with a game."


    return
