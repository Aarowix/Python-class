import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
Polygon = turtle.Turtle()
ns = 7
sl = 70
ag = 360/ns
for i in range(ns):
    Polygon.forward(sl)
    Polygon.right(ag)

turtle.done()
