import turtle as t
import random as rand

t.shape('turtle')

x=rand.randint(-300,300)
y=rand.randint(-300,300)
c=rand.randint(10,100)

for i in range(10):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(c)
    x=rand.randint(-300,300)
    y=rand.randint(-300,300)
    c=rand.randint(10,100)

t.mainloop()