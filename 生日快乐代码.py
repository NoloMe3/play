import turtle as t
import random as r
import math
def draw_x(x, i):
    return x*math.cos(math.radians(i))
def draw_y(y,i):
    return y*math.sin(math.radians(i))
def ground_floor(width,height,colors_a,h):
    t.penup()
    t.goto(width, h)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colors_a[0])
    for i in range(360):
        x=draw_x(width, i)
        y=draw_y(height,i)+h
        t.goto(x,y)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(colors_a[1])
    for i in range(180):
        x=draw_x(width, -i)
        y=draw_y(height+10,-i)+h
        t.goto(x,y)
    for i in range(180,360):
        x=draw_x(width, i)
        y=draw_y(height,i)+h
        t.goto(x,y)
    t.end_fill()
def each_piece(width,height_1,height_2,colors_b,h):
    t.penup()
    t.goto(width,h)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colors_b[0])
    for i in range(360):
        x=draw_x(width, i)
        y=draw_y(height_1,i)+h
        t.goto(x,y)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(colors_b[0])
    for i in range(540):
        x=draw_x(width, i)
        y=draw_y(height_1,i)+height_2+h
        t.goto(x,y)
    t.goto(-width,h)
    t.end_fill()
    t.penup()
    t.goto(width-10,height_2+h)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colors_b[1])
    for i in range(360):
        x=draw_x(width - 10, i)
        y=draw_y(height_1*0.9,i)+height_2+h
        t.goto(x,y)
    t.end_fill()
    t.penup()
    t.goto(width,h)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colors_b[2])
    for i in range(180):
        x=draw_x(width, -i)
        y=draw_y(height_1,-i)+10+h
        t.goto(x,y)
    t.goto(-width,h)
    for i in range(180,360):
        x=draw_x(width, i)
        y=draw_y(height_1,i)+h
        t.goto(x,y)
    t.end_fill()
    t.penup()
    t.goto(width,height_2+h)
    t.pendown()
    t.begin_fill()
    t.fillcolor(colors_b[3])
    for i in range(1800):
        x=draw_x(width, 0.1 * i)
        y=draw_y(-height_1*0.3,i)+h
        t.goto(x,y)
    t.goto(-width,height_2+h)
    for i in range(180,360):
        x=draw_x(width, i)
        y=draw_y(height_1,i)+height_2+h
        t.goto(x,y)
    t.end_fill()
def candle(width,height,color_c,w,h1,h2):
    t.penup()
    t.goto(w,h1)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color_c[0])
    for i in range(360):
        x = draw_x(width, i) + w
        y = draw_y(height, i)+h1
        t.goto(x, y)
    t.goto(width+w, h2)
    for i in range(540):
        x = draw_x(width, i) + w
        y = draw_y(height, i)+h2
        t.goto(x, y)
    t.goto(-width+w, h1)
    t.end_fill()
    t.pencolor(color_c[1])
    for i in range(1, 6):
        t.goto(width+w, h1 + 10 * i)
        t.penup()
        t.goto(-width+w, h1 + 10 * i)
        t.pendown()
    t.penup()
    t.goto(w, h2)
    t.pendown()
    t.goto(w, h2)
def star(w1,w2,h1,h2,a,color):
    t.penup()
    x=r.randint(w1,w2)
    y=r.randint(h1,h2)
    c=color
    t.goto(x,y)
    t.pendown()
    t.pencolor(c)
    t.begin_fill()
    t.fillcolor(c)
    for i in range(5):
        t.forward(a)
        t.right(144)
        t.forward(a)
        t.left(72)
    t.end_fill()
def Stars(n,w1,w2,h1,h2,a,c):
    for i in range(n):
        star(w1,w2,h1,h2,a,c)
def Year(w,h,c,o):
    t.penup()
    t.goto(w,h)
    t.pendown()
    t.pencolor(c)
    t.write(o,font=("Curlz MT", 25))
t.tracer(0)
#t.Turtle().screen.delay(0)
colors_a=['oldlace','mistyrose']
colors_b=['lightcyan','oldlace','pink','mistyrose']
colors_c=['skyblue','white']
t.setup(0.6,0.6)
t.screensize(1.0,0.75)
t.hideturtle()
t.bgcolor('aliceblue')
t.pencolor("white")
t.Turtle().screen.delay(0)
ground_floor(160,30,colors_a,-50)
each_piece(120,30,40,colors_b,-50)
each_piece(90,20,30,colors_b,-10)
each_piece(60,10,20,colors_b,20)
candle(4,1,colors_c,15,40,100)
candle(4,1,colors_c,-15,40,100)
Year(-22,95,'skyblue','3')
Year(8,95,'skyblue','岁')
color='pink'
Stars(50,-300,300,150,300,3,color)
t.penup()
t.goto(-250,200)
t.pendown()
t.pencolor("pink")
t.write("Happy Birthday!", font=("Curlz MT", 50))
t.mainloop()