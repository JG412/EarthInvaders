import turtle
import random

height = 300
width = 500

score = 0
health = 10

screen = turtle.Screen()
screen.tracer(0)

screen.setup(600,400)
screen.bgpic('earthy.gif')


t=turtle.Turtle()
t.pencolor("chartreuse")
t.pensize(3)
t.hideturtle()
t.penup()
t.goto(-width/2,height/2)
t.pendown()
for i in range(2):
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)

screen.register_shape("laser",((0,5),(2,5),(2,0),(0,0),(0,5)))
screen.register_shape("batman",((4,-4),(4,-2),(10,-2),(10,2),(8,2),(7,6),(6,2),(2,2),(2,8),(1,8),(0,16),(-1,8),(-2,2),(-6,2),(-7,6),(-8,2),(-10,2),(-10,-2),(-4,-2),(-4,-4),(4,-4)))

ship=turtle.Turtle()
ship.shape("batman")
ship.color("cyan")

tt=turtle.Turtle()
tt.color("cyan")
tt.ht()
tt.penup()
tt.goto(-width/2,height/2 + 10)
tt.write("health: " + str(health),font=("Arial",12))


ttt=turtle.Turtle()
ttt.color("cyan")
ttt.ht()
ttt.penup()
ttt.goto(-width/2,height/2 + 30)
ttt.write("score: " + str(score),font=("Arial",12))


lasers = []
for i in range(20):
  l = turtle.Turtle()
  l.shape("laser")
  l.color("red")
  l.ht()
  l.penup()
  l.goto(width/2, height/2)
  lasers.append(l)

def genR(x,y):
  return random.randint(x,y)


def makeEnemies(numEnemies):
  enemies = []
  for i in range(numEnemies):
    pplbad=turtle.Turtle()
    pplbad.right(180)
    pplbad.penup()
    pplbad.goto(width/2 - genR(10,50) , genR(-height/2 + 20,height/2 - 20))
    pplbad.ht()
    enemies.append(pplbad)
  return enemies


ship.penup()
ship.goto(-width/2 + 30,0)


def up():
  x = ship.xcor()
  y = ship.ycor() + 13
  ship.goto(x, y)

def down():
  x = ship.xcor()
  y = ship.ycor() - 13  
  ship.goto(x, y)
    
a=0
def shoot():
  global a  
  a += 1
  lasers[a].goto(ship.xcor(),ship.ycor())
  lasers[a].st()
  if a >= len(lasers)-1:
    a = 0

screen.onkey(shoot,"space")
screen.onkey(down,"s")
screen.onkey(up,"w")
screen.listen()

def makeBadpplHelper():
  sooevil=random.randint(5,15)
  return makeEnemies(sooevil)


gameState = True
badguys = []
jk=turtle.Turtle()
jk.penup()
jk.ht()
jk.goto(0,height/2+20)

def screenStuff():
	screen.update()
	ttt.clear()
	ttt.write("score: " + str(score),font=("Arial",12))
	tt.clear()
	tt.write("health: " + str(health),font=("Arial",12))	

def badDude(lilTurtle, l):
	global health, score
	lilTurtle.color("magenta")
	lilTurtle.shape("turtle")
	lilTurtle.showturtle()

	lilTurtle.forward(0.15)

	x=abs(lilTurtle.xcor()-l.xcor())
	y=abs(lilTurtle.ycor()-l.ycor())

	if x<25 and y<25:
		lilTurtle.ht()
		badguys.remove(lilTurtle)
		score += 1

	elif lilTurtle.xcor()<-width/2:
		health -= 1
		lilTurtle.ht()
		badguys.remove(lilTurtle)

def shipStuff():
	if ship.ycor()>height/2 - 20:
		ship.goto(ship.xcor(),ship.ycor()-20) 
	elif ship.ycor()<-height/2 + 20:
		ship.goto(ship.xcor(),ship.ycor()+20)  


i = 0
while gameState:
	screenStuff()
	i = 0
	for l in lasers:
		
		shipStuff()
		
		l.forward(10)
		
		if len(badguys) < 1:
			badguys=makeBadpplHelper()

		if i >= len(badguys) - 1:
			i = 0
		else:
			i+=1

		badDude(badguys[i],l)

		if l.xcor()>width/2 -5:
			l.ht()

		if health<1:
			ship.write("GAME OVER", font=("Arial", 20))
			gameState=False
		

	
		
tt.clear()
tt.write("health: " + str(health),font=("Arial",12))
screen.update()