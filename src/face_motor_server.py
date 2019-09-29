#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
from ohbot import ohbot
import re

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET  MOVE THE ROBOT! 
  def do_GET(self):
        self.send_response(200)
        self.end_headers()
        string_to_split = self.path.replace("/","")
        nums = re.findall('\d*\.?\d+',string_to_split)
        motor_num = int(nums[0])
        motor_position = float(nums[1])
        speed = int(nums[2])
        ohbot.move(motor_num,motor_position,speed)
        return
  
# curl 127.0.0.1:9976/move?engine=1?x=1?y=2.2?speed=1.1

def run(): 
  # Server settings
  print("starting server on:")
  # Choose port 8080, for port 80, which is normally used for a http server, 
  server_ip = "127.0.0.1"
  server_port = 8081
  server_address = (server_ip,server_port)
  sentence = 'ip: {}\nport: {}'
  print(sentence.format(server_ip,server_port))
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.server_close()
 
run()
