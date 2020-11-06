import random as r

class Board:
    def __init__(self,size):
        self.size = size
        
class Player:
    def __init__(self,name,row,col,coins=0):
        self.name = name
        self.row = row
        self.col = col
        self.coins = coins
    
    def moveUp(self):
        if self.row == 0: return 
        self.row -= 1

    def moveDown(self):
        if self.row == size-1: return
        self.row += 1

    def moveRight(self):
        if self.col == size-1: return
        self.col += 1

    def moveLeft(self):
        if self.col == 0: return
        self.col -= 1


    
    
    

        
