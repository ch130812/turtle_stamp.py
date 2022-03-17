import turtle
import random

##왼쪽 마우스 버튼 클릭하여 도장찍기 함수
def screenLeftClick(x, y):
    global r ,g ,b
    #거북이 크기 2~10 까지
    tSize = random.randrange(2, 10)
    turtle.shapesize(tSize)

    r = random.random()
    g = random.random()
    b = random.random()
    #거북이 색상 함수#
    turtle.color((r, g, b))
    # 각도는 0~ 360 까지
    tAngle = random.randrange(0, 360)

    #거북이 이동 ,각도 함수
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(tAngle)
    #거북이 도장찍기
    turtle.stamp()

#변수 초기값#
r, g, b =0.0, 0.0, 0.0
#메인 부분#
turtle.title('거북 도장 찍는 프로그램')
turtle.shape('turtle')
turtle.pensize()

turtle.onscreenclick(screenLeftClick, 1)


turtle.done()

