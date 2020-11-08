import random as r
import copy as c

#creating board
def board(size):
    b = [[0 for _ in range(size)] for _ in range(size)]
    return b

#generates the hidden coin coordinates
def coincoords(cc):
    x,y = [i for i in range(size)],[i for i in range(size)]
    r.shuffle(x)
    r.shuffle(y)
    coins = []
    for _ in range(cc):
        #append into coin coords
        coins.append([x.pop(),y.pop()])
    return coins

#prints board aesthetically
def printboard(board):
    for n in board:
        print(n)
    return "\n"

#moving
def move(bo,pos,m,p): #insert bo=board,pos=position,m=move decision,p=which player
    if m == "u" and pos[0]-1 >= 0:
        bo[pos[0]][pos[1]] = 0 #reset the current spot that player is going to leave
        pos[0] -= 1
    elif m == "d" and pos[0]+1 < size:
        bo[pos[0]][pos[1]] = 0
        pos[0] += 1
    elif m == "l" and pos[1]-1 >= 0:
        bo[pos[0]][pos[1]] = 0
        pos[1] -= 1
    elif m == "r" and pos[1]+1 < size:
        bo[pos[0]][pos[1]] = 0
        pos[1] += 1
    else:
        print("That is an invalid move")
        return False
    bo[pos[0]][pos[1]] = p #moves current player to new position
    return True

#moving setup
def moveinput(b,p,c):
    while True:
        if p == 1: print("Searcher's Turn (u/d/l/r)")
        else: print("Monster's Turn (u/d/l/r)")
        m = input()
        if move(b,c,m,p): return

def checkcoin(): #checking if there is a coin
    if sc in coins:
        coins.remove(sc)
        return True
    return False

#Win conditions
def wincond():
    if cc != 0 and (sc[0] != mc[0] or sc[1] != mc[1]): return False
    elif cc == 0: print("Searcher Wins!")
    else: print("Monster Wins!")
    return True

#board setup
size = 6
cc = size//2 #coin count
b = board(size)
b2 = c.deepcopy(b)
coins = coincoords(cc)
b[0][0] = 1 #searcher
b2[size-1][size-1] = 2 #places monster at very bottom right
#initializes coords for searcher and monster
sc = [0,0]
mc = [size-1,size-1]

#actual game
while True:
    printboard(b)
    moveinput(b,1,sc)
    if checkcoin(): cc -= 1
    print("Coins left: %s" % cc)
    if wincond(): break
    printboard(b2)
    moveinput(b2,2,mc)
    if wincond(): break
