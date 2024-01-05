import pygame
from Board import Board

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT // ROWS

white_king = pygame.image.load('white_king.png')
white_pawn = pygame.image.load('white_pawn.png')
white_rook = pygame.image.load('white_rook.png')
white_knight = pygame.image.load('white_knight.png')
white_bishop = pygame.image.load('white_bishop.png')
white_queen = pygame.image.load('white_queen.png')

black_king = pygame.image.load('black_king.png')
black_pawn = pygame.image.load('black_pawn.png')
black_rook = pygame.image.load('black_rook.png')
black_knight = pygame.image.load('black_knight.png')
black_bishop = pygame.image.load('black_bishop.png')
black_queen = pygame.image.load('black_queen.png')

piece_images = {
    'P': white_pawn, 'R': white_rook, 'N': white_knight, 'B': white_bishop,
    'Q': white_queen, 
    'K': white_king,
    'p': black_pawn, 'r': black_rook, 'n': black_knight, 'b': black_bishop,
    'q': black_queen, 'k': black_king
}

# Colors
WHITE = (255, 255, 255)
BLACK = (75, 75, 75)

# Create the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

board = Board()
# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE
            
            clicked_position = (clicked_row, clicked_col)
            
            if selected_piece is None:
                # If no piece is selected, store the clicked position as the selected piece
                selected_piece = clicked_position
            else:
                # If a piece is already selected, attempt to make the move
                if selected_piece != clicked_position:
                    # Validate the move using your Board class methods
                    if board.is_valid_move(selected_piece, clicked_position):
                        # Make the move using your Board class methods
                        board.make_move(selected_piece, clicked_position)

    # Draw the chessboard
    for row in range(ROWS):
        for col in range(COLS):
            color = (255, 255, 255) if (row + col) % 2 == 0 else (75, 75, 75)
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Get the piece at the current board position
            piece = board.get_piece_at_position((row, col))  # Assuming get_piece_at_position returns piece at (row, col)
            if piece != ' ':
                piece_img = piece_images[piece]
                # Resize the image to fit the square size
                piece_img = pygame.transform.scale(piece_img, (SQUARE_SIZE, SQUARE_SIZE))
                win.blit(piece_img, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    pygame.display.update()

pygame.quit()