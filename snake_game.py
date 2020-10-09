# Snake Game in Python3
# By ThongLe

import pygame

# Setup colors
background_color = ( 45, 45, 45 )
snake_color = food_color = ( 245, 203, 66 )


# Setup the game environment
# The screen is sized 400x400
pygame.init()
screen = pygame.display.set_mode( ( 400, 400 ) )
screen.fill( background_color )
pygame.display.update()
pygame.display.set_caption( 'Snake Game by ThongLe' )
game_over = False

# Declare the defaul position of the snake
x_pos = y_pos = 200
x_pos_update = y_pos_update = 0

# Setup the clock
clock = pygame.time.Clock()

while not game_over:

    # Listen for the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_pos_update = -10
                y_pos_update = 0
            elif event.key == pygame.K_RIGHT:
                x_pos_update = 10
                y_pos_update = 0
            elif event.key == pygame.K_UP:
                x_pos_update = 0
                y_pos_update = -10
            elif event.key == pygame.K_DOWN:
                x_pos_update = 0
                y_pos_update = 10

    # Setup new direction of the snake
    x_pos += x_pos_update
    y_pos += y_pos_update

    screen.fill( background_color )
    pygame.draw.rect( screen, snake_color, [x_pos, y_pos, 10, 10] )
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
