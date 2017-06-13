###############################################################################
#                                  REDME.txt                                  #
###############################################################################

Here are the files that were used to test the performances of the different
RPC servers.

The recursive Fibonacci function has been chosen on purpose. Since the complexity
of this function explodes very fast, it can be used to assess the performances of
a server when complexity is very high.

Repository tree:
.
|__dirac
|     |__FibonacciHandler.py
|     |__myDIRACClient.py
|
|__xmlrpc
|     |__xmlrpcServers
|     |              |__basicServer.py
|     |              |__processServer.py
|     |              |__threadedServer.py
|     |
|     |__myRPCClient.py
|
|__README.txt
|__plotBuilder.py


