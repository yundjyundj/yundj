import turtle # 터틀 그래픽 모듈을 불러온다.
import random # 난수 모듈을 불러온다.

for i in range(5):
        t1 = turtle.Turtle() # 첫 번째 거북이를 생성한다.
        t1.shape("turtle")
        t1.color("lightgreen")
        t1.pensize(5) # 팬의 두께를 5로 한다.
        t1.penup() # 펜을 든다.
        t1.goto(-300, 0) # (-300, 0) 위치로 간다.

        t2 = turtle.Turtle() # 두 번째 거북이를 생성한다.
        t2.shape("turtle")
        t2.pensize(5) # 팬의 두께를 5로 한다.
        t2.penup() # 펜을 든다.
        t2.goto(-300, -200) # (-300, -100) 위치로 간다.

        t1.pendown() # 첫 번째 거북이의 펜을 내린다.
        t2.pendown() # 첫 번째 거북이의 펜을 내린다.

        t1.speed(1) # 0 : 가장 빠름, 1 : 가장 느림, 6 : 기본
        t2.speed(1)
        for i in range(100): # 100번 반복한다.
                d1 = random.randint(1, 60) # 1부터 60 사이의 난수를 발생한다.
                t1.forward(d1) # 난수만큼 이동한다.
                d2 = random.randint(1, 60) # 1부터 60 사이의 난수를 발생한다.
                t2.forward(d2)
                if t1.position()[0]>=200 or t2.position()[0]>=200: break

        t1.penup()
        t2.penup()

        ##t1.speed(6) # 0 : 가장 빠름, 1 : 가장 느림, 6 : 기본
        ##t2.speed(6)

        win=t1 if t1.position()[0]>t2.position()[0] else t2
        win.left(90)
        for i in range(30):
        ##    win.right(30)
            win.forward(15)
            win.backward(15)
            win.write('wow')
        t1.clear()
        t2.clear()
        ##    win.right(180)
        ##    win.forward(5)
        ##    win.right(180)
        '''
        if t1.position()[0]>t2.position()[0]:
            for i in range(10):
                t1.right(30)
                t1.forward(5)
                t1.right(180)
                t1.forward(5)
                t1.right(180)
        else:
            for i in range(10):
                t2.right(30)
                t2.forward(5)
                t2.right(180)
                t2.forward(5)
                t2.right(180)
        '''
