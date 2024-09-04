import turtle as t
import random as r

SHOOT_DIST_MAX = 500


def move(obj, x, y):  # 객체를 이동하는 함수
    obj.pu()  # 팬을 들고
    obj.goto(x, y)  # x,y 위치로
    obj.pd()  # 다시 팬을 내려


def left():  # 왼쪽 화살표
    global angle
    angle += 2
    tu.setheading(angle)
    missile.setheading(angle)


def right():  # 오른쪽 화살표
    global angle
    angle -= 2
    tu.setheading(angle)
    missile.setheading(angle)


def shoot():  # 위 화살표
    global trajectory
    trajectory += 3
    missile.pendown()
    missile.forward(3)
    missile.penup()
    if missile.distance(blimps) < 30:  # 명중
        blimps.turtlesize(3)
        srn.bgcolor('coral')
        srn.bgcolor('coral')
        blimps.color('tomato', 'tomato')
        texter.write('BOOM!!!!', font=("Arial", 48, 'bold'))
        missile.goto(0, -200)
        trajectory = 0
        srn.ontimer(newTrial, 800)
    else:
        if trajectory > SHOOT_DIST_MAX:  # 미사일 종료
            missile.goto(0, -200)
            trajectory = 0
            srn.ontimer(newTrial, 500)
        else:  # 미사일 추적
            srn.ontimer(shoot, 20)


def newTrial():  # 새로운 시작
    texter.clear()
    missile.clear()
    initBlimps()


def initBlimps():  # 비행선 초기화
    srn.bgcolor('lightcyan')
    blimps.shape('circle');
    blimps.turtlesize(2)
    blimps.color('black', 'ivory')
    # blimps.penup()
    move(blimps, r.randint(-200, 200), r.randint(0, 200))
    blimps.penup()
    direction = r.randint(0, 1)


def moveBlimps():  # 비행선 이동
    global direction
    if direction:
        blimps.forward(2)
    else:
        blimps.backward(2)
    if -280 < blimps.xcor() < 280:  # 화면 이내
        srn.ontimer(moveBlimps, 200)
    else:  # 화면을 벋어 나면
        initBlimps()


angle = 90
direction = 1
trajectory = 0
# 스크린 객체 설정
srn = t.Screen()
srn.setup(500, 500)
srn.register_shape('missile', ((2, -3), (0, 5), (-2, -3)))
srn.bgcolor('lightcyan')
# turtle 객체 설정
tu = t.Turtle()
tu.setheading(angle)
tu.shape('turtle')
tu.turtlesize(3)
tu.color('black', 'green')
move(tu, 0, -200)
# texter 객체 설정
texter = t.Turtle()
texter.hideturtle()
texter.color('yellow', 'red')
move(texter, -100, 0)

# missile 객체 설정
missile = t.Turtle()
missile.shape('missile')
missile.color('red', 'white')
missile.turtlesize(2)
missile.setheading(90)
move(missile, 0, -200)
# blimps 객체 설정
blimps = t.Turtle()
blimps.speed(0)
initBlimps()
moveBlimps()
# screen 이벤트 바인딩
srn.onkey(shoot, "Up")
srn.onkey(left, "Left")
srn.onkey(right, "Right")
srn.onkey(newTrial, "space")
srn.onkey(srn.bye, 'Escape')
srn.listen()  # 이벤트 관리시작
srn.mainloop()  # 이벤트 서비스 루프