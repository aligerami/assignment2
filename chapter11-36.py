import turtle
import random
wn=turtle.Screen()
wn.bgcolor("Black")

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.goto(-160,-160)
my_turtle.pendown()
my_turtle.color("white")
my_turtle.speed(0)
i=-160
j=-160
list_number=[]

while j<=160:
    my_turtle.pendown()
    my_turtle.forward(320)
    my_turtle.penup()     
    j=j+20
    my_turtle.goto(i,j)
i=-160
j=-160     
my_turtle.goto(i,j)
my_turtle.left(90)

while j<=160 :
    my_turtle.pendown()
    my_turtle.forward(320)
    my_turtle.penup()     
    j=j+20
    my_turtle.goto(j,i)

list_number=[]

x=(20*random.randint(0,16))-160
y=(20*random.randint(0,16))-160
my_turtle.penup()
my_turtle.goto(x,y)
list_number.append([x,y])
list_number.append([-160,-160])
print(list_number)

my_turtle.color("red")
previouse_direction=0
my_turtle.width(2)
my_turtle.pendown()
while True:
    rand=random.randint(1,4)
    #back to start of the loop if the direction was in opposite of previous direction and find new direction
    if(previouse_direction==rand):
        continue
    if rand==1:
        y=y+20
        previouse_direction=3
    elif rand==2:
        x=x-20
        previouse_direction=4
    elif rand==3:
        y=y-20
        previouse_direction=1
    else:
        x=x+20
        previouse_direction=2
    
    my_turtle.goto(x,y)
    if(any( (i==[x,y]) for i in list_number) or x==160 or y==160 or x==-160 or y==-160):
        break
    list_number.append([x,y])









   
wn.exitonclick()

    