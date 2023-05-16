import random

def jogar():
    exibeMensagemInicio()
    palavraSecreta = carregaPalavraSecreta()
    
    letrasAcertadas = iniciaLetrasAcertadas(palavraSecreta)
    print(letrasAcertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pedeChute()

        if(chute in palavraSecreta):
            marcaChuteCorreto(chute, palavraSecreta, letrasAcertadas)
        else:
            erros += 1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

    if(acertou):
        imprimeMensagemVencedor()

    else:
        imprimeMensagemPerdedor(palavraSecreta)

def exibeMensagemInicio():
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************")

def carregaPalavraSecreta(nomeArquivo="palavras.txt"):
    arquivo = open(nomeArquivo, "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero]
    return palavraSecreta

def iniciaLetrasAcertadas(palavra):
    return ["_" for letra in palavra]

def pedeChute():
    chute = input("Tente uma letra")
    chute = chute.strip().upper()
    return chute

def marcaChuteCorreto(chute, palavraSecreta, letrasAcertadas):
    index = 0
    for letra in palavraSecreta:
        if(chute == letra):
            letrasAcertadas[index] = letra
        index += 1

def imprimeMensagemVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimeMensagemPerdedor(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________       ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|    |        |     | /   ")
    print(" |    |        |     |/     ")
    print(" |    |__      |__   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("\nFAZ O LLLLLLLLLLLLLLLLLLLLL")
    
def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print() 

if(__name__ == "__main__"):
    jogar()