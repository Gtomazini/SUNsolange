# O jogo começa aqui.
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
    import random

    class EnvGame:
        def __init__(self):
            self.score = 0  # Pontuação inicial

        # Teste de pH
        def check_ph(self, guess):
            target_pH = 6.8  # pH médio do rio Lambari
            if target_pH < 7:
                correct_answer = "acid"
            elif target_pH == 7:
                correct_answer = "neutral"
            else:
                correct_answer = "alkaline"

            if guess == correct_answer:
                self.score += 1
                return "Correto! O pH era {}. Você acertou!".format(correct_answer.capitalize())
            else:
                return "Errado! Tente novamente."

        # Teste de temperatura
        def check_temperature(self, guess):
            target_temp = 26.4  # Temperatura média do rio Lambari
            if target_temp < 15:
                correct_answer = "fria"
            elif 15 <= target_temp <= 30:
                correct_answer = "moderada"
            else:
                correct_answer = "quente"

            if guess == correct_answer:
                self.score += 1
                return "Correto! A temperatura da água era {}ºC. Você acertou!".format(target_temp)
            else:
                return "Errado! Tente novamente."

        # Teste de oxigênio
        def check_oxygen(self, guess):
            target_oxygen = 7.5  # Nível médio de oxigênio no rio Lambari
            if target_oxygen < 4:
                correct_answer = "baixo"
            elif 4 <= target_oxygen <= 8:
                correct_answer = "moderado"
            else:
                correct_answer = "alto"

            if guess == correct_answer:
                self.score += 1
                return "Correto! O nível de oxigênio era {} mg/L. Você acertou!".format(target_oxygen)
            else:
                return "Errado! Tente novamente."

# Instância do jogo criada uma vez
default game = EnvGame()

# Teste 1: Medição de pH da água
label start_ph_test:
    $ feedback = "Escolha uma opção:"
    $ correct_answer = False
    while not correct_answer:
        scene background_river  # Adicione o background
        show sol_test_ph  # Mostra a personagem Sol
        "Vamos medir o pH da água."
        call screen ph_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correto" in result:
            $ correct_answer = True
    "Você concluiu o teste de pH corretamente!"
    jump start_temp_test  # Passa para o teste de temperatura

# Teste 2: Verificação da Temperatura da Água
label start_temp_test:
    $ feedback = "Escolha uma opção:"
    $ correct_answer = False
    while not correct_answer:
        scene background_river  # Adicione o background
        show sol_test_temp  # Mostra a personagem correspondente
        "Agora vamos verificar a temperatura da água."
        call screen temp_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correto" in result:
            $ correct_answer = True
    "Você concluiu o teste de temperatura corretamente!"
    jump start_oxygen_test  # Passa para o teste de oxigênio

# Teste 3: Verificação de Oxigênio Dissolvido na Água
label start_oxygen_test:
    $ feedback = "Escolha uma opção:"
    $ correct_answer = False
    while not correct_answer:
        scene background_river  # Adicione o background
        show sol_test_oxygen  # Mostra a personagem correspondente
        "Por fim, vamos verificar o nível de oxigênio dissolvido na água."
        call screen oxygen_game
        $ result = _return
        "[result]"  # Mostra o feedback do resultado
        if "Correto" in result:
            $ correct_answer = True
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
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "Teste de pH" size 30 xalign 0.5
            text "Escolha se o pH da água é ácido, neutro ou alcalino."
            
            # Exibir as cores correspondentes
            text "Ácido: Vermelho, Neutro: Verde, Alcalino: Roxo." size 20 xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Ácido" action Return(game.check_ph("acid"))
                textbutton "Neutro" action Return(game.check_ph("neutral"))
                textbutton "Alcalino" action Return(game.check_ph("alkaline"))

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5

# Tela do teste de temperatura
screen temp_game:
    frame:
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "Teste de Temperatura" size 30 xalign 0.5
            text "Escolha se a temperatura da água é fria, moderada ou quente."
            
            # Exibir as cores correspondentes
            text "Fria: Azul, Moderada: Verde, Quente: Vermelho." size 20 xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Fria" action Return(game.check_temperature("fria"))
                textbutton "Moderada" action Return(game.check_temperature("moderada"))
                textbutton "Quente" action Return(game.check_temperature("quente"))

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5

# Tela do teste de oxigênio dissolvido
screen oxygen_game:
    frame:
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "Teste de Oxigênio Dissolvido" size 30 xalign 0.5
            text "Escolha se o nível de oxigênio na água é baixo, moderado ou alto."
            
            # Exibir as cores correspondentes
            text "Baixo: Vermelho, Moderado: Verde, Alto: Azul." size 20 xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                textbutton "Baixo" action Return(game.check_oxygen("baixo"))
                textbutton "Moderado" action Return(game.check_oxygen("moderado"))
                textbutton "Alto" action Return(game.check_oxygen("alto"))

            # Mensagem de feedback
            text "[feedback]" size 20 xalign 0.5
