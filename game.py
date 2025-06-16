import board
import pygame as pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

gameBoard = board.Board()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for square in gameBoard.squares:
        pygame.draw.rect(surface=screen,color=square.color,rect=(square.pos[0]*100, square.pos[1]*100, 100, 100))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
pygame.quit()