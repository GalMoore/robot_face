#!/usr/bin/python3
import sys
from ohbot import ohbot

print("this is what eyes got from os /sys argv[1]:", sys.argv[1])
# close top lip
first_arg = float(sys.argv[1])
# second_arg = int(sys.argv[2])
ohbot.move(ohbot.EYETURN,first_arg,1)