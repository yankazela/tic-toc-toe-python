#!/usr/bin/env python3

class TicTocToe (object):
    _gameGrid = [[0 for i in range(3)] for j in range(3)]
    _xTokens = []
    _oTokens = []
    _winningGrids = []

    @classmethod
    def evaluateGameStatus(cls, player):
        result = 'c'
        tokens = cls._xTokens if player == 'X' else cls._oTokens

        for item in tokens:
            x = list(filter(lambda x: x == item, cls._gameGrid))
            if len(x) > 0:
                result = player
                break
            elif len(cls._oTokens) + len(cls._xTokens) == 9 and result != player:
                result = 'd'
                break
        return result

    @staticmethod
    def readInput(value):
        correct = False
        result = 0
        while correct == False:
            try:
                result = int(value)
                correct = True
            except:
                value = input('Incorrect input: only integers are accepted. Try again: ')
        return result

    @classmethod
    def placeToken(cls, player):
        playerCell = []
        validCell = False

        value = input("Player " + player + ", please enter a row (0, 1 or 2): ")
        playerCell.append(cls.readInput(value))

        value = input("Player " + player + ", please enter a row (0, 1 or 2): ")
        playerCell.append(cls.readInput(value))

        while validCell == False:
            if playerCell[0] < 3 and playerCell[1] < 3 and cls._gameGrid[playerCell[0]][playerCell[1]] == '\0':
                validCell = True
                cls._gameGrid[playerCell[0]][playerCell[1]] = player
                cls._xTokens.append(playerCell) if player == 'X' else cls._oTokens.append(playerCell)
            else:
                print("Wrong selection!! The cell " + " ".join(map(str, playerCell)) + " is either taken or is invalid")
                playerCell = []

                value = input("Player " + player + ", please enter a row (0, 1 or 2): ")
                playerCell.append(cls.readInput(value))

                value = input("Player " + player + ", please enter a row (0, 1 or 2): ")
                playerCell.append(cls.readInput(value))

            return cls.evaluateGameStatus(player)

    @classmethod
    def printGrid(cls):
        print(' ----------')
        for i in range(3):
            for j in range(3):
                print(' | ' + cls._gameGrid[i][j], end=''),
            print(' | ')
            print(' ----------')

    @classmethod
    def setWinningGrids(cls):
        win1 = [[0, 0], [0, 1], [0, 2]]
        win2 = [[1, 0], [1, 1], [1, 2]]
        win3 = [[2, 0], [2, 1], [2, 2]]
        win4 = [[0, 0], [1, 0], [2, 0]]
        win5 = [[0, 1], [1, 1], [2, 1]]
        win6 = [[0, 2], [1, 2], [2, 2]]
        win7 = [[0, 0], [1, 1], [2, 2]]
        win8 = [[0, 2], [1, 1], [2, 0]]

        cls._winningGrids.append(win1)
        cls._winningGrids.append(win2)
        cls._winningGrids.append(win3)
        cls._winningGrids.append(win4)
        cls._winningGrids.append(win5)
        cls._winningGrids.append(win6)
        cls._winningGrids.append(win7)
        cls._winningGrids.append(win8)

    @classmethod
    def initializeGrid(cls):
        for i in range(3):
            for j in range(3):
                cls._gameGrid[i][j] = '\0'

    @classmethod
    def startGame(cls):
        print('The game has started...')
        # cls.printGrid()
        while True:
            cls.printGrid()
            response = cls.placeToken('X')
            if response == 'x':
                print('Player X has won the game :)')
                break
            elif response == 'd':
                print('The game is finished with a draw :)')
                break
            else:
                cls.printGrid()
                print('The game continues, it\'s player\'s O turn!')
            response = cls.placeToken('O')
            if response == 'o':
                print('Player O has won the game :)')
                break
            elif response == 'd':
                print('The game is finished with a draw :)')
                break
            else:
                cls.printGrid()
                print('The game continues, it\'s player\'s X turn!')
            cls.printGrid()


def main():
    ticTocToe = TicTocToe()
    ticTocToe.initializeGrid()
    ticTocToe.setWinningGrids()
    ticTocToe.startGame()


if __name__ == "__main__":
    main()
