###############################################################################
#                              threadedServer.py                              #
###############################################################################

"""This RPC server uses multithreading. It has a thread pool at it's disposal,
in which the threads are waiting to be assigned to a task."""

import SocketServer
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

def fib(n):
	"""Recursive Fibonacci function. Returns the fibinacci number of n"""
	if n <= 2:
		return 1
   	else:
        	return fib(n - 1) + fib(n - 2)

def smallDicoFib(n):
	"""Returns a relatively small dictionary (100 entries)"""
	dico = dict()
	for x in range(100):
		dico[str(x)] = fib(n)
		print x
	print "threaded server: small dictionary created"
	print "threaded server: sending dictionary to the client..."
	return dico

def bigDicoFib(n):
	"""Returns a dictionary which is relatively big and complex"""
	dico = dict()
	for x in range(100):
		dicA = dict()
		for y in range(100):
			listB = list()
			for z in range(50):
				listB.append(fib(n))
				print z
			dicA[str(y)] = listB
		dico[str(x)] = dicA
	print "threaded server: big dictionary created"
	print "threaded server: sending dictionary to the client..."
	return dico

def myServer(address = None):
	class SimpleThreadXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer):
    		pass
  	class RequestHandler(SimpleXMLRPCRequestHandler):
    		rpc_paths = ('')
  	if address is None:
		address = ("localhost", 8000)
  	server = SimpleThreadXMLRPCServer(address, requestHandler=RequestHandler, logRequests=True, allow_none=True,)

	#We register the methods of our server
	server.register_function(fib, "fib")
  	print "threaded server: fib function registered"
	server.register_function(smallDicoFib, "smallDicoFib")
	print "threaded server: smallDicoFib function registered"
	server.register_function(bigDicoFib, "bigDicoFib")
	print "threaded server: bigDicoFib function registered"
  	server.register_introspection_functions() #Usefull for debugging
  	print "threaded server: introspection functions registered"
  	print "threaded server working..."
  	server.serve_forever() #We launch the server

myServer()
