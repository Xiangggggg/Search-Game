from boardgame import Board
from player import Player

def moveinput(player):
    valid = False
    while not valid:
        if player != monster: 
            print("Searcher's Turn (u/d/l/r)")
        else: 
            print("Monster's Turn (u/d/l/r)")
        m = input()
        if move(player,m): 
            valid = True
            collectCoin(player,board.board[player.row][player.col])
        else:
            print("That is an invalid move.")
    
def move(player,m): 
    if m == "u":
        return player.moveUp(board)
    elif m == "d":
        return player.moveDown(board)
    elif m == "l":
        return player.moveLeft(board)
    elif m == "r":
        return player.moveRight(board)
    return False

def collectCoin(player,room):
    if player == searcher:
        searcher.coins += room.coins
        room.coins = 0
    
size = 5
ratio = 1/3
endgame = False
board = Board(size,ratio)
searcher = Player("Xiang",0,0)
monster = Player("Monster",size-1,size-1)
board.board[searcher.row][searcher.col].players.append(searcher.name)
board.board[monster.row][monster.col].players.append(monster.name)
collectCoin(searcher,board.board[0][0])


while not endgame:
    print(board)
    moveinput(searcher)
    print("Coins collected: %s" % searcher.coins)
    print(board)
    moveinput(monster)