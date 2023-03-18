def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavraSecreta = "banana"
    letrasAcertadas = ["_", "_","_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Tente uma letra")
        chute = chute.strip()

        index = 0
        for letra in palavraSecreta:
            if(chute.upper() == letra.upper()):
                letrasAcertadas[index] = letra
            index = index + 1

        print(letrasAcertadas)

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
