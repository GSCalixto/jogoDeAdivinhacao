import random

def jogar():
    imprimeApresentação()

    numeroSecreto = random.randrange(1, 101)
    totalDeTentativas = 0
    pontos = 10000

    escolheNivel(totalDeTentativas)

    for rodada in range(1, totalDeTentativas + 1):
        print("Tentativa {} de {}".format(rodada, totalDeTentativas))
        chuteStr = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chuteStr)
        chute = int(chuteStr)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numeroSecreto
        maior   = chute > numeroSecreto
        menor   = chute < numeroSecreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            #calculo de pontos com numeros absolutos
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

    print("Fim do jogo")

def imprimeApresentação():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def escolheNivel(totalDeTentativas):
    print("Qual é o nível de dificuldade desejado?")
    print("(1) para fácil \n(2) para médio \n(3) para difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        totalDeTentativas = 20
    elif (nivel == 2):
        totalDeTentativas = 10
    else:
        totalDeTentativas = 5

if(__name__ == "__main__"):
    jogar()