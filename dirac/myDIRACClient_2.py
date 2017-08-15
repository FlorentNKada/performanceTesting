###############################################################################
#                           myDIRACClient_2.py                                #
###############################################################################
   """This script is the same as 'myDIRACClient.py', but it is put in a for-loop.
   By running the script only once, you measure the time taken to process the
   requests of one client, until as many clients as you want. The problem is
   that it takes much more time than relaunching the script when you change
   the number of clients. Sometimes, this script even gets killed before
   it is finished."""

#!/usr/bin/python
import threading
import thread
import time

from DIRAC.Core.Base.Script import parseCommandLine
from DIRAC.Core.DISET.RPCClient import RPCClient

#NUMBER_OF_THREADS = 1 #This is the number of client we want to spawn

class Client(threading.Thread):
    """Thread representing a client"""
    def __init__(self):
        super(Client, self).__init__()
        self.value=0

    def run(self):
        """The thread connects to the server,
        then it requests the wanted dictionary to the server
        and stores it in its 'value' attribute"""
        connexion = RPCClient('Framework/Fibonacci')
        self.value = connexion.bigDicoFib1(1)

if __name__ == "__main__":
    for NUMBER_OF_THREADS in range(1, 11):
        parseCommandLine()
        L=list()
        start = time.time() #We start counting the time

        #Creating the threads
        for i in range(NUMBER_OF_THREADS):
            print "creating thread no {}\tnumber of clients: {}".format(i,NUMBER_OF_THREADS)
            th = Client()
            th.start()
            L.append(th)
            print "thread number {} launched...\tnumber of clients: {}".format(i,NUMBER_OF_THREADS)

        print "all the threads are launched...\tnumber of clients: {}".format(NUMBER_OF_THREADS)

        #Waiting for all the threads to finish
        for i in range(NUMBER_OF_THREADS):
            L[i].join()
            print "thread no {} completed...\tnumber of clients: {}".format(i,NUMBER_OF_THREADS)

        print "all the threads are closed...\tnumber of clients: {}".format(NUMBER_OF_THREADS)
        end = time.time()
        amountOfTime = end-start #This is the amount of time taken to process all the requests of the clients
        print "amount of seconds taken: {}\tnumber of clients: {}".format(amountOfTime,NUMBER_OF_THREADS)

       #We can store the 'amountOfTime' variable in any file we want
        with open("./valuesLists/DEncode_bigDicoFib1_1thread.txt", "a") as myFile:
            myFile.write(str(amountOfTime))
            myFile.write(";")
    print "All the values are written. Time to draw the plot."
