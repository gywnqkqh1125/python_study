import turtle as t

t.shape('turtle')
t.left(90)

for i in range(6):
    t.forward(300)
    t.forward(-100)

    t.left(60)
    t.forward(100)
    t.forward(-100)

    t.right(120)
    t.forward(100)
    t.forward(-100)

    t.goto(0,0)

t.mainloop()