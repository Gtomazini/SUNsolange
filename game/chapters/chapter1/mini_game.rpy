label mini_game_start:
    menu:
        "Yes, let's get started!":
            jump start_ph_test
        "No, maybe later.":
            "Okay, see you next time!"
            jump return_label  # Volta para o ponto anterior

# Classe Python que gerencia os três testes
init python:
    class EnvGame:
        def __init__(self):
            self.score = 0  # Pontuação inicial

        # Teste de pH
        def check_ph(self, guess):
            target_pH = 7  # pH médio do rio
            if target_pH == 7:
                correct_answer = "neutral"
            elif target_pH < 7:
                correct_answer = "acid"
            else:
                correct_answer = "alkaline"

            if guess == correct_answer:
                self.score += 10
                return "Correct! The pH was {}".format(correct_answer.capitalize())
            else:
                self.score -= 5
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
                return "Correct! The water temperature was {}ºC.".format(target_temp)
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
    scene background_river with fade
    show sol_test_ph at right
    $ feedback = "Choose an option:"
    $ correct_answer = False
    while not correct_answer:
        "Let's measure the pH of the water."
        call screen ph_game
        $ result = _return
        "[result]"
        if "Correct" in result:
            $ correct_answer = True
    hide sol_test_ph
    "You've completed the pH test correctly!"
    jump start_temp_test

# Teste 2: Verificação da Temperatura da Água
label start_temp_test:
    scene background_river
    show sol_test_temp at right
    $ feedback = "Choose an option:"
    $ correct_answer = False
    while not correct_answer:
        "Now let's check the water temperature."
        call screen temp_game
        $ result = _return
        "[result]"
        if "Correct" in result:
            $ correct_answer = True
    hide sol_test_temp
    "You've completed the temperature test correctly!"
    jump start_oxygen_test

# Teste 3: Verificação de Oxigênio Dissolvido na Água
label start_oxygen_test:
    scene background_river
    show sol_test_o2 at right
    $ feedback = "Choose an option:"
    $ correct_answer = False
    while not correct_answer:
        "Finally, let's check the level of dissolved oxygen in the water."
        call screen oxygen_game
        $ result = _return
        "[result]"
        if "Correct" in result:
            $ correct_answer = True
    hide sol_test_o2
    "You've completed the oxygen test correctly!"
    jump final_score  # Muda para a tela de pontuação

# Tela de pontuação final
label final_score:
    "Congratulations! You have completed the three environmental tests."
    "Your final score was: [game.score]"
    jump return_label  # Retorna ao ponto de onde o mini-jogo foi chamado

# Telas para os testes
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
            text "Choose whether the pH of the water is acidic, neutral or alkaline. Using the test carried out by Aunt Sol and held in your hand" size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Acid is 🔴 , Neutral is 🟢 , Alkaline is 🟣" size 30 outlines [(2, "#000", 0, 0)] xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Acid" action Return(game.check_ph("acid")):
                    text_size 40
                    text_color "#FF0000"
                    text_outlines [(2, "#000000", 0, 0)]
                textbutton "Neutral" action Return(game.check_ph("neutral")):
                    text_size 40
                    text_color "#04a119"
                    text_outlines [(2, "#000000", 0, 0)]
                textbutton "Alkaline" action Return(game.check_ph("alkaline")):
                    text_size 40
                    text_color "#6d0370"
                    text_outlines [(2, "#000000", 0, 0)]

            text "[feedback]" size 20 xalign 0.5

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
            text "Choose whether the water temperature is Cold, Moderate or Warm by looking at the measurement that you and Auntie Sol made." size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "COLD: Below 15°C   WARM: Between 15°C and 30°C   HOT: Above 30°C" size 30 outlines [(2, "#000", 0, 0)] xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Cold" action Return(game.check_temperature("Cold")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]
                textbutton "Moderate" action Return(game.check_temperature("Moderate")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]
                textbutton "Hot" action Return(game.check_temperature("Hot")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]

            text "[feedback]" size 20 xalign 0.5

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

            text "Oxygen Test" size 50 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Choose whether the oxygen level is Low, Moderate or High. looking at the measurement you and auntie sol made" size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "LOW: Less than 4 mg/L     MODERATE: Between 4 mg/L and 8 mg/L     HIGH: More than 8 mg/L" size 30 outlines [(2, "#000", 0, 0)] xalign 0.5


            hbox:
                xalign 0.5
                spacing 10
                textbutton "Low" action Return(game.check_oxygen("Low")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]
                textbutton "Moderate" action Return(game.check_oxygen("Moderate")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]
                textbutton "High" action Return(game.check_oxygen("High")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]

            text "[feedback]" size 20 xalign 0.5
