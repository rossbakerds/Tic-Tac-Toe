import math
class ticTacToe():
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.player = 'x'
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
            if self.valid_move(xCord,yCord):
                break
            else:
                print('invalid')
                continue
        
        self.board[yCord][xCord] = str(self.player)
            
        print(self)
    
    #--------MINIMAX------------
    def miniMax(self, depth, player = 'COMP'):
        if player == 'COMP':
            best = [-1,-1, -math.inf]
        else:
            best = [-1,-1, math.inf]
            
        if depth == 0 or self.checkWin():
            score = self.evaluate()
            return [-1, -1, score]
        
        for cell in self.empty_cells():
            x, y = cell[0], cell[1]
            self.board[y][x] = player
            score = self.miniMax(depth-1, 'HUMAN')
            self.board[y][x] = '-'
            score[0],score[1] = x, y
            if player == 'COMP':
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
        return best
        
                
    def agentTurn(self):
        depth = len(self.empty_cells())
        print('Agents turn to move')
        
        if depth == 9:
            x = 1
            y = 1
        else:
            move = self.miniMax(depth, player = 'COMP')
            x, y = move[0], move[1]
            
        self.set_agent_move(x, y)
        print(self)
        
    def empty_cells(self):
        emptyCells = []
        
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == '-':
                    emptyCells.append([x,y])
                    
        return emptyCells

    def valid_move(self, x, y):
        if [x,y] in self.empty_cells():
            return True
        return False
    
    def set_agent_move(self,x,y):
        if self.valid_move(x,y):
            self.board[y][x] = 'o'
            return True
        return False
    
    def evaluate(self):
        if self.checkWinMinimax():
            return 1
        else:
            return -1
        return 0
    
    def checkWinMinimax(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '-':
            if self.board[0][0] == self.player:
                return False
            else:
                return True
            
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '-':
            if self.board[1][0] == self.player:
                return False
            else:
                return True
            
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '-':
            if self.board[2][0] == self.player:
                return False
            else:
                return True
            
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '-':
            if self.board[0][0] == self.player:
                return False
            else:
                return True
            
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '-':
            if self.board[0][1] == self.player:
                return False
            else:
                return True
            
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '-':
            if self.board[0][2] == self.player:
                return False
            else:
                return True
            
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            if self.board[0][0] == self.player:
                return False
            else:
                return True
            
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            if self.board[0][2] == self.player:
                return False
            else:
                return True
            
        else:
            return False
    #--------------------------
        
    def checkWin(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '-':
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '-':
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '-':
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '-':
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '-':
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '-':
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            return True
        else:
            return False


game = ticTacToe()

counter = 1 
while not game.checkWin():
    if len(game.empty_cells()) == 0:
        break
    if counter % 2 == 0:
        print('User turn\n')
        game.makeMove()
    else:
        game.agentTurn()
        

    counter += 1 
