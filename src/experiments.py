import subprocess
import os

from os.path import expanduser
home = expanduser("~") + "/"

os.system("python3 {}catkin_ws/src/robot_face/src/go_left.py 5".format(home))
