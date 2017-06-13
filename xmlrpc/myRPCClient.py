#!/usr/bin/python
# -*-coding:utf-8 -*

###############################################################################
#                                 myRPCClient.py                              #
###############################################################################

""" This file contains the clients supposed to connect to the rpc server """

import threading
import thread
import xmlrpclib
import time

NUMBER_OF_THREADS = 10 #the number of clients to connect to the server

class Client(threading.Thread):
	"""Thread representing a client
		- __init__(self): initializes the client
		- run(self): this function is executed by every client"""
	def __init__(self):
        	"""A threads has:
        	- a value (which it gets from a rpc request to the server)"""
        	super(Client, self).__init__()
        	self.value=0

	def run(self):
        	"""The thread connects to the server, then it call any of the
		methods you need to use and stores the result in its 'value'
		attribute"""
        	s=xmlrpclib.ServerProxy('http://localhost:8000')
        	self.value=s.bigDicoFib(12)

if __name__ == "__main__":
	"""- We start by spawning the number of threads we want
	   - Each thread runs the 'run()' method (it connects to the server
	     and requests a dictionary)
	   - We wait for all the threads to finish
	   - We compute the amount of time between the opening of the threads
	     and the moment they are all closed
	   - We write the value we just computed in the file we want"""

	L=list()
    	start = time.time() #starting to measure time from here

    	for i in range(NUMBER_OF_THREADS):
        	print "creating thread number {}".format(i)
        	th = Client()
        	th.start() #starting the thread
        	L.append(th) #all the threads are stored in a list L
        	print "thread number {} launched...".format(i)

    	print "all the threads are launched..."

    	for i in range(NUMBER_OF_THREADS):
        	L[i].join() #waiting for every thread to finish
        	print "thread number {} completed...".format(i)

    	print "all the threads are closed..."
    	end = time.time()
    	amountOfTime = end-start #measuring the amount of time taken
    	print "amount of seconds taken: {}".format(amountOfTime)

	#We have a list of files for every server and every type of test.
	#We choose a certain file in which we want to store the amount of time taken.
    	with open("valuesLists/processServerBigDicoFib12.txt", "a") as myFile:
        	myFile.write(str(amountOfTime))
        	myFile.write(";")
