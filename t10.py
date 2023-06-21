from turtle import *
from polygon import *

speed('fastest')

# for i in range(5):
#     hexagon()
#     for i in range(3):
#         triangle()
#         for i in range(2):
#             square()
#             lt(36)
#         lt(360/3)
#     lt(360/5)

for i in range(6):
    hexagon(100)
    for i in range(6):
        hexagon(50)
        circle(50)
        lt(65)
    lt(50)



hideturtle()
mainloop()
