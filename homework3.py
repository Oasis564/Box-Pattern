import turtle


def draw_pentagon(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72) 


turtle.speed(2)


draw_pentagon(-150, 0)  
draw_pentagon(100, 0)  


turtle.exitonclick()
