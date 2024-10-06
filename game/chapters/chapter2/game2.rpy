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
