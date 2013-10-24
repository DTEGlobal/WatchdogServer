__author__ = 'Cesar'

#-------------------------------------------------------------------------------
# Name:        Feeder
# Purpose:     This process needs to be included on the thread to be watched.
#              Connects to a Watchdog Server and sends updates based on a random
#              UUID generated at the start of the thread to be watched.
#
#
# Author:      Cesar, Jorge
#
# Created:     10/23/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from socket import *
import uuid
import time

id = str(uuid.uuid4())

while 1:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8080))
    currentTime = str(time.time())
    toSend = id+","+currentTime
    s.send(toSend.encode())
    s.close()
    print(toSend)
    time.sleep(1)
