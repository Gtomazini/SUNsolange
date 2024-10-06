  # Declarações de imagens
image cirrus_cloud = "images/chapter2/cirrus_cloud.jpg"
image altocumulus_cloud = "images/chapter2/altocumulus_cloud.jpg"
image stratus_cloud = "images/chapter2/stratus_cloud.jpg"
label game2:


    $ score = 0
    $ questions = 3

    "Bem-vindo ao Quiz de Nuvens! Vamos testar seu conhecimento sobre tipos de nuvens."

    label .question1:
        $ questions -= 1
        show cirrus_cloud at truecenter
        menu:
            "Que tipo de nuvem é esta?"
            "Cirrus":
                $ score += 1
                "Correto! Estas são nuvens Cirrus."
            "Altocumulus":
                "Incorreto. Estas são nuvens Cirrus. Vamos tentar novamente."
                jump .question1
            "Stratus":
                "Incorreto. Estas são nuvens Cirrus. Vamos tentar novamente."
                jump .question1

    label .question2:
        $ questions -= 1
        show altocumulus_cloud at truecenter
        menu:
            "Que tipo de nuvem é esta?"
            "Cirrus":
                "Incorreto. Estas são nuvens Altocumulus. Vamos tentar novamente."
                jump .question2
            "Altocumulus":
                $ score += 1
                "Correto! Estas são nuvens Altocumulus."
            "Stratus":
                "Incorreto. Estas são nuvens Altocumulus. Vamos tentar novamente."
                jump .question2

    label .question3:
        $ questions -= 1
        show stratus_cloud at truecenter
        menu:
            "Que tipo de nuvem é esta?"
            "Cirrus":
                "Incorreto. Estas são nuvens Stratus. Vamos tentar novamente."
                jump .question3
            "Altocumulus":
                "Incorreto. Estas são nuvens Stratus. Vamos tentar novamente."
                jump .question3
            "Stratus":
                $ score += 1
                "Correto! Estas são nuvens Stratus."

    "Parabéns! Você completou o Quiz de Nuvens. Sua pontuação final é [score] de 3."

    return