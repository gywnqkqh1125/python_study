import turtle as t

t.shape('turtle')
t.color('red')
t.speed(0)

t.left(90)
n = 100

for r in range(9):
    for i in range(30):
        for a in range(5):
            t.forward(n)
            t.left(144)
        t.left(12)
    n=n+100

t.mainloop()