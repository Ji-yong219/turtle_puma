import turtle

t = turtle.Turtle()
# t.shape("turtle")
t.screen.setup(1200, 800)
t.speed(500)

def drawStick(a, b, c, d, width, height, cor):
    t.pendown()
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    
    if a:   t.circle(10, 90)
    else:
        t.forward(10)
        t.left(90)
        t.forward(10)
    
    t.forward(height)
    
    if b:   t.circle(10, 90)
    else:
        t.forward(10)
        t.left(90)
        t.forward(10)
        
    t.forward(width)
    
    if c:   t.circle(10, 90)
    else:
        t.forward(10)
        t.left(90)
        t.forward(10)
        
    t.forward(height)
    
    if d:   t.circle(10, 90)
    else:
        t.forward(10)
        t.left(90)
        t.forward(10)
        
    t.forward(width)
    
    t.end_fill()
    t.penup()
    
    

def drawPumaLogo():

    # P
    t.penup()
    t.goto(-400, 0)
    t.left(90)
    
    drawStick(False, False, False, False, 200, 30, "black")
    
    t.right(90)
    t.forward(90)
    t.left(90)
    
    drawStick(True, True, True, True, 150, 80, "black")
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.right(180)
    
    drawStick(True, False, False, True, 100, 5, "white")
    
    
    
    # U
    t.goto(-150, 0)
    drawStick(False, False, True, True, 200, 120, "black")
    
    t.goto(-210, 0)
    drawStick(False, False, True, True, 180, 5, "white")
    
    
    
    # M
    t.goto(90, 0)
    drawStick(True, True, False, False, 200, 200, "black")
    
    t.goto(30, -20)
    drawStick(True, True, False, False, 180, 5, "white")
    
    t.goto(-50, -20)
    drawStick(True, True, False, False, 180, 5, "white")
    
    
    
    # M
    t.goto(250, 0)
    drawStick(True, True, False, False, 200, 120, "black")
    
    t.goto(190, -20)
    drawStick(True, True, False, False, 180, 5, "white")
    
    t.right(180)
    t.forward(120)
    t.right(180)
    drawStick(False, False, False, False, 10, 5, "black")
    
    
    
    # PUMA
    t.goto(550, 350)
    t.right(45)
    t.pendown()
    t.begin_fill()
    
    # 꼬리 윗부분, 등
    t.circle(20, 180)
    t.circle(500, 25)
    t.right(45)
    t.circle(-200, 80)
    t.circle(300, 30)
    
    # 머리
    t.right(50)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.right(100)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.circle(-20, 60)
    t.circle(5, 50)
    t.left(40)
    t.circle(-15, 90)
    t.circle(5, 150)
    t.circle(-40, 30)
    t.circle(5, 50)
    t.forward(20)
    
    # 앞 다리
    t.circle(-10, 180)
    t.forward(20)
    t.circle(80, 30)
    t.circle(15, 180)
    t.circle(4, 90)
    t.circle(-8, 150)
    t.forward(40)
    t.circle(70, 40)
    t.circle(20, 60)
    t.circle(-2, 130)
    
    # 배
    t.forward(10)
    t.circle(200, 70)
    
    # 뒷 다리
    t.circle(-80, 70)
    t.circle(200, 30)
    t.right(50)
    t.forward(30)
    t.circle(30, 90)
    t.left(90)
    t.forward(30)
    t.right(70)
    t.circle(15, 90)
    t.left(50)
    t.circle(-15, 90)
    t.circle(15, 90)
    t.circle(-30, 90)
    t.circle(200, 30)
    
    # 꼬리 밑 부분
    t.right(50)
    t.forward(10)
    t.circle(200, 25)
    t.right(20)
    t.circle(-180, 30)
    t.circle(150, 17)
    
    t.end_fill()
    
    t.penup()
    t.goto(0, 0)
    t.hideturtle()
    
    

drawPumaLogo()

turtle.Screen().exitonclick()