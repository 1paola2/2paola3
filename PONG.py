import turtle

#ventana
ventana = turtle.Screen()
ventana.title("PONG By Paola")
ventana.bgcolor("#00beff")
ventana.setup(width=800,height=600)
ventana.tracer(0)

#Marcador
marcador1=0
marcador2=0

#Jugador1
jug1 = turtle.Turtle ()
jug1.speed(0) #solo para que aparezca en la ventana
jug1.shape("square")
jug1.color("#ff8000")
jug1.penup() # quita linea
jug1.goto(-350,-250)
jug1.shapesize(stretch_wid=5,stretch_len=1)

#Jugador2
jug2 = turtle.Turtle ()
jug2.speed(0) #solo para que aparezca en la ventana
jug2.shape("square")
jug2.color("#ff8000")
jug2.penup() # quita turtle
jug2.goto(350,250)
jug2.shapesize(stretch_wid=5,stretch_len=1)

#bola
bola = turtle.Turtle()
bola.speed(0) #solo para que aparezca en la ventana
bola.shape("circle")
bola.color("white")
bola.penup()
bola.dx = 3
bola.dy = 3

#linea del centro
linea = turtle.Turtle()
linea.speed(0)
linea.color("white")
linea.goto(0,400)
linea.goto(0,-400)


#marcador2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador1 : 0         Jugador2: 0", align= "center", font= ("Courier", 24, "normal"))
#Movimiento

def jug1_up():
   y = jug1.ycor()
   y += 20
   jug1.sety(y)
def jug1_dw():
    y = jug1.ycor()
    y -= 20
    jug1.sety(y)
def jug2_up():
   y = jug2.ycor()
   y += 20
   jug2.sety(y)
def jug2_dw():
    y = jug2.ycor()
    y -= 20
    jug2.sety(y)

 #teclado
ventana.listen()
ventana.onkeypress(jug1_up,"w")
ventana.onkeypress(jug1_dw,"s")
ventana.onkeypress(jug2_up,"Up")
ventana.onkeypress(jug2_dw,"Down")

while True:
    ventana.update()

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #limite
    if bola.ycor()>290:
        bola.dy *=-1
    if bola.ycor()<-290:
        bola.dy *=-1
    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        marcador1 +=10
        pen.clear()
        pen.write("Jugador1 : {}        Jugador2: {}".format(marcador2,marcador1), align="center", font=("Courier", 24, "normal"))
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx*=-1
        marcador2 +=10
        pen.clear()
        pen.write("Jugador1 : {}        Jugador2: {}".format(marcador2,marcador1), align="center", font=("Courier", 24, "normal"))
    #colision
    if ((bola.xcor()>340 and bola.xcor()<350) and (bola.ycor() < jug2.ycor() + 50 and bola.ycor() > jug2.ycor() -50 )):
        bola.dx *=-1
    if ((bola.xcor()<-340 and bola.xcor()>-350) and (bola.ycor() < jug1.ycor() + 50 and bola.ycor() > jug1.ycor() -50 )):
        bola.dx *=-1