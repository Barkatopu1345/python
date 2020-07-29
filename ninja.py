import turtle
import math
turtle.speed(0)

turtle.bgcolor("midnightblue")

t = Turtle()
Pencolor(t, "cyan")
Penwidth(t, 1.5)
n = 5
for i in 400:
    Forward(t, n)
    Turn(t, 89.5)
    HueShift(t)
    n +=0.75

end
frontsize(20)
Message(t, "finished")
finish()

quantity = 9
turtles = [Turtle(O, true, 2pi * rand(), (rand(), rand(), 0.5)...) for i in 1:quantity]
Reposition.(turtles, first.(collect(Tiler(800, 800, 3, 3))))
n = 10
Penwidth.(turtles, 0.5)
for i in 1:300
    Forward.(turtles, n)
    HueShift.(turtles)
    Turn.(turtles, [60.1, 89.5, 110, 119.9, 120.1, 135.1, 145.1, 176, 190])
    n += 0.5
end
finish()
