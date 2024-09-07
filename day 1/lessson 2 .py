from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(20)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#step 2:paint a window
begin_fill()
left(30)
forward(50)
left(90)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
end_fill()
right(180)
#Paint two window
penup()
forward(155)
pendown()
begin_fill()
forward(45)
right(180)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
right(90)
forward(60)
end_fill()
penup()
right(90)
forward(20)
pendown
pendown
right(90)
pendown()
penup()
left(90)
forward(180)
right(90)
pendown()
forward(60)
right(90)
penup()
forward(200)
pendown()
left(90)
forward(50)



exitonclick()