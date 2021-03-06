__author__ = 'Cesar'
#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     This process run the Server and Killer processes of the Watchdog,
#              it also reads the configuration parameters:
#                   1. Number of threads to check.
#                   2. Watchdog timeout.
#
# Author:      Cesar, Jorge
#
# Created:     10/02/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import threading
import logging

from Killer import Killer
from Server import Server

logging.basicConfig(format='%(asctime)s - [%(levelname)s]: %(message)s',
                    filename='/home/pi/logs/watchdogServer.log',
                    level=logging.INFO)
logging.info('Watchdog main - Started')

ServerThread = threading.Thread(target=Server)
ServerThread.daemon = True
ServerThread.start()

KillerThread = threading.Thread(target=Killer)
KillerThread.daemon = True
KillerThread.start()


while True:
    a = 0  # Do nothing
