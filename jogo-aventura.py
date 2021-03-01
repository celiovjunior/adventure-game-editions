import time

def slow_step(msg):
    print(msg)
    time.sleep(2)

def newtry():
    print("Comando inválido. Termiando...")

def end_game():
    print("Fim de jogo!")

print("COMO JOGAR")
print("-- Aperte apenas os comandos válidos;")
print("-- Você decide o que acontece com o personagem através de suas escolhas")
print("-- Caso escolha um comando inválido, o jogo termina.")

slow_step("\nO JOGO VAI COMEÇAR..." )

slow_step("\nVocê está em casa, observando sua mãe cozinhar...")
slow_step("Até que ela tira do armário um cesto cheio de pães...")
slow_step("Ela pede para você deixar o cesto até a casa de sua Vó...")
slow_step("A casa da Vovó é um pouco longe e você está cansado...")
answer1 = input("Você quer ir até lá? (sim/nao)")

if answer1 == "sim":
    slow_step("Mesmo cansado, você decide ir...")
    slow_step("Você veste seu moletom vermelho e segue até a casa da vovó...")
    slow_step("Mas você não quer demorar muito...")
    slow_step("Pode ser pelo bosque, que é mais escuro e fechado, porém vai andar menos...")
    slow_step("Ou pela estrada, mais aberta e movimentada, mas vai andar mais...")

    answer1 = input("Por onde você vai? (bosque/estrada)")
    
    if answer1 == "bosque":
        slow_step("Você vai pelo bosque...")
        slow_step("Depois de andar um pouco, você tropeça em algo entre as folhas...")

        answer1 = input("Você quer ver em que você tropeçou ou seguir? (ver / seguir)")
        if answer1 == "ver":
                slow_step("Você volta alguns passos para ver em o que tropeçou...")
                slow_step("Você cava as folhas e percebe um mal cheiro subindo...")
                slow_step("Entre as folhas está um crânio!")
                slow_step("Você se assusta e fica sem saber o que fazer...")
                answer1 = input("Voltar para a estrada (v) ou seguir em frente(f)?")

                if answer1 == "v":
                    slow_step("Você fica com medo e dá meia volta...")
                    slow_step("Chegando na estrada, há um alguel de bicicletas")
                    slow_step("Você pega aluga uma e segue em segurança até a casa da Vovó")
                    end_game()

                elif answer1 == "f":
                    slow_step("Você analisa melhor o crânio...")
                    slow_step("E conclui que pode ser de algum animal morto...")
                    slow_step("Você pega um pedaço de madeira caso seja atacado...")
                    slow_step("E decide seguir...")
                    
                else:
                    newtry()
        else:
                slow_step("Você decide seguir, apressando os passos")
                slow_step("")

    
    else:
        slow_step("Você resolve pegar a estrada...")
        slow_step("Há um aglomerado de pessoas a poucos metros...")
        slow_step("Você não quer se atrasar mas fica curioso...")

        answer1 = input("Ignorar (ignorar) ou descobrir(descobrir) o que está acontecendo?")

elif answer1 == "nao":
    slow_step("Você está com preguiça demais para fazer esse favor...")
    slow_step("GAME OVER")

else:
    newtry()
