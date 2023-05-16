import random

def exibeMensagemInicio():
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************")

def carregaPalavraSecreta():
    arquivo = open("palavras.txt", "r")

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
    print("Parabens! Você ganhou!!")

def imprimeMensagemPerdedor():
    print("Você perdeu...")

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

        enforcou = erros == 6
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

    if(acertou):
        imprimeMensagemVencedor()

    else:
        imprimeMensagemPerdedor()  

if(__name__ == "__main__"):
    jogar()