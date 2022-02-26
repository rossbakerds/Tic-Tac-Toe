import random

class ticTacToe():
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.player = input('Please enter symbol (x or o) = ')
        print(self)
        
    def __str__(self):
        pr = str(self.board[0]) +  '\n' + str(self.board[1]) + '\n' + str(self.board[2])
        return pr
        
    def makeMove(self):
        
        while True:
            try:
                xCord = int(input('Please enter x cordinate (1,2,3) = ')) - 1
                yCord = int(input('Please enter y cordinate (1,2,3) = ')) - 1
            except (ValueError) as e:
                print("error -", e)
                continue
            if self.board[yCord][xCord] == '-':
                break
            else:
                print('invalid')
                continue
        
    
        self.board[yCord][xCord] = str(self.player)
            
        print(self)
        
    def randomAgent(self):
        while True:
            try:
                xCord = random.randint(0,2)
                yCord = random.randint(0,2)
            except ValueError:
                print("Invalid input")
                continue
            if self.board[yCord][xCord] == '-':
                break
            else:
                continue
        print('Agent chose: x = %i, y = %i' % (xCord + 1, yCord + 1))
        
        symbol = None
        if self.player == 'x':
            symbol = '/'
        else: 
            symbol = 'x'
        self.board[yCord][xCord] = symbol
        print(self)

        
    def checkWin(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '-':
            if self.board[0][0] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '-':
            if self.board[1][0] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '-':
            if self.board[2][0] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '-':
            if self.board[0][0] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '-':
            if self.board[0][1] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '-':
            if self.board[0][2] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            if self.board[0][0] == self.player:
                print('Player wins!')
            else:
                print('Random agent wins!')
            return True
        else:
            return False


game = ticTacToe()
counter = 1 
while not game.checkWin():
    if counter % 2 == 0:
        print('User turn\n')
        game.makeMove()
    else:
        game.randomAgent()
    counter += 1 
