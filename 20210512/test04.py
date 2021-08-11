import turtle as t

t.shape('turtle')

t.penup()
t.goto(-100,200)
t.pendown()

for i in range(10):
    t.forward(200)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)

t.mainloop()