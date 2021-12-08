from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward,key='w')
screen.onkey(fun=move_backward,key='s')
screen.onkey(fun=move_left,key='a')
screen.onkey(fun=move_right,key='d')
screen.onkey(fun=clear_screen,key='c')

screen.exitonclick()