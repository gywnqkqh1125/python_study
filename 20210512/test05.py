import turtle as t
import random as rand

t.shape('turtle')
scr=t.Screen()
scr.setup(width=1.0, height=1.0)
t.speed(0)
t.color('red', 'yellow')
t.begin_fill()

y=rand.randint(-300, 300)
x=rand.randint(-300, 300)
s=rand.randint(100,1000)

for i in range(10):
    t.penup()
    t.goto(x,y)
    t.pendown()
    while True:
        t.forward(s)
        t.left(170)
        if abs(t.pos())<1:
            break
    y=rand.randint(-300, 300)
    x=rand.randint(-300, 300)
    s=rand.randint(100,1000)

t.end_fill()

t.mainloop()