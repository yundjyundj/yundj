
tcolors = ['#95B9D3', '#77ADD3', '#4497D2', '#2A84C5', '#1A5D8E', '#CE8F91','#CB4E53','#B4252A','#8B1317','#780409']
''' 

 

#점수에 따라 거북이의 크기를 크게하기 위해 크기와 색상을 변수로 설정한다.

#거북이 크기 값

turtlesize = 1

#거북이의 크기

p.turtlesize(turtlesize,turtlesize)

 

#거북이의 초기 색상

p.color(tcolors[0])


 

 

#점수에 따라 거북이의 크기를 변경해주고, 색상을 변경하는 코드를 작성한다.

 

#1) 점수를 10으로 나누어서 나머지가 0일때, 즉 10의 배수일 때마다 거북이의 크기를 1 증가시킨다.

 

#2) 거북이의 크기가 무한대로 커지는 것을 방지하기 위해 크기가 30을 초과하면 30으로 고정시킨다.

 

#3) 거북이의 색상을 10단계로 나누어 두었다. 점수를 나누어서 그 몫이 10보다 작으면, 몫에 해당하는 값을 색상 리스트의 인덱스로 사용하여 색상을 변경해준다.

score += 1

 

if(score % 10 == 0):
    turtlesize += 1
    if turtlesize > 30:
        turtlesize = 30
    p.turtlesize(turtlesize,turtlesize)
   

    k = score // 10
    if k < 10:
        p.color(tcolors[k])

 

 

#거북이의 크기가 점점 커지면 벌레를 그 만큼 잘 잡을 수 있어야 한다. 따라서 거북이와 벌레의 충돌 거리 부분을 거북이의 크기에 비례해서 거리도 커지게 만든다.

#충돌 확인 함수에 거리값을 변경해주는 코드를 추가한다.

#충돌 확인 함수
'''
def isCollision(t1, t2):
    #수학식에서 두 점 사이의 거리
    d = math.sqrt( math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
     
    coll = turtlesize * 10
     
    if d < coll:
        return True
    else:
        return False
 

#위의 코드를 적용한 전체코드는 아래와 같다.

import turtle as t
import random
import math

 

#스크린 객체 생성
screen = t.Screen()
#스크린 배경색 지정
screen.bgcolor("lightgreen")
screen.tracer(2)

 

#울타리 그리기
mypen = t.Turtle()
mypen.penup()
mypen.setposition(-300, 300)
mypen.pendown()
mypen.pensize(3)

 

for x in range(4):
    mypen.forward(600)
    mypen.right(90)


mypen.hideturtle()


#Create bugs 
maxBugs = 20
bugs = []
colors = ['red','blue','purple','white','black', 'pink','#FFFF00']
shapes = ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle']
tcolors = ['#95B9D3', '#77ADD3', '#4497D2', '#2A84C5', '#1A5D8E', '#CE8F91','#CB4E53','#B4252A','#8B1317','#780409']

for count in range(maxBugs):
    c = random.randint(0,6)
    s = random.randint(0,5)
    bugs.append(t.Turtle())
    bugs[count].color(colors[c])
    bugs[count].shape(shapes[s])
    bugs[count].penup()
    bugs[count].speed(0)
    bugs[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
    bugs[count].right(random.randint(0,360))


#거북이의 크기 변수
turtlesize = 1
#Turtle 객체 p 생성
p = t.Turtle()
#p 객체의 모양을 거북이로 만들기
p.shape("turtle")
#p 객체 크기 설정
p.turtlesize(turtlesize,turtlesize)
#p 객체 색상 설정, 
#색상은 색상 이름 또는 색상 코드(#FFFFFF) 등을 이용하여 설정 할 수 있다.
p.color(tcolors[0])
#거북이를 따라다니는 선을 제거
p.penup()

#거북이의 움직임 속도
speed = 1

#거북이 점수
score = 0


def turnleft():
    p.left(30)

 

def turnright():
    p.right(30)

 

def increasespeed():
    global speed
    speed += 1

 

def decreasespeed():
    global speed
    speed -= 1

 

#점수 입력 함수
def setScore(score): 
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-290, 310)
    scorestring = "Score: %s" % score
    mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))   
 
#충돌 확인 함수   
def isCollision(t1, t2):
    #수학식에서 두 점 사이의 거리
    d = math.sqrt( math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
     
    coll = turtlesize * 10
     
    if d < coll:
        return True
    else:
        return False


screen.listen()
screen.onkey(turnleft, "Left")
screen.onkey(turnright, "Right")
screen.onkey(increasespeed, "Up")
screen.onkey(decreasespeed, "Down")


while True:
    p.forward(speed)
    
    #울타리 체크
    if p.xcor() > 300 or p.xcor() < -300:
        p.right(180)
    
    if p.ycor() > 300 or p.ycor() < -300:
        p.right(180)
            
    #다수의 벌레 움직이기
    for count in range(maxBugs):        
        
        bugs[count].forward(5)
    
        #울타리 체크
        if bugs[count].xcor() > 300 or bugs[count].xcor() < -300:
            bugs[count].right(180)
            #soundBounce()
                    
        if bugs[count].ycor() > 300 or bugs[count].ycor() < -300:
            bugs[count].right(180)    
   

        if isCollision(p, bugs[count]):
            #벌레가 먹히면 색상, 모양 변경후 다른 곳으로 이동
            bugs[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            bugs[count].right(random.randint(0,360))
            s = random.randint(0,5)
            c = random.randint(0,6)
            bugs[count].shape(shapes[s])        
            bugs[count].color(colors[c])
            
            #벌레를 먹었을 때, 점수 1 추가
            score += 1
            
            #점수에 따라 거북이 크기와 색상 변경하기
            if(score % 10 == 0):
                turtlesize += 1
                if turtlesize > 30:
                    turtlesize = 30
                p.turtlesize(turtlesize,turtlesize)
                
                k = score // 10
                if k < 10:
                    p.color(tcolors[k])
                               
            #점수를 표시
            setScore(score)
