import turtle as t
import math

scr=t.Screen()
scr.setup(width=1.0, height=1.0)
t.shape('turtle')

t.color('red', 'yellow')

for i in range(360):
    radian=math.pi*i/180.0
    sinx=math.sin(radian)
    t.goto(i, sinx*100)

t.mainloop()