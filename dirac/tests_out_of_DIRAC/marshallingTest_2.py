#!/usr/bin/python
import time

import DEncode
import extendedJSON

def run():
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

start = time.time()
for N in range(1000):
    print "started client no {}".format(N)
    run()
    print "ended client no {}".format(N)
end = time.time()
amountOfTime = end-start #This is the amount of time taken to process all the requests of the clients
print "amount of seconds taken: {}".format(amountOfTime)
