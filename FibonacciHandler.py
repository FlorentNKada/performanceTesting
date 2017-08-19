###############################################################################
#                             FibonacciHandler.py                             #
###############################################################################
"""This service can compute Fibonacci numbers and create dictionaries."""

__RCSID__ = "$Id: $"

import types
from DIRAC.Core.DISET.RequestHandler import RequestHandler
from DIRAC import gLogger, S_OK, S_ERROR

class FibonacciHandler(RequestHandler):
    """This is a DIRAC service that can compute Fibonacci numbers and create dictionaries."""

    @classmethod
    def initializeHandler(cls, serviceInfo):
        """This method initializes the FibonacciHandler class"""
        return S_OK()

    def initialize(self):
        """This method initializes each FibonacciHandler instance"""
        return S_OK()

    types_fibo = [types.IntType] #any argument passed to the fib() method must be an integer
    def export_fibo(self, n):
        """Recursive Fibonacci function. Returns S_OK(fibo(n)) """
        if n <= 2:
            result = 1
        else:
            result = self.export_fibo(n - 1)['Value'] + self.export_fibo(n - 2)['Value']
        return S_OK(result)

    types_smallDicoFib = [types.IntType]
    def export_smallDicoFib(self, n):
        """Returns a relatively small dictionary (100 entries)"""
        dico = dict()
        for x in range(100):
            dico[str(x)] = self.export_fibo(n)['Value']
            print x
        return S_OK(dico)

    types_bigDicoFib = [types.IntType]
    def export_bigDicoFib(self, n):
        """Returns a dictionary which is relatively big and complex"""
        dico = dict()
        for x in range(1000):
            dicA = dict()
            for y in range(100):
                listB = list()
                for z in range(50):
                    listB.append(self.export_fibo(n)['Value'])
                    print "{}\t{}\t{}".format(z,y,x)
                dicA[str(y)] = listB
            dico[str(x)] = dicA

            #L = list()
            #for y in range(1000):
                #L.append(self.export_fibo(n)['Value'])
                #print y
                #print '\ttuple {} created'.format(x)
            #T = tuple(L)
            #dico[str(x)] = T
        return S_OK(dico)
