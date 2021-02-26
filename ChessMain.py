import pygame
import ChessEngine


# Global variables
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
IMAGES = {}

# Init images


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ',
              'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(
            "images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# MAIN

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = ChessEngine.GameState()  # GAME_STATE
    load_images()
    running = True
    sqSelected = ()  # Square clicked by user tuple(row, col)
    playerClicks = []  # Where user clicked after list[(row, col), (row2,col2)]

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            # mouse handler

            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()  # (x,y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):  # The user clicked the same square twice
                    sqSelected = ()  # unselect
                    playerClicks = []  # clear clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:  # after 2nd click
                    move = ChessEngine.Move(
                        playerClicks[0], playerClicks[1], game_state.board)
                    print(move.get_chess_notation())
                    game_state.make_move(move)
                    sqSelected = ()  # Reset clicks
                    playerClicks = []  # Reset clicks

            # key handler
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:  # "z" pressed
                    game_state.undo_move()

        drawGameState(screen, game_state)
        clock.tick(15)
        pygame.display.flip()


# Graphic
def drawGameState(screen, game_state):
    drawBoard(screen)
    # later
    drawPieces(screen, game_state.board)

# Draw the squares on the board


def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Draw the pieces on the board


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':  # not empty square
                screen.blit(IMAGES[piece], pygame.Rect(
                    c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
