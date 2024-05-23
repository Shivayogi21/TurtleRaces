# import turtle
# the above project is for the making the circle with using the asde and c

# tim=Turtle()
# screen=Screen()
#
#
# def move_forword():
#     tim.forward(10)
#
# def move_backword():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey( move_forword,'w')
# screen.onkey( move_backword,'s')
# screen.onkey( turn_left,'a')
# screen.onkey( turn_right,'d')
# screen.onkey( clear,'c')
#
# screen.exitonclick()



# Turtle race project starts


from turtle import Turtle,Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='make your bet',prompt='which turtle will win the race ? Enter a color :')
colors = ['red','green','blue','violet','orange','yellow']
y_position=[-78,-48,-14,20,50,82]
all_turtles=[]

for turtle_index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=-y_position[turtle_index])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'you won ! the {winning_color} is winner')
            else:
                print(f'you lose ! the {winning_color} is winner')
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()



