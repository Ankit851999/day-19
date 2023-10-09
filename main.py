from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    tim.left(30)


def turn_clockwise():
    tim.right(30)


def clear_screen():
    tim.clear()
    tim.reset()


tim.speed("fast")
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()