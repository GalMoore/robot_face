from ohbot import ohbot
import math
import time
import random
speed = 1

XMOVE = 1
YMOVE = 0
EYEMOVE = 3


xpos = 5
ypos = 5


for num in range(3000):
  lerpn = 0.9
  lerpb = 0.1

  xpos = lerpn * xpos + (1-lerpn) * random.uniform(-0.5, 0.5)
  xpos = lerpb * xpos + (1-lerpb) * math.sin(num/10.0) * 2.0 
  xpos += 5

  ypos = lerpn * ypos + (1-lerpn) * random.uniform(-0.5, 0.5)
  ypos = lerpb * ypos + (1-lerpb) * math.cos(num/10.0) * 2.0
  ypos += 5

  ohbot.move( XMOVE , xpos ,speed)
  ohbot.move( YMOVE , ypos ,speed)
  ohbot.move( EYEMOVE ,6 + math.cos(num/3.0) * 3.0 ,speed)
  ohbot.wait(speed / 15.0)
