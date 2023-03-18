from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=0, address=0x3C)  # rev.1 users set port=0

import netifaces as ni			# for ethernet
import os				# for ping
import psutil				# for uptime
import time
import math

n = 5
while n > 0:
############  ROW 1: ETHERNET IP ############
 if 2 in ni.ifaddresses('eth0'):
  ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
 else:
  ip = '0.0.0.0'

 ############  ROW 2: PING ############
 hostname = "208.123.173.1" #example
 #hostname = "8.8.8.9" #example
 response = os.system("ping -c 2 -W 1 " + hostname)
 print(response)

 #and then check the response...
 if response == 0:
  net = 'online'
  print(hostname, 'is up!')
 else:
  net = 'offline'
  print(hostname, 'is down!')

 ############  ROW 3: TUNNEL ############


 ############  ROW 4: UPTIME ############
 from datetime import timedelta
 seconds = time.time() - psutil.boot_time()
 my_uptime = "{}".format(str(timedelta(seconds=math.ceil(seconds))))


#my_uptime = "{:0>8}".format(str(timedelta(seconds=seconds)))
#my_uptime = "{}".format(str(timedelta(seconds=seconds)))
# Result: '00:01:06'
#"{:0>8}".format(str(timedelta(seconds=666777)))
# Result: '7 days, 17:12:57'
#"{:0>8}".format(str(timedelta(seconds=60*60*49+109)))
# Result: '2 days, 1:01:49'

#def seconds_elapsed():
#    return time.time() - psutil.boot_time()

#print(seconds_elapsed())

#def cpu_usage():
#    # load average, uptime
#    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
#    av1, av2, av3 = os.getloadavg()
#    return "Ld:%.1f %.1f %.1f Up: %s" \
#            % (av1, av2, av3, str(uptime).split('.')[0])


############    DISPLAY    ############
 with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.text((0, 0), "eth0: " + ip, font=font, fill=255)
    draw.text((0, 14), "status: " + net, font=font, fill=255)
    draw.text((0, 26), "tunnel: ", font=font, fill=255)
#    draw.text((0, 38), "", font=font, fill=255)
    draw.text((0, 50), "uptime: " + my_uptime, font=font, fill=255)


 time.sleep(0.5)			# Sleep half a second
