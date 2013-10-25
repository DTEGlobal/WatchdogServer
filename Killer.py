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
    os.system('echo "bone" > /dev/watchdog')

    print("Watchdog started")

#-------------------------------------------------------------------------------
# Method:   FeedWatchdog
# Purpose:  Restart Watchdog timer. Platform dependant
# Author:   CCR, JC
#
# Created:  10/02/2013
#-------------------------------------------------------------------------------
def FeedWatchdog():
    os.system('echo "bone" > /dev/watchdog')
    print(" =) Nooom - Nooom")

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
    numberOfClients = 4
    timeout = 60

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
            kill = True
        # 5. If all of the above was OK, feed Watchdog.
        if kill == False:
            FeedWatchdog()
        else:
            print(" =( ")

