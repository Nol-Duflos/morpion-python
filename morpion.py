import random

class Morpion:

#Créez un tableau à l'aide d'un tableau à 2 dimensions et initialisez chaque élément comme vide.
    def __init__(self):
        self.board = []

    def createBoard(self):
        for i in range (3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def premierJoueur(self):
        return random.randint(0, 1)
    
    def rempliSpot(self, row, col, player):
        self.board[row][col] = player

#Écrire une fonction pour vérifier si on a gagné ou non
    def joueurWin(self, player):
        win = None

        n = len(self.board)

        #les row
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        
        #les colonnes
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
                
        #Vérification des diagonales
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False
                
    
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

#Écrire une fonction pour vérifier si le tableau est rempli ou non
    #revenir sur false si le tableau contient un signe vide ou bien return true
    def isBoardFilled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True   

    def swapPlayerTurn(self, player):
        return 'X' if player == '0' else '0'
    
    def showBoard(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

#Écrire une fonction pour afficher le tableau chaque fois que l'on joue
    def start(self):
        self.createBoard()

        player = 'X' if self.premierJoueur() == 1 else '0'
        while True:
            print(f"Au tour du joueur {player}")

            self.showBoard()

            row, col = list(
                map(int, input("Remplir les colonnes : ").split()))
            print()

            self.rempliSpot(row - 1, col - 1, player)

            #Verifier si le joueur gagne ou non
            if self.joueurWin(player):
                print(f"Le joueur {player} a gagné la partie")
                break

            if self.isBoardFilled():
                print("Yay")
                break

            #changer de tour
            player = self.swapPlayerTurn(player)

            #Montrer la vue final du tableau
            print()
            self.showBoard()

#Écrire une fonction pour Démarrer le jeu
#Commencer le jeu
morpion = Morpion()
morpion.start()