###############################################################################
#                           marshallingTest.py                                #
###############################################################################
"""This script is used to spawn as many client threads as we want, and every
one of them is going to connect to the DIRAC service and request for a
dictionary."""

#!/usr/bin/python
import threading
import thread
import time

import DEncode
import extendedJSON

#This is the number of client we want to spawn
NUMBER_OF_THREADS = 1000

class Client(threading.Thread):
    """Thread representing a client"""
    def __init__( self ):
        super( Client, self ).__init__()

    def run( self ):
        """Creates a variable, marshalls it, then unmarshalls it."""
        l = list()
        for i in range(100):
            l2 = list()
            for j in range(100):
                l2.append(long(j))
            t2 = tuple(l2)
            l.append(t2)
        t = tuple(l)
        marshall_test = DEncode.encode(t)
        unmarshall_test = DEncode.decode(marshall_test)

def fib( n ):
    """Recursive Fibonacci function. Returns the Fibonicci number of n"""
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

def bigDicoFib( n ):
    """Returns a dictionary which is relatively big"""
    dico = dict()
    for x in range(1000):
        dicA = dict()
        for y in range(100):
            listB = list()
            for z in range(50):
                listB.append( fib( n ) )
                print "{}\t{}\t{}".format(z,y,x)
            dicA[str(y)] = listB
        dico[str(x)] = dicA
    return dico

if __name__ == "__main__":
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

    ###############################################################################
    # We can store the 'amountOfTime' variable in any file we want                #
    ###############################################################################
    #with open("/home/florent/performanceTesting/dirac/tests_out_of_DIRAC/varible_types/long/Json.txt", "a") as myFile:   #
      #myFile.write(str(amountOfTime))                                             #
      #myFile.write(";")                                                           #
    ###############################################################################
