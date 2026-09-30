import colorsys
import turtle

# Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Turtle Animation")

# Turtle Setup
t = turtle.Turtle()
t.speed(0)
t.width(1)
turtle.tracer(2, 0)  # Animation fast karne ke liye

n = 36
h = 0

# Animation Loop
for i in range(200):
    c = colorsys.hsv_to_rgb(h % 1.0, 1, 1)
    h += 1 / n
    t.color(c)
    
    t.forward(i)
    t.left(135)
    t.forward(i)
    t.left(135)
    t.circle(i, 45)
    t.left(135)

turtle.done()
