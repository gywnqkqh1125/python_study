import turtle as t

t.shape('turtle')
t.color('#BDE7FF')
t.begin_fill()

#n=int(input('숫자를 입력해 주세요. '))
for i in range(6):
    t.forward(100)
    t.right(360/6)

t.end_fill()
t.mainloop()