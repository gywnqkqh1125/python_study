import turtle as t

t.shape('turtle')

def rect(길이):
    for i in range(4):
        t.forward(길이)
        t.right(90)

def move_draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    length=t.textinput('입력','길이를 입력해주세요.')
    rect(int(length))

scr=t.Screen()
scr.onclick(move_draw)
scr.listen()

t.mainloop()