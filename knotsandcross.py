import pygame
import sys
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4
# Colours
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knots and Crosses")
screen.fill(BG_COLOR)
# Board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = "X"
game_over = False

def draw_lines():
   # Horizontal
   pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE),
                    (WIDTH, SQUARE_SIZE), LINE_WIDTH)
   pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE),
                    (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
   # Vertical
   pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0),
                    (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
   pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0),
                    (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
   for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
           if board[row][col] == "O":
               pygame.draw.circle(
                   screen,
                   CIRCLE_COLOR,
                   (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    row * SQUARE_SIZE + SQUARE_SIZE // 2),
                   CIRCLE_RADIUS,
                   CIRCLE_WIDTH,
               )
           elif board[row][col] == "X":
               pygame.draw.line(
                   screen,
                   CROSS_COLOR,
                   (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                   ((col + 1) * SQUARE_SIZE - SPACE,
                    (row + 1) * SQUARE_SIZE - SPACE),
                   CROSS_WIDTH,
               )
               pygame.draw.line(
                   screen,
                   CROSS_COLOR,
                   (col * SQUARE_SIZE + SPACE,
                    (row + 1) * SQUARE_SIZE - SPACE),
                   ((col + 1) * SQUARE_SIZE - SPACE,
                    row * SQUARE_SIZE + SPACE),
                   CROSS_WIDTH,
               )

def mark_square(row, col, player):
   board[row][col] = player

def available_square(row, col):
   return board[row][col] is None

def board_full():
   for row in board:
       for cell in row:
           if cell is None:
               return False
   return True

def check_win(player):
   # Horizontal
   for row in range(BOARD_ROWS):
       if all(board[row][col] == player for col in range(BOARD_COLS)):
           return True
   # Vertical
   for col in range(BOARD_COLS):
       if all(board[row][col] == player for row in range(BOARD_ROWS)):
           return True
   # Diagonals
   if all(board[i][i] == player for i in range(BOARD_ROWS)):
       return True
   if all(board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)):
       return True
   return False

def restart():
   screen.fill(BG_COLOR)
   draw_lines()
   for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
           board[row][col] = None

draw_lines()
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
           mouseX = event.pos[0]
           mouseY = event.pos[1]
           clicked_row = mouseY // SQUARE_SIZE
           clicked_col = mouseX // SQUARE_SIZE
           if available_square(clicked_row, clicked_col):
               mark_square(clicked_row, clicked_col, player)
               if check_win(player):
                   print(f"{player} wins!")
                   game_over = True
               elif board_full():
                   print("Draw!")
                   game_over = True
               player = "O" if player == "X" else "X"
               draw_figures()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_r:
               restart()
               player = "X"
               game_over = False
   pygame.display.update()