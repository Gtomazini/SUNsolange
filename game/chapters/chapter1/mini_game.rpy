
label mini_game_start:
    "Bem-vindo ao jogo ambiental! Você precisa realizar 3 testes ambientais para garantir a qualidade da água."
    "Está pronto para começar?"

    menu:
        "Sim, vamos começar!":
            jump start_ph_test
        "Não, talvez mais tarde.":
            "Ok, até a próxima!"
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
                return "Correto! O pH era {}. Você acertou!".format(correct_answer.capitalize())
            else:
                self.score -5
                return "Errado! Tente novamente."

        # Teste de temperatura
        def check_temperature(self, guess):
            target_temp = 24  # Temperatura média do rio
            if target_temp < 15:
                correct_answer = "fria"
            elif 15 <= target_temp <= 30:
                correct_answer = "moderada"
            else:
                correct_answer = "quente"

            if guess == correct_answer:
                self.score += 10
                return "Correto! A temperatura da água era {}ºC. Você acertou!".format(target_temp)
            else:
                self.score -5
                return "Errado! Tente novamente."

        # Teste de oxigênio
        def check_oxygen(self, guess):
            target_oxygen = 5  # Nível médio de oxigênio no rio
            if target_oxygen < 4:
                correct_answer = "baixo"
            elif 4 <= target_oxygen <= 8:
                correct_answer = "moderado"
            else:
                correct_answer = "alto"

            if guess == correct_answer:
                self.score += 10
                return "Correto! O nível de oxigênio era {} mg/L. Você acertou!".format(target_oxygen)
            else:
                self.score -5
                return "Errado! Tente novamente."

# Instância do jogo criada uma vez
default game = EnvGame()

# Teste 1: Medição de pH da água
label start_ph_test:
    scene background_river with fade  # Define o background para o teste de pH
    show sol_test_ph at right  # Mostra a personagem Sol à direita
    $ feedback = "Escolha uma opção:"
    $ correct_answer = False
    while not correct_answer:
        "Vamos medir o pH da água."
        
        # Adicionando a legenda para o teste de p

        call screen ph_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correto" in result:
            $ correct_answer = True
    hide sol_test_ph  # Esconde a personagem após o teste
    "Você concluiu o teste de pH corretamente!"
    jump start_temp_test  # Passa para o teste de temperatura

# Teste 2: Verificação da Temperatura da Água
label start_temp_test:
    scene background_river  # Define o background para o teste de temperatura
    show sol_test_temp at right  # Mostra a personagem Sol à direita
    $ feedback = "Escolha uma opção:"
    $ correct_answer = False
    while not correct_answer:
        "Agora vamos verificar a temperatura da água."
        call screen temp_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correto" in result:
            $ correct_answer = True
    hide sol_test_temp  # Esconde a personagem após o teste
    "Você concluiu o teste de temperatura corretamente!"
    jump start_oxygen_test  # Passa para o teste de oxigênio

# Teste 3: Verificação de Oxigênio Dissolvido na Água
label start_oxygen_test:
    scene background_river  # Define o background para o teste de oxigênio
    show sol_test_o2 at right  # Mostra a personagem Sol à direita
    $ feedback = "Escolha uma opção:"
    $ correct_answer = False
    while not correct_answer:
        "Por fim, vamos verificar o nível de oxigênio dissolvido na água."
        call screen oxygen_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correto" in result:
            $ correct_answer = True
    hide sol_test_o2  # Esconde a personagem após o teste
    "Você concluiu o teste de oxigênio corretamente!"
    jump final_score  # Finaliza os testes e exibe a pontuação

# Tela de pontuação final
label final_score:
    "Parabéns! Você completou os três testes ambientais."
    "Sua pontuação final foi: [game.score]"
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

            hbox:
                xalign 0.5
                spacing 10
                # Botão Ácido (personalizado diretamente)
                textbutton "Ácido" action Return(game.check_ph("acid")):
                    text_size 40
                    text_color "#FF0000"  # Cor vermelha
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

                # Botão Neutro (personalizado diretamente)
                textbutton "Neutro" action Return(game.check_ph("neutral")):
                    text_size 40
                    text_color "#04a119"  # Cor verde
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

                # Botão Alcalino (personalizado diretamente)
                textbutton "Alcalino" action Return(game.check_ph("alkaline")):
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

            text "Teste de Temperatura" size 50 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Escolha se a temperatura da água é fria, moderada ou quente." size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Fria" action Return(game.check_temperature("fria")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

                textbutton "Moderada" action Return(game.check_temperature("moderada")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto
                textbutton "Quente" action Return(game.check_temperature("quente")):
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

            text "Teste de Oxigênio Dissolvido" size 50 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5
            text "Escolha se o nível de oxigênio na água é baixo, moderado ou alto." size 45 color "#ffffff" outlines [(2, "#000", 0, 0)] xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Baixo" action Return(game.check_oxygen("baixo")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto
                textbutton "Moderado" action Return(game.check_oxygen("moderado")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto
                textbutton "Alto" action Return(game.check_oxygen("alto")):
                    text_size 40
                    text_outlines [(2, "#000000", 0, 0)]  # Contorno preto

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5
