# Snake Game in Python3
# By ThongLe

# Import the libraries
import pygame
import time
import random

# Import the classes
from classes.food import Food
from classes.snake import Snake

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

# Function displays the text
def display_score( content, color ) :
    text = font_style.render( content, True, color )
    screen.blit( text, [ 10, 50 ] )

# Declare the defaul position of the snake
x_pos = y_pos = 200
x_pos_update = y_pos_update = 0

# Setup the clock
clock = pygame.time.Clock()

# Setup Food
food = Food( [ random.randrange( 0, 400, 10 ), random.randrange( 0, 400, 10 ) ] )

# Setup the Snake
snake = Snake( [200, 200] )

while not game_over:

    # Listen for the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
            elif event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')

    pos = snake.get_snakes_head()
    # Check for the border
    # Game Over if the snake hits the border
    if ( pos[0] < 0 or pos[0] > 400) or ( pos[1] < 0 or pos[1] > 400 ):
        game_over = True
        display_text( "Game Over", text_color )
        pygame.display.update()
        break

    # Check if the snake reaches the food
    if ( pos[0] == food.x_pos ) and ( pos[1] == food.y_pos ):
        food.eaten()
        snake.eat()
        snake.score += 1
    # Setup new position of the snake
    else:
        snake.update_position()

    # Draw and udpate the screen
    screen.fill( background_color )
    pygame.draw.rect( screen, food_color , [food.x_pos, food.y_pos, 10, 10] )
    segs = snake.get_the_snake()
    for seg in segs:
        pygame.draw.rect( screen, snake_color, [seg[0], seg[1], 10, 10] )
    display_score( str( snake.score ), text_color );
    pygame.display.update()

    clock.tick(20)

# For Homepage setup - To be developed
close_window = False
while not close_window:

    # Listen for the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

pygame.quit()
quit()
