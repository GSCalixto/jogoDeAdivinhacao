import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero]
    
    letrasAcertadas = ["_" for letra in palavraSecreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Tente uma letra")
        chute = chute.strip().upper()

        if(chute in palavraSecreta):
            index = 0
            for letra in palavraSecreta:
                if(chute == letra):
                    letrasAcertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
