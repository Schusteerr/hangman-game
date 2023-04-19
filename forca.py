from boneco import Boneco
from palavra import Palavra
import os

class Forca:

    def __init__(self, palavra, erros = 0):
        self.erros = erros
        self.palavra = Palavra(palavra)
        self.boneco = Boneco(self.erros)

    def __display_game(self):
        os.system('clear')
        self.boneco.mostrar_boneco()
        self.palavra.mostrar_palavra()

    def __atualizar_todos_erros(self):
        self.erros+=1
        self.boneco.errar_tentativa()

    def jogar(self):

        while self.erros < 6:

            self.__display_game()

            letra = input("Tente uma letra:  ")

            if self.palavra.verificar_letra(letra):

                if self.palavra.acertar_tudo():
                    self.__display_game()
                    print("PARABÉNS!! Você ganhou!\n\n")
                    break
            else:
                self.__atualizar_todos_erros()

        if self.erros == 6:
            self.__display_game()
            print("PERDEU!! TENTE EM OUTRA OPORTUNIDADE !!\n\n")
