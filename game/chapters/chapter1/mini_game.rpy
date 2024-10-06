
label mini_game_start:


    menu:
        "Yes, let's get started!":
            jump start_ph_test
        "No, maybe later.":
            "Okay, see you next time!"
            return

# Classe Python que gerencia os três testes
init python:
    class EnvGame:
        def __init__(self):
            self.score = 0  # Pontuação inicial

        # Teste de pH
        def check_ph(self, guess):
            target_pH = 7  # pH médio do rio
            if target_pH < 3:
                correct_answer = "acid"
            elif 4 <= target_pH <= 7:
                correct_answer = "neutral"
            else:
                correct_answer = "alkaline"

            if guess == correct_answer:
                self.score += 10
                return "Correct! The pH was {}".format(correct_answer.capitalize())
            else:
                self.score -5
                return "Wrong! Try again."

        # Teste de temperatura
        def check_temperature(self, guess):
            target_temp = 24  # Temperatura média do rio
            if target_temp < 15:
                correct_answer = "Cold"
            elif 15 <= target_temp <= 30:
                correct_answer = "Moderate"
            else:
                correct_answer = "Hot"
            if guess == correct_answer:
                self.score += 10
                return "That's right! The water temperature was {}ºC".format(target_temp)
            else:
                
                return "Wrong! Try again."

        # Teste de oxigênio
        def check_oxygen(self, guess):
            target_oxygen = 5  # Nível médio de oxigênio no rio
            if target_oxygen < 4:
                correct_answer = "Low"
            elif 4 <= target_oxygen <= 8:
                correct_answer = "Moderate"
            else:
                correct_answer = "High"

            if guess == correct_answer:
                self.score += 10
                return "Correct! The oxygen level was {} mg/L.".format(target_oxygen)
            else:
                
                return "Wrong! Try again."

# Instância do jogo criada uma vez
default game = EnvGame()

# Teste 1: Medição de pH da água
label start_ph_test:
    scene background_river with fade  # Define o background para o teste de pH
    show sol_test_ph at right  # Mostra a personagem Sol à direita
    $ feedback = "Choose an option:"
    $ correct_answer = False
    while not correct_answer:
        "Let's measure the pH of the water."
        
        # Adicionando a legenda para o teste de p

        call screen ph_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correct" in result:
            $ correct_answer = True
    hide sol_test_ph  # Esconde a personagem após o teste
    "You've completed the pH test correctly!"
    jump start_temp_test  # Passa para o teste de temperatura

# Teste 2: Verificação da Temperatura da Água
label start_temp_test:
    scene background_river  # Define o background para o teste de temperatura
    show sol_test_temp at right  # Mostra a personagem Sol à direita
    $ feedback = "Choose an option:"
    $ correct_answer = False
    while not correct_answer:
        "Now let's check the water temperature."
        call screen temp_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        $ renpy.log(result)
        if "Correct" in result:
            $ correct_answer = True
    hide sol_test_temp  # Esconde a personagem após o teste
    "You've completed the temperature test correctly!"
    jump start_oxygen_test  # Passa para o teste de oxigênio

# Teste 3: Verificação de Oxigênio Dissolvido na Água
label start_oxygen_test:
    scene background_river  # Define o background para o teste de oxigênio
    show sol_test_o2 at right  # Mostra a personagem Sol à direita
    $ feedback = "Choose an option:"
    $ correct_answer = False
    while not correct_answer:
        "Finally, let's check the level of dissolved oxygen in the water."
        call screen oxygen_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correct" in result:
            $ correct_answer = True
    hide sol_test_o2  # Esconde a personagem após o teste
    "You've completed the oxygen test correctly!"
    jump final_score  # Finaliza os testes e exibe a pontuação

# Tela de pontuação final
label final_score:
    "Congratulations! You have completed the three environmental tests."
    "His final score was: [game.score]"
    return

# Telas para os testes

# Tela do teste de pH
screen ph_game:
    frame:
        add "background_river"
        add "sol_test_ph" at right
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "PH test" size 50 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Choose whether the pH of the water is acidic, neutral or alkaline according to the result in Sol's hand" size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            # Tabela de cores
            hbox:
                spacing 20
                vbox:
                    text "Red" size 30 color "#FF0000" outlines [(2, "#000", 0, 0)]
                    text "Acid" size 30 color "#FF0000" outlines [(2, "#000", 0, 0)]
                vbox:
                    text "Green" size 30 color "#04a119" outlines [(2, "#000", 0, 0)]
                    text "Neutral" size 30 color "#04a119" outlines [(2, "#000", 0, 0)]
                vbox:
                    text "Purple" size 30 color "#6d0370" outlines [(2, "#000", 0, 0)]
                    text "Alkaline" size 30 color "#6d0370" outlines [(2, "#000", 0, 0)]

            hbox:
                xalign 0.5
                spacing 10
                # Botão Ácido (personalizado diretamente)
                textbutton "Acid" action Return(game.check_ph("acid")):
                    text_size 40
                    text_color "#FF0000"  # Cor vermelha
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

                # Botão Neutro (personalizado diretamente)
                textbutton "Neutral" action Return(game.check_ph("neutral")):
                    text_size 40
                    text_color "#04a119"  # Cor verde
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

                # Botão Alcalino (personalizado diretamente)
                textbutton "Alkaline" action Return(game.check_ph("alkaline")):
                    text_size 40
                    text_color "#6d0370"  # Cor roxa
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5

# Tela do teste de temperatura
screen temp_game:
    frame:
        add "background_river"
        add "sol_test_temp" at right
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "Temperature test" size 50 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Choose whether the water temperature is Cold, Moderate or Hot." size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Cold" action Return(game.check_temperature("Cool")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

                textbutton "Moderate" action Return(game.check_temperature("Moderate")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto
                textbutton "Warm" action Return(game.check_temperature("Warm")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5

# Tela do teste de oxigênio dissolvido
screen oxygen_game:
    frame:
        add "background_river"
        add "sol_test_o2" at right
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "Dissolved Oxygen Test" size 50 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Choose whether the oxygen level in the water is low, moderate or high." size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Low" action Return(game.check_oxygen("Low")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto
                textbutton "Moderate" action Return(game.check_oxygen("Moderate")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto
                textbutton "High" action Return(game.check_oxygen("High")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5
