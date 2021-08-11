import turtle as t
t.speed('fastest')

def star(t):
    t.left(36)
    for i in range(5):
        t.forward(200)
        t.left(144)

def drawstar(x,y):
    #print('x좌표: {}, y좌표: {}'.format(x,y))
    t.penup()
    t.goto(x,y)
    t.pendown()
    star(t)
import random as rand
def bgchange():
    colors=['lavender','gray','light cyan','pale green']
    scr.bgcolor(colors[rand.randint(0,2)])

t.shape('turtle')

scr=t.Screen()
scr.bgcolor('orange')

#star(t)
scr.onclick(drawstar)
scr.onkey(bgchange,'c')
scr.listen()

t.mainloop()