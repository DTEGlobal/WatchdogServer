__author__ = 'Cesar'

#-------------------------------------------------------------------------------
# Name:        Server
# Purpose:     This process sets the client thread dictionary with UUID and update
#              time upon connection from a client.
#
#              Max number of concurrent clientsThreads = 16
#
# Author:      Cesar, Jorge
#
# Created:     10/02/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from socket import *

global clientThreads
clientThreads = dict()

#-------------------------------------------------------------------------------
# Method:   Server
# Purpose:  This process sets the client thread dictionary with UUID and update
#           time upon connection from a client.
# Author:   CCR, JC
#
# Created:  10/02/2013
#-------------------------------------------------------------------------------
def Server():

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 8080))
    s.listen(16)

    print("Server started")

    while True:

    # 1. Wait for client connection. Upon connection get data

        conn, IP = s.accept()
        data = conn.recv(1024).decode("utf-8")
        conn.close()

    # 2. Update dictionary. Check if the UUID of the client is already on.

        UUID, time = data.split(',')
        # If UUID already exists, update the time if not it creates a new entry
        clientThreads[UUID] = time

