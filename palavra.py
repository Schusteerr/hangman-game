class Palavra:

    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta.lower()
        self.acertos = [False]*len(self.palavra_secreta)

    def mostrar_palavra(self):
        print('\n\n')
        for acerto, letra in zip(self.acertos, self.palavra_secreta):
            if acerto:
                print(letra.upper(), end=' ')
            else:
                print('_', end=' ')
        print('\n\n')

    def verificar_letra(self, tentativa):
        tem_letra = False
        for i, letra in enumerate(self.palavra_secreta):
            if tentativa.lower() == letra:
                self.acertos[i] = True
                if not tem_letra:
                    tem_letra = True
        return tem_letra

    def acertar_tudo(self):
        return all(self.acertos)
