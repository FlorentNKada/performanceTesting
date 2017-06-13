###############################################################################
#                              processServer.py                               #
###############################################################################
"""This RPC server uses process forking"""

import SocketServer
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

def fib(n):
	"""Recursive Fibonacci function. Returns the fibinacci number of n"""
	if n <= 2:
		return 1
    	else:
        	return fib(n-1)+fib(n-2)

def smallDicoFib(n):
	"""Returns a relatively small dictionary (100 entries)"""
	dico = dict()
	for x in range(100):
		dico[str(x)] = fib(n)
		print x
	print "process server: small dictionary created"
	print "process server: sending dictionary to the client..."
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
	print "process server: big dictionary created"
	print "process server: sending dictionary to the client..."
	return dico


def server(address = None):
	class SimpleThreadXMLRPCServer(SocketServer.ForkingMixIn, SimpleXMLRPCServer):
        	pass

    	class RequestHandler(SimpleXMLRPCRequestHandler):
        	rpc_paths = ("")

    	if address is None:
        	address = ("localhost", 8000)

    	server = SimpleThreadXMLRPCServer(address, requestHandler = RequestHandler, logRequests = True,allow_none = True,)

	#We register the methods of our server
    	server.register_function(fib, "fib")
    	print "process server: fib function registered"
	server.register_function(smallDicoFib, "smallDicoFib")
	print "process server: smallDicoFib function registered"
	server.register_function(bigDicoFib,"bigDicoFib")
	print "process server: bigDicoFib function registered"
    	server.register_introspection_functions() #Can be used for debugging
    	print "process server: introspection functions registered"
    	print "process server working..."
    	server.serve_forever() #Launching our server

server()
