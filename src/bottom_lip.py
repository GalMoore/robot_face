#!/usr/bin/python3
import sys
from ohbot import ohbot

print("bottom lip moving:", sys.argv[1])
# close top lip
first_arg = float(sys.argv[1])
# second_arg = int(sys.argv[2])
ohbot.move(ohbot.BOTTOMLIP,first_arg,5)