from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=0, address=0x3C)  # rev.1 users set port=0

############  ROW 1: ETHERNET IP ############
import netifaces as ni
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
#print(ip)  # should print "192.168.100.37"

# Alternative Method if we need
#import socket
#import fcntl
#import struct

#def get_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,  # SIOCGIFADDR
#        struct.pack('256s', ifname[:15])
#    )[20:24])
#get_ip_address('eth0')  # '192.168.0.110'

############  ROW 2: PING ############
import os
hostname = "8.8.8.8" #example
#hostname = "8.8.8.9" #example
response = os.system("ping -c 1 " + hostname)
print(response)

#and then check the response...
if response == 0:
  net = 'online'
  print(hostname, 'is up!')
else:
  net = 'offline'
  print(hostname, 'is down!')

############  ROW 3: TUNNEL ############


with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.text((0, 0), "eth0: " + ip, font=font, fill=255)
    draw.text((0, 14), "status: " + net, font=font, fill=255)
    draw.text((0, 14), "tunnel: ", font=font, fill=255)




#        draw.text((0, 0), cpu_usage(), font=font2, fill=255)
#        draw.text((0, 14), mem_usage(), font=font2, fill=255)
#        draw.text((0, 26), disk_usage('/'), font=font2, fill=255)
#        draw.text((0, 38), network('eth0'), font=font2, fill=255)
