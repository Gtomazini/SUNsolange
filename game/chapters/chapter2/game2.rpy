# Images
image cirrus_cloud = "images/chapter2/cirrus_cloud.jpg"
image altocumulus_cloud = "images/chapter2/altocumulus_cloud.jpg"
image stratus_cloud = "images/chapter2/stratus_cloud.jpg"

label game2:
    "Welcome to the Cloud Quiz! Let's test your knowledge of cloud types."
    
    call .question

    "Congratulations! You have completed the Cloud Quiz!"
    
    "Remember! Identification will not always be simple, our friend the sun can have an impact 
    on the development of formats, this happens up there for those who see from the satellites too."

    return

label .question:
    $ finish = False
    $ question = 1
    while not finish:
        if question == 1:
            call .question1
        if question == 2:
            call .question2
        if question == 3:
            call .question3
    return

label .question1:
    show cirrus_cloud at truecenter
    menu:
        "What kind of cloud is it?"
        "Cirrus":
            call .correct_answer
        "Altocumulus":
            call .wrong_answer
        "Stratus":
            call .wrong_answer
    return

      

label .question2:
    show altocumulus_cloud at truecenter
    menu:
        "How about that?"
        "Cirrus":
            call .wrong_answer
        "Altocumulus":
            call .correct_answer
        "Stratus":
            call .wrong_answer
    return


label .question3:
    show stratus_cloud at truecenter
    menu:
        "The final question! What kind of cloud is it?"
        "Cirrus":
            call .wrong_answer
        "Altocumulus":
            call .wrong_answer
        "Stratus":
            call .correct_answer
            $ finish = True
    return

label .wrong_answer:
    play sound "errou.mp3" volume 0.5
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
