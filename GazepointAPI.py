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

def eye_tracker_client():
    # Host machine IP
    HOST = '127.0.0.1'
    # Gazepoint Port
    PORT = 4242
    ADDRESS = (HOST, PORT)

    et_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    et_client.connect(ADDRESS)

    et_client.send(str.encode('<SET ID="ENABLE_SEND_CURSOR" STATE="1" />\r\n'))
    et_client.send(str.encode('<SET ID="ENABLE_SEND_POG_FIX" STATE="1" />\r\n'))
    et_client.send(str.encode('<SET ID="ENABLE_SEND_DATA" STATE="1" />\r\n'))
    
    return et_client

    # while 1:
    #     rxdat = et_client.recv(1024)    
    #     print(bytes.decode(rxdat))

    # et_client.close()