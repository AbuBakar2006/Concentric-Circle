import turtle

n = int(input("Enter Number of Circles: "))
radius = 20
offset = 10

turtle.speed(50)
turtle.hideturtle()

for i in range(n):

    turtle.pendown()
    turtle.circle(radius)
    radius += offset
    turtle.penup()
    x = turtle.xcor()
    y = turtle.ycor()-offset
    turtle.goto(x, y)

turtle.done()
