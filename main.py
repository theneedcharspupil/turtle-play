import turtle as t
from turtle import*
import turtle
'''
图形列表
1.旋涡
2.风车
3.玫瑰花
4.求婚照
'''

'''
方法列表
---表*的为作者（也就是本小学生）编写程序时用到的辅助函数，请勿删除---
1.粗细
2.速度
3.颜色
*4.玫瑰花辅助函数
*5.求婚照辅助函数1
*6.求婚照辅助函数2
'''

'''
花絮
1.有几种好看颜色供你使用(在turtle里)
'''
#旋涡

def wirlpool(n):
    for i in range(n):
        turtle.forward(n)
        turtle.left(59)
#风车

def windmill():
    for i in range(4):
        left(225)
        fd(100)
        right(90)
        circle(-150,45)
        goto(0,0)

#玫瑰花辅助函数

def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))
#求婚照辅助函数

def clear_screen():

    turtle.penup() #画笔抬起

    turtle.goto(0,0) #定位到（0，0）

    turtle.color('white')

    turtle.pensize(800) #画笔粗细

    turtle.pendown() #画笔落下

    turtle.setheading(0) #设置朝向

    turtle.fd(300) #前进

    turtle.bk(600) #后退

    # 初始化海龟的位置

def go_start(x, y, state):

    turtle.pendown() if state else turtle.penup()

    turtle.goto(x, y)

#画线，state为真时海龟回到原点，为假时不回到原来的出发点

def draw_line(length, angle, state):

    turtle.pensize(1)

    turtle.pendown()

    turtle.setheading(angle)

    turtle.fd(length)

    turtle.bk(length) if state else turtle.penup()

    turtle.penup()

# 画出发射爱心的小人

def draw_people(x, y):

    turtle.penup()

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pensize(2)

    turtle.color('black')

    turtle.setheading(0)

    turtle.circle(35, 360)

    turtle.penup()

    turtle.pensize(3)

    turtle.setheading(90)

    turtle.fd(45)

    turtle.setheading(180)

    turtle.fd(20)

    turtle.setheading(0)

    turtle.fd(35)

    turtle.pendown()

    turtle.circle(4, 360)

    turtle.penup()

    turtle.goto(x, y)

    turtle.pensize(2)

    turtle.setheading(0)

    turtle.fd(20)

    turtle.setheading(90)

    turtle.fd(20)

    turtle.setheading(-90)

    turtle.pendown()

    turtle.circle(5, 180)

    turtle.penup()

    turtle.goto(x, y)

    turtle.setheading(-90)

    turtle.pendown()

    turtle.fd(20)

    turtle.setheading(0)

    turtle.fd(35)

    turtle.setheading(60)

    turtle.fd(10)

    turtle.penup()

    turtle.goto(x, y)

    turtle.setheading(-90)

    turtle.pendown()

    turtle.fd(40)

    turtle.setheading(0)

    turtle.fd(35)

    turtle.setheading(-60)

    turtle.fd(10)

    turtle.penup()

    turtle.goto(x, y)

    turtle.setheading(-90)

    turtle.pendown()

    turtle.fd(60)

    turtle.setheading(-135)

    turtle.fd(60)

    turtle.bk(60)

    turtle.setheading(-45)

    turtle.fd(30)

    turtle.setheading(-135)

    turtle.fd(35)

    turtle.penup()

# 画爱心

def draw_heart(size):

    turtle.color('red', 'pink')

    turtle.pensize(2)

    turtle.pendown()

    turtle.setheading(150)

    turtle.begin_fill()

    turtle.fd(size)

    turtle.circle(size * -3.745, 45)

    turtle.circle(size * -1.431, 165)

    turtle.left(120)

    turtle.circle(size * -1.431, 165)

    turtle.circle(size * -3.745, 45)

    turtle.fd(size)

turtle.end_fill()

# 画箭羽

def draw_feather(size):

    angle = 30 # 箭的倾角

    feather_num = size // 6 # 羽毛的数量

    feather_length = size // 3 # 羽毛的长度

    feather_gap = size // 10 # 羽毛的间隔

    for i in range(feather_num):

        draw_line(feather_gap, angle + 180, False) # 箭柄，不折返

        draw_line(feather_length, angle + 145, True) # 羽翼，要折返

        draw_line(feather_length, angle + 145, False)

        draw_line(feather_num * feather_gap, angle, False)

        draw_line(feather_length, angle + 145 + 180, False)

        for i in range(feather_num):

        draw_line(feather_gap, angle + 180, False) # 箭柄，不折返

        draw_line(feather_length, angle - 145, True) # 羽翼，要折返

        draw_line(feather_length, angle - 145, False)

        draw_line(feather_num * feather_gap, angle, False)

        draw_line(feather_length, angle - 145 + 180, False)

        # 画一箭穿心,最后箭的头没有画出来，用海龟来代替

    def arrow_heart(x, y, size):

        go_start(x, y, False)

        draw_heart(size * 1.15)

        turtle.setheading(-150)

        turtle.penup()

        turtle.fd(size * 2.2)

        draw_heart(size)

        turtle.penup()

        turtle.setheading(150)

        turtle.fd(size * 2.2)

        turtle.color('black')

        draw_feather(size)

        turtle.pensize(4)

        turtle.setheading(30)

        turtle.pendown()

        turtle.fd(size * 2)

        turtle.penup()

        turtle.setheading(29)

        turtle.fd(size * 5.7)

        turtle.color('black')

        turtle.pensize(4)

        turtle.pendown()

        turtle.fd(size * 1.2)

        #显示倒数3,2,1

        def draw_0(i):

        turtle.speed(0)

        turtle.penup()

        turtle.hideturtle() # 隐藏箭头显示

        turtle.goto(-50, -100)

        turtle.color('red')

        write = turtle.write(i, font=('宋体', 200, 'normal'))

        time.sleep(1)

# 显示文字

def draw_1():

    turtle.penup()

    turtle.hideturtle() #隐藏箭头显示

    turtle.goto(-250, 0)

    turtle.color('red')

    write = turtle.write('臭猪猪，接招', font=('宋体', 60, 'normal'))

    time.sleep(2)

    # 显示发射爱心的小人儿

    def draw_2():

    turtle.speed(3)

    draw_people(-250, 20)

    turtle.penup()

    turtle.goto(-150, -30)

    draw_heart(14)

    turtle.penup()

    turtle.goto(-20, -60)

    draw_heart(25)

    turtle.penup()

    turtle.goto(205, -100)

    draw_heart(43)

    turtle.hideturtle()

    time.sleep(2)

    def draw_3():

    turtle.penup()

    turtle.hideturtle() # 隐藏箭头显示

    turtle.goto(-220, 50)

    turtle.color('red')

    write = turtle.write('💕不离', font=('宋体', 60, 'normal'))

    turtle.penup()

    turtle.goto(0, -50)

    write = turtle.write('不弃💕', font=('宋体', 60, 'normal'))

    time.sleep(2)

# 显示一箭穿心

def draw_4():

    turtle.speed(10)

    turtle.penup()

    turtle.goto(-210, -200)

    turtle.color('blue')

    turtle.pendown()

    turtle.write('YRB CQZ', font=('wisdom', 50, 'normal'))

    turtle.speed(1)

    turtle.penup()

    turtle.color("red")

    turtle.goto(-31, -200)

    turtle.write('❤',font=('wisdom', 50, 'normal'))

    arrow_heart(20, -60, 51)

    turtle.showturtle()

    number=[3,2,1] #储存显示界面倒数数字1,2,3



    turtle.setup(900, 500) #调画布的尺寸

    for i in number:

    draw_0(i)

    clear_screen()

    draw_1()

    clear_screen()

    draw_2()

    clear_screen()

    draw_3()

    clear_screen()

    draw_4()

    turtle.done()
'''
上述代码在获取、调整时仍存在小的缩进问题，请略做调整
'''
#玫瑰花

def rose():
    s = 0.2 # size
    t.setup(450*5*s, 750*5*s)
    t.pencolor("black")
    t.fillcolor("red")
    t.speed(100)
    t.penup()
    t.goto(0, 900*s)
    t.pendown()
    # 绘制花朵形状
    t.begin_fill()
    t.circle(200*s,30)
    DegreeCurve(60, 50*s)
    t.circle(200*s,30)
    DegreeCurve(4, 100*s)
    t.circle(200*s,50)
    DegreeCurve(50, 50*s)
    t.circle(350*s,65)
    DegreeCurve(40, 70*s)
    t.circle(150*s,50)
    DegreeCurve(20, 50*s, -1)
    t.circle(400*s,60)
    DegreeCurve(18, 50*s)
    t.fd(250*s)
    t.right(150)
    t.circle(-500*s,12)
    t.left(140)
    t.circle(550*s,110)
    t.left(27)
    t.circle(650*s,100)
    t.left(130)
    t.circle(-300*s,20)
    t.right(123)
    t.circle(220*s,57)
    t.end_fill()
    # 绘制花枝形状
    t.left(120)
    t.fd(280*s)
    t.left(115)
    t.circle(300*s,33)
    t.left(180)
    t.circle(-300*s,33)
    DegreeCurve(70, 225*s, -1)
    t.circle(350*s,104)
    t.left(90)
    t.circle(200*s,105)
    t.circle(-500*s,63)
    t.penup()
    t.goto(170*s,-30*s)
    t.pendown()
    t.left(160)
    DegreeCurve(20, 2500*s)
    DegreeCurve(220, 250*s, -1)
    # 绘制一个绿色叶子
    t.fillcolor('green')
    t.penup()
    t.goto(670*s,-180*s)
    t.pendown()
    t.right(140)
    t.begin_fill()
    t.circle(300*s,120)
    t.left(60)
    t.circle(300*s,120)
    t.end_fill()
    t.penup()
    t.goto(180*s,-550*s)
    t.pendown()
    t.right(85)
    t.circle(600*s,40)
    # 绘制另一个绿色叶子
    t.penup()
    t.goto(-150*s,-1000*s)
    t.pendown()
    t.begin_fill()
    t.rt(120)
    t.circle(300*s,115)
    t.left(75)
    t.circle(300*s,100)
    t.end_fill()
    t.penup()
    t.goto(430*s,-1070*s)
    t.pendown()
    t.right(30)
    t.circle(-600*s,35)
    t.done()

#粗细

def size(size):
    pensize(size)

#颜色

def color(color,backgroundcolor=None): 
    pencolor(color)
    bgcolor(backgroundcolor)
    
#速度

def speed(speed):
    t.speed = speed
    
'''
花絮之Python好看颜色
'''

beautiful_color = ['lightcoral','coral','darkorange','skyblue','gold','plaegreen','paleturquoise','plum','hotpink','pink']    
