from turtle import *

s=Screen()
s.setup(600,400)   #change screen size using x and y pixels
colors=['red','yellow']  #list of colors
pencolor('green')
pensize(5)               #change pen size
for i in range(6,0,-1):
    penup()              #move pen up from screen
    setpos(0,-20*i)      #move to a position on y axis
    pendown()            #put pendown
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)         #create circle with diff radius because i changes every turn of loop
    end_fill()
mainloop()