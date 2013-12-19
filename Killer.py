__author__ = 'Cesar'

#-------------------------------------------------------------------------------
# Name:        Killer
# Purpose:     This process feeds the hardware Watchdog if all the client
#              processes reported on time
#
# Author:      Cesar, Jorge
#
# Created:     10/02/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Server
import time
import os
import logging


#-------------------------------------------------------------------------------
# Method:   StartWatchdog
# Purpose:  Disable Watchdog timer. Platform dependant. 'V' is a magic character
#           that will disable the watchdog
# Author:   CCR, JC
#
# Created:  10/02/2013
#-------------------------------------------------------------------------------
def DisableWatchdog():
    # Specific for Raspberry PI
    os.system('echo V > /dev/watchdog')

    logging.info("Watchdog disabled")


#-------------------------------------------------------------------------------
# Method:   StartWatchdog
# Purpose:  Start Watchdog timer. Platform dependant
# Author:   CCR, JC
#
# Created:  10/02/2013
#-------------------------------------------------------------------------------
def StartWatchdog():
    # Specific for Raspberry PI
    os.system("sudo chmod 777 /dev/watchdog")
    os.system('echo bone > /dev/watchdog')

    logging.info("Watchdog started")


#-------------------------------------------------------------------------------
# Method:   FeedWatchdog
# Purpose:  Restart Watchdog timer. Platform dependant
# Author:   CCR, JC
#
# Created:  10/02/2013
#-------------------------------------------------------------------------------
def FeedWatchdog():
    os.system('echo bone > /dev/watchdog')
    logging.debug(" =) Nooom - Nooom")


#-------------------------------------------------------------------------------
# Method:   Killer
# Purpose:  This process feeds the hardware Watchdog if all the client
#           processes reported on time
# Author:   CCR, JC
#
# Created:  10/02/2013
#-------------------------------------------------------------------------------
def Killer():
# 1. Get configuration parameters from main (# of threads and timeout)
    numberOfClients = 2
    timeout = 180
    notEnoughClientsTimeout = 0

    # 2. Start Hardware Watchdog (platform dependant?)
    StartWatchdog()
    while True:
        time.sleep(1)
        kill = False
        # 3. Compare table size (table set by server) with # of threads
        if len(Server.clientThreads) == numberOfClients:
            # 4. Compare each thread time entry with system time and timeout
            for id in Server.clientThreads.keys():
                currentTime = time.time()
                if currentTime - float(Server.clientThreads[id]) > timeout:
                    kill = True
                    break
        else:
            if notEnoughClientsTimeout >= timeout:
                kill = True
                notEnoughClientsTimeout = 0
            else:
                kill = False
                notEnoughClientsTimeout += notEnoughClientsTimeout

        # 5. If all of the above was OK, feed Watchdog.
        if kill == False:
            FeedWatchdog()
        else:
            logging.info("Watchdog Killer ->  =( ")

