import turtle
print("loading intro.....")

new = 2
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
a = 0
b = 0
t.speed(-1)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3 
    b+=1
    if b ==222:
        break
    t.hideturtle()

t.write("SIMBA THE AI TECH")

turtle.done()