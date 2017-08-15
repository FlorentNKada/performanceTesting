###############################################################################
#                              myDIRACClient.py                               #
###############################################################################
"""This script is used to spawn as many client threads as we want, and every
one of them is going to connect to the DIRAC service and request for a
dictionary."""

#!/usr/bin/python
import threading
import thread
import time

from DIRAC.Core.Base.Script import parseCommandLine
from DIRAC.Core.DISET.RPCClient import RPCClient

#This is the number of client we want to spawn
NUMBER_OF_THREADS = 1

class Client(threading.Thread):
    """Thread representing a client"""
    def __init__(self):
        """A thread has a value, which it gets from a rpc request to the server"""
        super(Client, self).__init__()
        self.value=0

    def run(self):
        """The thread connects to the server,
        then it requests the wanted dictionary to the server
        and stores it in its 'value' attribute"""
        connexion = RPCClient('Framework/Fibonacci')
        self.value = connexion.bigDicoFib(1)

if __name__ == "__main__":
    parseCommandLine()
    L=list()
    start = time.time() #We start counting the time

    #Creating the threads
    for i in range(1, NUMBER_OF_THREADS+1):
        print "creating thread no {}".format(i)
        th = Client()
        th.start()
        L.append(th)
        print "thread number {} launched...".format(i)

    print "all the threads are launched..."

    #Waiting for all the threads to finish
    for i in range(NUMBER_OF_THREADS):
        L[i].join()
        print "thread no {} completed...".format(i+1)

    print "all the threads are closed..."
    end = time.time()
    amountOfTime = end-start #This is the amount of time taken to process all the requests of the clients
    print "amount of seconds taken: {}".format(amountOfTime)

    ################################################################################
    # We can store the 'amountOfTime' variable in any file we want                 #
    ################################################################################    
    #with open("valuesLists/dip/DEncode_bigDicoFib1_5threads.txt", "a") as myFile: #
      #myFile.write(str(amountOfTime))                                             #
      #myFile.write(";")                                                           #
    ################################################################################
