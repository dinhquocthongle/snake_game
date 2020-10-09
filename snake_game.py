# Snake Game in Python3
# By ThongLe

import pygame
import time

# Setup colors
background_color = ( 45, 45, 45 )
snake_color = food_color = ( 245, 203, 66 )
text_color = ( 252, 3, 65 )

# Setup the game environment
# The screen is sized 400x400
pygame.init()
screen = pygame.display.set_mode( ( 400, 400 ) )
screen.fill( background_color )
pygame.display.update()
pygame.display.set_caption( 'Snake Game by ThongLe' )
game_over = False

# Font stylefor text
font_style = pygame.font.SysFont( "Arial", 40 )

# Function displays the text
def display_text( content, color ) :
    text = font_style.render( content, True, color )
    screen.blit( text, [ 100, 200 ] )


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

    # Check for the border
    # Game Over if the snake hits the border
    if ( x_pos < 0 or x_pos > 400) or ( y_pos < 0 or y_pos > 400 ):
        game_over = True
        display_text( "Game Over", text_color )
        pygame.display.update()
        break

    # Setup new direction of the snake
    x_pos += x_pos_update
    y_pos += y_pos_update

    # Draw and udpate the screen
    screen.fill( background_color )
    pygame.draw.rect( screen, snake_color, [x_pos, y_pos, 10, 10] )
    pygame.display.update()

    clock.tick(30)

# For Homepage setup - To be developed
close_window = False
while not close_window:

    # Listen for the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

pygame.quit()
quit()
