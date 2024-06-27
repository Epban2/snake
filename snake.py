from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90  # angoli per la rotazione della testa
DOWN = 270
LEFT = 180
RIGHT = 0
LIMIT = 280
SNAKE_IMAGE="snake.gif"


def make_a_segment():
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    return segment


class Snake:
    def __init__(self):
        screen = Screen()
        screen.register_shape(SNAKE_IMAGE)  # Carica l'immagine
        self.list_of_segments = []
        self.create_snake()
        self.head = self.list_of_segments[0]
        self.head.shape(SNAKE_IMAGE)  # Imposta l'immagine come testa

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = make_a_segment()
            segment.goto(position)  #
            self.list_of_segments.append(segment)

    def extend(self):
        self.list_of_segments.append(make_a_segment())

    def move(self):
        for seg_number in range(len(self.list_of_segments) - 1, 0, -1):
            new_x = self.list_of_segments[seg_number - 1].xcor()  # coordinate del segmento precedente a quello attuale
            new_y = self.list_of_segments[seg_number - 1].ycor()
            self.list_of_segments[seg_number].goto(new_x, new_y)  # muovo alle coordinate
        self.list_of_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.list_of_segments[0].heading() != DOWN:
            self.list_of_segments[0].setheading(UP)

    def down(self):
        if self.list_of_segments[0].heading() != UP:
            self.list_of_segments[0].setheading(DOWN)

    def left(self):
        if self.list_of_segments[0].heading() != RIGHT:
            self.list_of_segments[0].setheading(LEFT)

    def right(self):
        if self.list_of_segments[0].heading() != LEFT:
            self.list_of_segments[0].setheading(RIGHT)

    def check_inside_screen(self):  # controlla che la testa sia dentro i limiti dello schermo
        xcor = self.list_of_segments[0].xcor()
        ycor = self.list_of_segments[0].ycor()
        if xcor > LIMIT or xcor < -LIMIT or ycor > LIMIT or ycor <= -LIMIT:
            return False
        else:
            return True

    def check_collision(self):
        collision = False
        for segment in self.list_of_segments[3:]:
            # Escludi i primi tre segmenti (la testa e i due segmenti iniziali)
            if self.head.distance(segment) < 10:  # Controlla la distanza tra la testa e il segmento
                collision = True
        return collision
