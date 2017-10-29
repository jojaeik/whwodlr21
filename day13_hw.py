import turtle as t
import random
t.shape("turtle")
te = t.Turtle() #장애물
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 70)
t.speed(0)
x = 0
while x < 100 :
    a = random.randint(1, 360)
    t.setheading(a)
    tx, ty = t.pos()
    print(tx, ty) #좌표출력
    if t.distance(te) < 40:
        ang = t.towards(te.pos())
        t.setheading(ang)
        ang = random.randint(180, 360)
        t.setheading(ang)
        t.forward(20)
    else:
        if tx < -140 or tx > 140 or ty < -140 or ty > 140:
            ang = t.towards(0,0)
            t.setheading(ang)
            t.forward(40)
        else:
            t.forward(40)	
