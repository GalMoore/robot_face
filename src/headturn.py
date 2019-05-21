#!/usr/bin/python3
import sys
from ohbot import ohbot

print("this is what headturn got from os /sys argv[1]:", sys.argv[1])
# close top lip
first_arg = float(sys.argv[1])
# second_arg = int(sys.argv[2])
ohbot.move(ohbot.HEADTURN,first_arg,1)






# ohbot.wait(1)
# ohbot.move(ohbot.HEADNOD,9,1)
# # close bottom lip
# ohbot.move(5,6,5)