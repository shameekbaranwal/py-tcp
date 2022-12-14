######################################################################################
# GazepointAPI.py - Example Client
# Written in 2013 by Gazepoint www.gazept.com
#
# To the extent possible under law, the author(s) have dedicated all copyright 
# and related and neighboring rights to this software to the public domain worldwide. 
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this 
# software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
######################################################################################

import socket

# Host machine IP
HOST = '127.0.0.1'
# Gazepoint Port
PORT = 4242
ADDRESS = (HOST, PORT)

eye_client = None
# startup function
def connect_to_eye_tracker() :
    global eye_client
    # establish connection
    eye_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    eye_client.connect(ADDRESS)
    # send which data points are expected in every record 
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_CURSOR" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_POG_FIX" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_DATA" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_COUNTER" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_TIME" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_TIME_TICK" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_POG_LEFT" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_POG_RIGHT" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_POG_BEST" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_PUPIL_LEFT" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_PUPIL_RIGHT" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_EYE_LEFT" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_EYE_RIGHT" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_BLINK" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_PUPILMM" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_DIAL" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_GSR" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_HR" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_TTL" STATE="1" />\r\n'))
    eye_client.send(str.encode('<SET ID="ENABLE_SEND_PIX" STATE="1" />\r\n'))

# get next line of data and return it
def get_data_from_eye_tracker(b = 1024):
    rxdat = eye_client.recv(b)
    data = bytes.decode(rxdat)
    # print(f"[DATA FROM EYE-TRACKER] {data}")
    return data

# disconnect from the eye tracker
def disconnect_from_eye_tracker():
    eye_client.close()