import pygame
import sys

# Define constants for the board dimensions
ROWS = 6
COLS = 7
EMPTY = 0
RED = 1
BLACK = 2
BLUE = (0, 0, 255)
RED_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)
YELLOW_COLOR = (255, 255, 0)
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE // 2 - 5

# Set up the game window
WIDTH, HEIGHT = COLS * SQUARE_SIZE, (ROWS + 1) * SQUARE_SIZE
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect Four")

# Function to draw the board
def draw_board(board):
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

    # Draw the tokens with animation
    for col in range(COLS):
        for row in range(ROWS):
            if board[row][col] == RED:
                pygame.draw.circle(screen, RED_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, int((HEIGHT - (ROWS - row - 0.5) * SQUARE_SIZE))), RADIUS)
            elif board[row][col] == BLACK:
                pygame.draw.circle(screen, YELLOW_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, int((HEIGHT - (ROWS - row - 0.5) * SQUARE_SIZE))), RADIUS)

    pygame.display.update()

# Create the empty board
def create_board():
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    return board

def drop_token(board, color, column):
    for row in range(ROWS - 1, -1, -1):  # Start from the bottom row
        if board[row][column] == EMPTY:  # Check for an empty slot in the column
            board[row][column] = color  # Place the token (color) in the empty slot
            return True  # Token successfully placed
    return False  # Column is full, couldn't place the token

def check_win(board, color):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == color
                and board[row][col + 1] == color
                and board[row][col + 2] == color
                and board[row][col + 3] == color
            ):
                return True  # Horizontal win

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if (
                board[row][col] == color
                and board[row + 1][col] == color
                and board[row + 2][col] == color
                and board[row + 3][col] == color
            ):
                return True  # Vertical win

    # Check diagonal (ascending direction: bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (
                board[row + 3][col] == color
                and board[row + 2][col + 1] == color
                and board[row + 1][col + 2] == color
                and board[row][col + 3] == color
            ):
                return True  # Diagonal win

    # Check diagonal (descending direction: top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (
                board[row][col] == color
                and board[row + 1][col + 1] == color
                and board[row + 2][col + 2] == color
                and board[row + 3][col + 3] == color
            ):
                return True  # Diagonal win

    return False  # No win

def get_column_from_mouse_pos(pos):
    x, _ = pos
    return x // SQUARE_SIZE


board = create_board()
turn = RED  # Start with the red player
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            column = get_column_from_mouse_pos(pygame.mouse.get_pos())
            # Get column where player clicked
            # Drop the token in that column
            drop_token(board, turn, column)

            # Check for win
            if check_win(board, turn):
                print("Player", turn, "wins!")
                game_over = True

            # Switch turns
            if turn == RED:
                turn = BLACK
            else:
                turn = RED

    # Update the display
    draw_board(board)
    pygame.display.update()