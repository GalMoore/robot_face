#!/usr/bin/python3
import sys
from ohbot import ohbot
import time
import os
print("picking this emotion:", sys.argv[1])
first_arg = int(sys.argv[1])

if first_arg==0:
	print("reseting ohbot")
	ohbot.reset()

if first_arg==1:
	print("smiling")

	ohbot.move(ohbot.BOTTOMLIP,8,1)
	time.sleep(1)
	ohbot.move(ohbot.BOTTOMLIP,5,1)

if first_arg==2:
	print("blinking")
	ohbot.move(ohbot.LIDBLINK,4,1)
	time.sleep(0.4)
	ohbot.move(ohbot.LIDBLINK,10,1)

if first_arg==3:
	print("raise eyebrows")
	for i in range(3):
		ohbot.move(ohbot.LIDBLINK,4,5)
		time.sleep(0.2)
		ohbot.move(ohbot.LIDBLINK,9,5)
		time.sleep(0.2)


