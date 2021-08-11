import turtle as t
t.shape('turtle')
t.speed('fastest')

n=60
for i in range(n):
    t.circle(120)
    t.right(360/n)

t.mainloop()