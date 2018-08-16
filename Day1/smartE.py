import turtle
x=50
while x<200:
    turtle.penup()
    turtle.goto(x,100)
    turtle.pendown()
    turtle.goto(2*x,100)
    turtle.goto(x,100)
    turtle.goto(x,-100)
    turtle.goto(2*x,-100)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    turtle.goto(2*x,0)
    x+=100


#turtle.penup()
#turtle.goto(100,100)
#turtle.pendown()
#turtle.goto(200,100)
#turtle.goto(100,100)
#turtle.goto(100,-100)
#turtle.goto(200,-100)
#turtle.penup()
#turtle.goto(100,0)
#turtle.pendown()
#turtle.goto(200,0)
