import subprocess
import os

from os.path import expanduser
home = expanduser("~") + "/"
# os.system("python3 {}catkin_ws/src/robot_face/src/headturn.py {}".format(home,str(5)))

# python_bin3 = "/usr/bin/python3"
# subprocess.Popen([python_bin3, "/home/gal/catkin_ws/src/robot_face/src/go_left.py"]).wait()

os.system("python3 {}catkin_ws/src/robot_face/src/go_left.py 5".format(home))
