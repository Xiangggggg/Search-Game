class Player:
    def __init__(self,name,row,col):
        self.name = name
        self.row = row
        self.col = col
        self.coins = 0
    
    def moveUp(self,board):
        if self.row == 0: return False
        board.board[self.row][self.col].players.remove(self.name)
        self.row -= 1
        board.board[self.row][self.col].players.append(self.name)
        return True

    def moveDown(self,board):
        if self.row == board.size-1: return False
        board.board[self.row][self.col].players.remove(self.name)
        self.row += 1
        board.board[self.row][self.col].players.append(self.name)
        return True

    def moveRight(self,board):
        if self.col == board.size-1: return False
        board.board[self.row][self.col].players.remove(self.name)
        self.col += 1
        board.board[self.row][self.col].players.append(self.name)
        return True

    def moveLeft(self,board):
        if self.col == 0: return False
        board.board[self.row][self.col].players.remove(self.name)
        self.col -= 1
        board.board[self.row][self.col].players.append(self.name)
        return True

    def __str__(self):
        return '{}: {}'.format(self.name,self.coins)