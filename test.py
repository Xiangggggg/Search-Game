import pygame
from boardgame import Board
from player import Player


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define board/grid size
GRID_NUM = 10 # each row/colum
GRID_SIZE = 50
GRID_MARGIN = 3
BOARD_SIZE = GRID_NUM * GRID_SIZE + GRID_NUM * GRID_MARGIN
RATIO = 1/3

board = Board(GRID_NUM, RATIO)
searcher = Player("Searcher", 0, 0)
monster = Player("Monster", GRID_NUM-1, GRID_NUM-1)
board.board[searcher.row][searcher.col].players.append(searcher.name)
board.board[monster.row][monster.col].players.append(monster.name)
searcher.collectCoin(board)

# Create a 2 dimensional array. A two dimensional
boardview = [ [board.board[row][col].coins for col in range(GRID_NUM)] for row in range(GRID_NUM) ]
for row in boardview: print(row)
boardview[searcher.row][searcher.col] = 2

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Treasure Search Adventure")

# Set font/text
font = pygame.font.SysFont('arial', 20)
text = font.render('Hello', True, BLACK)
#rect = text.get_rect()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT: done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            col = pos[0] // (GRID_SIZE + GRID_MARGIN)
            row = pos[1] // (GRID_SIZE + GRID_MARGIN)
            print("Click ", pos, "Grid coordinates: ", row, col)
        elif event.type == pygame.KEYDOWN:
            boardview[searcher.row][searcher.col] = 0
            if event.key == pygame.K_UP:
                print('Up')
                searcher.moveUp(board)
            elif event.key == pygame.K_DOWN:
                print('Down')
                searcher.moveDown(board)
            elif event.key == pygame.K_LEFT:
                print('Left')
                searcher.moveLeft(board)
            elif event.key == pygame.K_RIGHT:
                print('Right')
                searcher.moveRight(board)
            boardview[searcher.row][searcher.col] = 2


    # Set the screen background
    screen.fill(BLACK)

    # Draw the board
    for row in range(GRID_NUM):
        for col in range(GRID_NUM):
            color = WHITE
            if boardview[row][col] == 1:
                color = GREEN
                screen.blit(text, ((GRID_MARGIN + GRID_SIZE) * col + GRID_MARGIN, (GRID_MARGIN + GRID_SIZE) * row + GRID_MARGIN))
            elif boardview[row][col] == 2:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(GRID_MARGIN + GRID_SIZE) * col + GRID_MARGIN,
                              (GRID_MARGIN + GRID_SIZE) * row + GRID_MARGIN,
                              GRID_SIZE,
                              GRID_SIZE])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()
