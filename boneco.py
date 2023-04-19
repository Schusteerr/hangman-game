class Boneco:

    def __init__(self, tentativas=0):
        self.tentativas_erradas = tentativas

    def errar_tentativa(self):
        self.tentativas_erradas += 1

    def mostrar_boneco(self):
        if self.tentativas_erradas == 0:
            print()
            print("|----- ")
            print("|    | ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        elif self.tentativas_erradas == 1:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        elif self.tentativas_erradas == 2:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|    | ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif self.tentativas_erradas == 3:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|    |\\ ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif self.tentativas_erradas == 4:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif self.tentativas_erradas == 5:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|     \\ ")
            print("_      ")
            print()
        elif self.tentativas_erradas == 6:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|   / \\ ")
            print("_      ")
            print()
