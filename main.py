from forca import Forca

def main():
    print("JOGO DA FORCA")
    palavra_secreta = input("Digite a palavra secreta: ")
    forca = Forca(palavra_secreta)
    forca.jogar()

if __name__ == '__main__':
    main()
