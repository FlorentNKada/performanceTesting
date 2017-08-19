""" This service proposes two methods accessible to the client:
- export_sayHello( self, whom ) says 'Hello' to someone
- export_fibo(self, n) returns S_OK(fibo(n))
"""

__RCSID__ = "$Id: $"

import types
from DIRAC.Core.DISET.RequestHandler import RequestHandler
from DIRAC import gLogger, S_OK, S_ERROR
from DIRAC.Core.Utilities import Time

class HelloHandler( RequestHandler ):
    @classmethod
    def initializeHandler( cls, serviceInfo ):
        """ This method initializes the HelloHandler class"""

        cls.defaultWhom = "World"
        return S_OK()

    def initialize(self):
        """ This method initializes each HelloHandler instance called by a client"""

        self.requestDefaultWhom = self.srv_getCSOption( "DefaultWhom", HelloHandler.defaultWhom )

    auth_sayHello = [ 'all' ] #Here, 'all' the clients can call this method
    types_sayHello = [ types.StringTypes ]#Must be defined for each method

    def export_sayHello( self, whom ):
        """ Says hello to somebody"""

        if not whom:
            whom = self.requestDefaultWhom
        return S_OK( "Hello " + whom )
