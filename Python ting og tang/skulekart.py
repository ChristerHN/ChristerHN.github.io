from turtle import *
t = Turtle()
t.color("Blue")
t.hideturtle()
# Importerer turtle og setter navnet til t, putter fargen blå på turtlen, gjør også at markøren blir usynlig.   


#HBygg 1 Kode

t.left(90) # Får turtlen til å snu til venstre med en 90* vinkel

for _ in range(2): # Kode som får turtlen til å gå fram med 30 2 ganger.  
    t.fd(30)
    
for _ in range(1): # Kode som får turtlen til å snu til venstre og gå fram 100 2 ganger.
    t.left(90)
    t.fd(100)
    t.fd(100)

t.left(90)
t.fd(60)

for _ in range(1): # Gjør det same som overfor, men det skriver "Bygg 1" i koden. 
    t.left(90)
    t.write(" 3. Etasje, IMA ")
    t.fd(100)
    t.fd(100)

# Bygg 1  Kode slutt

t.penup()
t.left(-180)
t.fd(200)
t.left(90)
t.fd(60)
t.pendown()

#Hall 1 Kode

for _ in range(2):
    t.fd(60)
    t.fd(30)

for _ in range(1):
    t.left(90)
    t.fd(60)

for _ in range(1):
    t.left(90)
    t.fd(180)

for _ in range(1):
    t.left(90)
    t.fd(60)

# Hall 1 kode slutt

#Kode som gjør at du kan skrive navnet på bygningen uten å tegne med hjelp av penup kommandoen. 
t.penup()
t.left(90)
t.left(90)
t.fd(20)
t.write("Hall 1")

t.penup()
t.fd(90)

#Hall 2 Kode

for _ in range(1):
    t.right(90)
    t.fd(25)
    t.pendown()

for _ in range(2):
    t.fd(75)

for _ in range(1):
    t.left(90)
    t.fd(60)

for _ in range(1):
    t.left(90)
    t.fd(150)

#Hall 2 Kode slutt

#Gjør det samme som den andre med at den skriver navn. 
t.left(90)
t.fd(60)
t.penup()
t.left(90)
t.left(90)
t.fd(20)
t.write("Hall 2")

t.home()

t.backward(200)

t.right(90)
t.forward(270)
t.pendown()
t.forward(50)

# Garasje kode
for _ in range(4):
    t.left(90)
    t.forward(55)

t.left(90)
t.penup()
t.forward(100)

t.pendown()

# Hall 3 kode
t.forward(150)
t.left(90)
t.forward(60)
t.left(90)
t.forward(150)
t.left(90)
t.forward(60)

t.backward(60)
t.left(90)
t.write("Hall 3")

#Hall 3 slutt

t.penup()
t.home()
t.forward(50)
t.pendown()

for _ in range(1):
    t.forward(200)
    t.left(90)

for _ in range(1):
    t.forward(60)
    t.left(90)

t.forward(200)
t.left(90)
t.forward(60)


t.left(90)
t.write(" 2. Etasje, SSR, Elektro ")

t.penup()
t.forward(250)
t.pendown()

for _ in range(1):
    t.forward(200)
    t.left(90)

for _ in range(1):
    t.forward(60)
    t.left(90)

t.forward(200)
t.left(90)
t.forward(60)

t.write(" 1. Etasje, Kantine, Naturfag. ")



exitonclick()  # Gjør at når du klikker så lukker fanen, istede for at den lukker automatisk.