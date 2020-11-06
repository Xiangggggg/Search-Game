import random as r

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
        
    def moveRigh(self):

    def moveLeft(self):
        

        
