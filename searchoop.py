from boardgame import Board
from player import Player

def moveInput(player):
    valid = False
    while not valid:
        if player != monster: 
            print("Searcher's Turn (u/d/l/r)")
        else: 
            print("Monster's Turn (u/d/l/r)")
        m = input()
        if player.move(m,board): 
            valid = True
            player.collectCoin(board)
        else:
            print("That is an invalid move.")
    
size = 5
ratio = 1/3
endgame = False
board = Board(size,ratio)
searcher = Player("Searcher",0,0)
monster = Player("Monster",size-1,size-1)
board.board[searcher.row][searcher.col].players.append(searcher.name)
board.board[monster.row][monster.col].players.append(monster.name)
searcher.collectCoin(board)

while not endgame:
    print(board)
    moveInput(searcher)
    print("Coins collected: %s" % searcher.coins)
    print(board)
    moveInput(monster)