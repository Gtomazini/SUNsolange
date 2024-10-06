  # Declarações de imagens
image cirrus_cloud = "images/chapter2/cirrus_cloud.jpg"
image altocumulus_cloud = "images/chapter2/altocumulus_cloud.jpg"
image stratus_cloud = "images/chapter2/stratus_cloud.jpg"

label game2:


    $ score = 0
    $ questions = 3

    "Welcome to the Cloud Quiz! Let's test your knowledge of cloud types."

    label .question1:
        $ questions -= 1
        show cirrus_cloud at truecenter
        menu:
            "What kind of cloud is it?"
            "Cirrus":
                $ score += 1
                "That's right! These are Cirrus clouds."
            "Altocumulus":
                "Incorrect. Let's try again."
                jump .question1
            "Stratus":
                "Incorrect. Let's try again."
                jump .question1

    label .question2:
        $ questions -= 1
        show altocumulus_cloud at truecenter
        menu:
            "How about that?"
            "Cirrus":
                "Incorrect. Let's try again."
                jump .question2
            "Altocumulus":
                $ score += 1
                "That's right! These are Altocumulus clouds."
            "Stratus":
                "Incorrect. Let's try again."
                jump .question2

    label .question3:
        $ questions -= 1
        show stratus_cloud at truecenter
        menu:
            "The final question! What kind of cloud is it?"
            "Cirrus":
                "Incorrect. Let's try again."
                jump .question3
            "Altocumulus":
                "Incorrect. Let's try again."
                jump .question3
            "Stratus":
                $ score += 1
                "That's right! These are Stratus clouds."

    "Congratulations! You have completed the Cloud Quiz. Your final score is [score] out of 3."


# precisa retornar pro script do chapter 2 e terminar o dialogo
    return