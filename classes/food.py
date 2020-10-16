# Food Class for snake_game
# By ThongLe

# Import the libraries
import random

class Food:
    # Constructor function
    def __init__( self, position ):
        self.x_pos = position[0]
        self.y_pos = position[1]

    # Setup new food position
    def eaten( self ):
        self.x_pos = random.randrange( 0, 400, 10 )
        self.y_pos = random.randrange( 0, 400, 10 )
