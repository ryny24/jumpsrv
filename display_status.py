from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=0, address=0x3C)  # rev.1 users set port=0

import datetime				# for loop
import netifaces as ni			# for ethernet
import os				# for ping
import socket				# for tunnel
from contextlib import closing
import psutil				# for uptime
import time
import math

def check_socket(host, port):
   with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
    sock.settimeout(1)
    if sock.connect_ex((host, port)) == 0:
     return 'UP'
    else:
     return 'DOWN'


n = 5
while n > 0:
 print(" ------------------------- Current date:", datetime.datetime.utcnow())
 start = datetime.datetime.now()	# Track starting time

 ############  ROW 1: ETHERNET IP ############
 if 2 in ni.ifaddresses('eth0'):
  ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
 else:
  ip = ''

 ############  ROW 2: PING ############
 hostname = "208.123.173.1" #example
 #hostname = "8.8.8.9" #example
 response = os.system("ping -c 1 -W 1 " + hostname)
 print("ping response: ", response)

 #and then check the response...
 if response == 0:
  cnt = 0
  net = 'online'
  print(hostname, 'is up!')
 else:
  cnt = cnt + 1
  if cnt > 1:
   net = 'offline'
   print(hostname, 'is down! (', cnt, ')')
  else:
   net = '?????'
   print(hostname, 'going down! (', cnt, ')')

 ############  ROW 3: TUNNEL ############
 tun = check_socket('localhost', 10900)

 ############  ROW 4: UPTIME ############
 from datetime import timedelta
 seconds = time.time() - psutil.boot_time()
 my_uptime = "{}".format(str(timedelta(seconds=math.ceil(seconds))))

############    DISPLAY    ############
 with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.text((0, 0), "eth0: " + ip, font=font, fill=255)
    draw.text((0, 14), "status: " + net, font=font, fill=255)
    draw.text((0, 26), "tunnel: " + tun, font=font, fill=255)
#    draw.text((0, 38), "", font=font, fill=255)
    draw.text((0, 50), "uptime: " + my_uptime, font=font, fill=255)

 # Calculate time to wait (for a 1 second loop)
# time.sleep(1)
 diff = datetime.datetime.now() - start
 diff_in_micro_secs = diff.total_seconds() * 1000000

# print("diff: " + str(diff) + "   diff_in_micro_secs: " + str(diff_in_micro_secs))

 if  diff_in_micro_secs < 1000000:
  wait = 1000000 - diff_in_micro_secs
  print("**** Loop time was " + str(diff_in_micro_secs) + "ms. We need to wait " + str(wait) + "ms for 1 second interval ****")

  time.sleep(wait/1000000)
 else:
  print("**** NO DELAY")

