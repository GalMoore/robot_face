#!/usr/bin/python3
import sys
from ohbot import ohbot

print("top lip moving:", sys.argv[1])
# close top lip
first_arg = float(sys.argv[1])
# second_arg = int(sys.argv[2])
ohbot.move(ohbot.TOPLIP,first_arg,5)
