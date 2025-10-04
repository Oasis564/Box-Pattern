import turtle

t = turtle.Turtle()
t.speed(0)

for _ in range(24):
    for _ in range(5):
        t.forward(100)
        t.right(72)
    t.right(15) 

turtle.done()
