import turtle
from random import randint
wn=turtle.Screen
turtle.bgcolor("lightgreen")
tom=turtle.Turtle()
tom.penup()
tom.goto(-100,220)
tom.pendown()
tom.hideturtle()
tom.write("TURTLE   RACE",font=('Times New Roman',20,'bold'))
a=turtle.Turtle()
a.pensize(2)
a.penup()
a.goto(-180,180)
a.pendown()
a.speed(0)
for i in range(0,11):
    a.write(i)
    a.right(90)
    a.penup()
    a.forward(10)
    a.pendown()
    a.forward(330)
    a.penup()
    a.backward(340)
    a.left(90)
    a.forward(40)
a.hideturtle()
b=turtle.Turtle()
b.color("red")
b.shape("turtle")
b.penup()
b.goto(-220,130)
b.pendown()


c=turtle.Turtle()
c.color("blue")
c.shape("turtle")
c.penup()
c.goto(-220,50)
c.pendown()



d=turtle.Turtle()
d.color("orange")
d.shape("turtle")
d.penup()
d.goto(-220,-30)
d.pendown()


e=turtle.Turtle()
e.shape("turtle")
e.color("gray")
e.penup()
e.goto(-220,-110)
e.pendown()


for i in range(150):
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))
    e.forward(randint(1,5))


    
    


    

