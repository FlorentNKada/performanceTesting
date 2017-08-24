###############################################################################
#                              basicServer.py                                 #
###############################################################################

"""This is a RPC server, which uses neither threading, nor process forking"""

import SimpleXMLRPCServer

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8000))

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
	print "basic server: small dictionary created"
	print "basic server: sending dictionary to the client..."
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
	print "basic server: big dictionary created"
	print "basic server: sending dictionary to the client..."
	return dico

server.register_function(fib, "fib")
print "basic server: fib function registered..."
server.register_function(smallDicoFib, "smallDicoFib")
print "basic server: smallDicoFib function registered..."
server.register_function(bigDicoFib, "bigDicoFib")
print "basic server: bigDicoFib function registered..."
server.register_introspection_functions() #serves for debugging
print "basic server: introspection functions registered"
print "basic server working..."
server.serve_forever() #launching the server
