def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    #STRIP retira os espaços antes e depois da palavra
    palavra_secreta = palavra_secreta.strip()
    #UPPER transforma todas as letras em maiusculo
    palavra_secreta = palavra_secreta.upper()

    acertos = ["_", "_", "_", "_", "_", "_"]
    
    enforcou = False
    acertou = False
    erros = 0

    print(acertos)

    while(not enforcou and not acertou):

        chute = input("Informe uma letra:")
        chute = chute.strip()
        chute = chute.upper()
        
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                acertos[index] = letra
            index = index + 1

        print(acertos)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
