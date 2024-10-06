# Back ground image
image background_escola = "images/chapter2/campus.png"

# name of the character.

define solange = Character("Solange")

# The chapter starts here.

label chapter2:
# Background scene
    scene background_escola
# Scream shake
    show layer master at scream_shake
# Falling sound
    "CRAMB CRAMB TCHUMM"
    player "What was that?!"
# Image of the fallen veteran
# Colocar imagem aqui
    player "'What's she doing?'"
    player "Hey..."    
# Image of the frightened veteran 
# Colocar imagem aqui
# Scream shake
    show layer master at scream_shake
    solange "YAHAH!!!!"
    player "??????????"
    solange "BREATHE...BREATHE...BREATHE..."
    player "Hmmm... Are yo-"
    solange "Yes, I'm fine, thank you!"
    menu:      
        "See you later!":
            call path1     
        
        "I see you're well, what are you doing?":
            call path2 
    return

label path1:
    solange "Wait, I need your help!"
    menu:       
        "Of course, what do you need?":
            call    path101
        "I don't know, what do you have in mind?":
            call    path102
    return

label path101:
    solange "Great that you asked! The GLOBE Protocol is a global program that connects ordinary people 
            with scientists to study our planet. Basically, you learn how to collect local environmental data
            in a standardized way."
    solange "This data, such as air temperature or water quality, is shared online and used by scientists 
            to understand global environmental changes. It's like a worldwide jigsaw puzzle where each person 
            contributes a piece."
    solange "The best thing is that anyone can take part, not just professional scientists. You learn about
            the environment, develop scientific skills and contribute to important research. 
            How about becoming a citizen scientist and taking part?"
    call    path3
    return

label path102:
    $ pause_time = 1.5
    solange "Oh, good of you to ask! The GLOBE Protocol is something fascinating that brings together science,
            education and global environmental action.{w=[pause_time]}{nw}"
    solange "Imagine a worldwide network of ordinary people like you and me, working together with scientists 
            to better understand our planet.{w=[pause_time]}{nw}"
    solange "Basically, GLOBE teaches people how to collect scientific data about their local environment - 
            things like air temperature, cloud types, water quality or biodiversity.{w=[pause_time]}{nw}" 
    solange "This data is collected using standardized methods, which means it can be compared and analyzed 
            globally.{w=[pause_time]}{nw}" 
    solange "The cool thing is that you don't have to be a professional scientist to take part. Students, 
            teachers, enthusiasts... everyone can contribute!{w=[pause_time]}{nw}" 
    solange "This data collected by people all over the world is then shared on an online platform. 
            Scientists use this information to better understand global environmental changes.{w=[pause_time]}{nw}" 
    solange "It's like each participant is a piece of a big global puzzle, helping to build a clearer 
            picture of the health of our planet.{w=[pause_time]}{nw}" 
    solange "As well as contributing to science, taking part in GLOBE is also a great way to learn about 
            the environment and develop practical scientific skills.{w=[pause_time]}{nw}"
    solange "So, what do you think? Would you like to be a citizen scientist and be part of this global 
            network of environmental observers?{w=[pause_time]}{nw}"  

    menu:
        "Yes":
            return
        "Of course":
            return
        "Why do you only have the option to agree???":      
            return

    call game2
            
label path2:
    solange "Hmm... I see you have a scientific mind, point for you"
    solange "I'm actually working on the GLOBE Protocol. It's a fascinating program that brings ordinary 
            people and scientists together to study our planet. You collect local environmental data in a 
            standardized way, which is then used in global research."
    solange "Imagine contributing to science by measuring things like air temperature or water quality in 
            your region. This data helps to understand environmental changes around the world. 
            It's like being part of a global team of citizen scientists!"
    solange "The best thing is that anyone can take part, learn about the environment and make a real 
            difference. Interested in joining this global network of environmental observers?"
    call    path3
    return

label path3:
    player "So what do we do?"
    solange "Let's learn about an essential factor in GLOBE Protocol readings, atmospheric data!"

    # Precisa fazer um menu de perguntas que volta ao mesmo menu depois da pergunta e as opções já perguntadas aparecem como marcadas
    # O QUE FALTA - LINKAR IMAGENS DAS NUVENS DO GAME2 COM NUVENS DO GLOBE IMAGES DA NASA
    # COLOCAR OS SONS DE ACERTO E ERRO

    menu:
        "Sure, that would be nice!":
            solange "Come closer my young paduan"
            call game2
        "That's fine, but I don't know much about it":
            solange "Great, let's learn then!"
            call game2
        "I don't know...":      
            solange "Come on, knowledge never hurts"
            call game2

        

        