# Turtle Party Project
# by Daniel McManaman
# 7-11-24
import turtle
turtle.color("aqua")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
#forward helper function
def move(len):
  back(-1*len)
  
def polygon(side, len):
    for i in range(side):
      turtle.forward(len)
      turtle.left(360/side)
      
# for s in range(3,10):
  # move(50) # forward
  # polygon (s,100/s)
  # back(50)
  # turtle.right(360/7)
  
def spiral(len,angle):
  for i in range(len, 1, -1):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(30,60)
move(100)
spiral(100,90)
