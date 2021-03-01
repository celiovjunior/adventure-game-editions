import time
import random

def slow_step(msg):
    print(msg)
    time.sleep(2)

def newtry():
    print("Comando inválido. Termiando...")

def end_game():
    print("Fim de jogo!")

food = random.choice(["doces", "pães", "frutas"])
weapon = random.choice(["madeira", "tijolo", "rocha"])
animal = random.choice(["lobo", "cervo", "urso"])


    

print("COMO JOGAR")
print("-- Aperte apenas os comandos válidos;")
print("-- Você decide o que acontece com o personagem através de suas escolhas")
print("-- Caso escolha um comando inválido, o jogo termina.")

slow_step("\nO JOGO VAI COMEÇAR..." )

slow_step("\nVocê está em casa, observando sua mãe cozinhar...")
slow_step("Até que ela tira do armário um cesto cheio de " + food + "...")
slow_step("Ela pede para você deixar o cesto até a casa de sua Vó...")
slow_step("A casa da Vovó é um pouco longe e você está cansado...")

answer = input("Você quer ir até lá? (sim/nao)")

if answer == "sim":
    slow_step("Mesmo cansado, você decide ir...")
    slow_step("Você veste seu moletom vermelho e segue até a casa da vovó...")
    slow_step("Mas você não quer demorar muito...")
    slow_step("Pode ser pelo bosque, que é mais escuro e fechado, porém vai andar menos...")
    slow_step("Ou pela estrada, mais aberta e movimentada, mas vai andar mais...")

    answer = input("Por onde você vai? (bosque/estrada)")
    
    if answer == "bosque":
        slow_step("Você vai pelo bosque...")
        slow_step("Depois de andar um pouco, você tropeça em algo entre as folhas...")

        answer = input("Você quer ver em que você tropeçou ou seguir? (ver / seguir)")
        if answer == "ver":
                slow_step("Você volta alguns passos para ver em o que tropeçou...")
                slow_step("Você cava as folhas e percebe um mal cheiro subindo...")
                slow_step("Entre as folhas está um crânio!")
                slow_step("Você se assusta e fica sem saber o que fazer...")
                answer = input("Voltar para a estrada (e) ou seguir em frente(f)?")
                
                if answer == "e":
                   slow_step("Você fica com medo e dá meia volta...")
                   slow_step("Chegando na estrada, há um alguel de bicicletas")
                   slow_step("Você pega aluga uma e segue em segurança até a casa da Vovó")
                   end_game()
                elif answer == "f":
                        slow_step("Você analisa melhor o crânio...")
                        slow_step("E conclui que pode ser de algum animal morto...")
                        slow_step("Você pega um pedaço de " + food + " caso seja atacado...")
                        slow_step("E decide seguir...")
                
        else:
                slow_step("Você decide seguir, apressando os passos")
                slow_step("No meio do caminho, você sente um cheiro de queimado...")
                slow_step("Está acontecendo uma queima no bosque!")
                answer = input("Você deve ligar para os bombeiros (b) ou seguir pelo atalho(a)?")
                if answer == "b":
                    slow_step("Você resolve ligar com urgencia para os bombeiros!")
                    slow_step("Você se afasta daquela região do bosque...")
                    slow_step("E rapidamente os bombeiros chegam.")
                    slow_step("Uma outra viatura chega para lhe dar carona até a casa da Vovó...")
                    slow_step("Você a entrega o cesto e passam a tarde juntos, por segurança.")
                    end_game()
                else:
                    slow_step("Você corre rapidamente por um atalho...")
                    slow_step("Mas o caminho escolhido está tomado pelo fogo da queimada!")
                    slow_step("Rapidamente você se perde no meio da floresta...")
                    slow_step("A fumaça lhe sufoca...")
                    end_game()
    else:
        slow_step("Você resolve pegar a estrada...")
        slow_step("Há um aglomerado de pessoas a poucos metros...")
        slow_step("Você não quer se atrasar mas fica curioso...")

        answer = input("Ignorar (i) ou descobrir(d) o que está acontecendo?")

        if answer == "d":
            slow_step("Você se aproxima das pessoas...")
            slow_step("Aconteceu um acidente de trânsito...")
            slow_step("Um motorista inexperiente atropela um" + animal + " sem querer...")
            slow_step("Você fica assustado, pois não imaginava que houvesse lobos na região.")
            slow_step("Para chegar mais rápido, você decide alugar uma bicicleta...")
            slow_step("Rapidamente você chega na casa da Vovó e passam a tarde juntos.")
            end_game()
            
        else:
            slow_step("Apesar da curiosidade, você quer logo entregar o cesto...")
            slow_step("Você tenta dar uma espiada por cima, mas segue até o aluguel de bicicletas...")
            slow_step("Rapidamente você chega na casa da Vovó e lhe entrega o cesto.")
            end_game()

elif answer == "nao":
    slow_step("Você está com preguiça demais para fazer esse favor...")
    slow_step("GAME OVER")

else:
    newtry()
