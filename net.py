from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=0, address=0x3C)  # rev.1 users set port=0

import netifaces as ni			# for ethernet
import os				# for ping
import psutil				# for uptime
import time
import math
import netifaces as ni


# Do not error on net ip trackback
import sys

sys.tracebacklimit = 0
#raise Exception
#Exception

n = 5
while n > 0:
############  ROW 1: ETHERNET IP ############
 eth0 = ni.ifaddresses('eth0')
 print(eth0)

# if ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']:
 if 2 in ni.ifaddresses('eth0'):
  ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
 else:
  ip = '0.0.0.0'


 print(ip)  # should print "192.168.100.37"

 from datetime import timedelta
 seconds = time.time() - psutil.boot_time()
 my_uptime = "{}".format(str(timedelta(seconds=math.ceil(seconds))))

 with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.text((0, 0), "eth0: " + ip, font=font, fill=255)
#    draw.text((0, 14), "status: " + net, font=font, fill=255)
#    draw.text((0, 26), "tunnel: ", font=font, fill=255)
#    draw.text((0, 38), "", font=font, fill=255)
    draw.text((0, 50), "uptime: " + my_uptime, font=font, fill=255)


 time.sleep(0.5)			# Sleep half a second
