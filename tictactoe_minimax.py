# I know that code could have been written in better way but once it is running and since there is no client requirements I can't do it :)
class Tictactoe:
    def __init__(self):
        self.board = [['.' for i in range(3)] for j in range(3)]
        self.ai = 1
        self.human = 0
        self.winner = -1
        
    def print_board(self):
        for i in range(3):
            print(self.board[i])
    
    def check_winner(self) -> int:
        isWinnerFound = False
        currentWinner:int = -1
        for i in range(3):
            if (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]) and (self.board[i][0] != '.'):
                currentWinner = self.board[i][0]
                isWinnerFound = True
                break;
        if not isWinnerFound:
            for i in range(3):
                if (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]) and (self.board[0][i] != '.'):
                    currentWinner = self.board[0][i]
                    isWinnerFound = True
                    break;
        if not isWinnerFound:
            if (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]) and (self.board[0][0] != '.'):
                currentWinner = self.board[0][0]
                isWinnerFound = True
        if not isWinnerFound:
            if (self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]) and (self.board[2][0] != '.'):
                currentWinner = self.board[0][2]
                isWinnerFound = True
                
        if (not isWinnerFound) and self.check_draw():
            currentWinner = 2
        return currentWinner
    
    def check_draw(self):
        cnt = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    cnt += 1
        if cnt == 0:
            return True
        return False
    
    def minimax_check(self, currentPlayer:int):
        # try all possibilities
        maxi = -1
        maxpos = [-1,-1]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    self.board[i][j] = currentPlayer
                    temp = self.dfs(0)
                    if temp > maxi:
                        maxi = temp
                        maxpos = [i,j]
                    self.board[i][j] = '.'
        self.board[maxpos[0]][maxpos[1]] = currentPlayer            
    
    def dfs(self, currentPlayer:int)->int:
        isThereWinner = self.check_winner()
        if isThereWinner != -1:
            if isThereWinner == 2:
                return 0
            if isThereWinner == 1:
                return 1
            return -1

        # consider max
        if currentPlayer:
            maxi:int = -1
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '.':
                        self.board[i][j] = currentPlayer
                        maxi = max(maxi, self.dfs(0)) 
                        self.board[i][j] = '.'
            return maxi
        else:
            mini:int = 10**3
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '.':
                        self.board[i][j] = currentPlayer
                        mini = min(mini, self.dfs(1)) 
                        self.board[i][j] = '.'
            return mini        
    
    def print_winner(self, player):
        if player == 2:
            print("!!!!!       game draw     !!!!!")
        else:
            print("!!!!! player ", player, "wins   !!!!")
    
    def gameOn(self):
        currentTurn = 1
        while True:
            if currentTurn:
                print("AI plays")
                self.minimax_check(currentTurn)
            else:
                print("Player: ", currentTurn , " Please enter position : ")
                pos = int(input())
                x = pos // 3
                y = pos % 3
                self.board[x][y] = self.human
            self.print_board()
            ans = self.check_winner()
            if ans != -1:
                self.print_winner(ans)
                break
            else:
                currentTurn ^= 1
        
t1 = Tictactoe()
t1.gameOn()
