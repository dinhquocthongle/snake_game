# Snake Class for snake_game
# By ThongLe

# Import the libraries

class Snake:
    # Constructor function
    def __init__( self, position ):
        self.score = 0
        self.segments = [position]
        self.x_pos_update = 10
        self.y_pos_update = 0
        self.current_direction = 'RIGHT'

    # Update direction
    def change_direction( self, direction ):
        if direction == 'LEFT' and self.current_direction != 'RIGHT':
            self.x_pos_update = -10
            self.y_pos_update = 0
            self.current_direction = 'LEFT'
        elif direction == 'RIGHT' and self.current_direction != 'LEFT':
            self.x_pos_update = 10
            self.y_pos_update = 0
            self.current_direction = 'RIGHT'
        elif direction == 'UP' and self.current_direction != 'DOWN':
            self.x_pos_update = 0
            self.y_pos_update = -10
            self.current_direction = 'UP'
        elif direction == 'DOWN' and self.current_direction != 'UP':
            self.x_pos_update = 0
            self.y_pos_update = 10
            self.current_direction = 'DOWN'

    # Update position
    def update_position( self ):
        last_segment = self.segments[len( self.segments ) - 1]
        first_segment = self.segments[0]
        last_segment[0] = first_segment[0] + self.x_pos_update
        last_segment[1] = first_segment[1] + self.y_pos_update
        self.segments.pop( len( self.segments ) - 1 )
        self.segments.insert( 0, last_segment)

    # Update segments when the snake eats the food
    def eat( self ):
        self.segments.insert( 0, [self.segments[0][0] + self.x_pos_update, self.segments[0][1] + self.y_pos_update])

    def killed( self ):
        for i in range( 1, len( self.segments ) ):
            if ( self.segments[0] == self.segments[i] ):
                return True
        return False

    # Get Snake first segment
    def get_snakes_head( self ):
        return self.segments[0]

    def get_the_snake( self ):
        return self.segments
