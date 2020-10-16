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

    # Update direction
    def change_direction( self, direction ):
        if direction == 'LEFT':
            self.x_pos_update = -10
            self.y_pos_update = 0
        elif direction == 'RIGHT':
            self.x_pos_update = 10
            self.y_pos_update = 0
        elif direction == 'UP':
            self.x_pos_update = 0
            self.y_pos_update = -10
        elif direction == 'DOWN':
            self.x_pos_update = 0
            self.y_pos_update = 10

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
        copy_segments = self.segments.copy()
        new_segment = copy_segments[0]
        print( new_segment , ' ' , self.segments[0])
        new_segment[0] += self.x_pos_update
        new_segment[1] += self.y_pos_update
        self.segments.insert( 0, new_segment)
        print( new_segment , ' ' , self.segments[0])

    # Get Snake first segment
    def get_snakes_head( self ):
        return self.segments[0]

    def get_the_snake( self ):
        return self.segments
