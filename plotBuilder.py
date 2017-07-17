#!/usr/local/bin/python
# -*-coding:utf-8 -*

###############################################################################
#                            plotBuilder.py                                   #
###############################################################################
"""We can modify and run this script to construct all the plots we need"""

import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import pylab

#from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})

def getListFromFile(fileName):
    """This function reads a list of values stored in a file, and makes
    a list of floats out of it. Then, we will be able to use this list
    of floats to build plots"""
    with open(fileName, "r") as myFile:
        L = []
        myLine = myFile.read() #We read the list stored in the file
        L = myLine.split(";") #We parse the list
        del L[-1] #We get rid of the last element (which is a carriage return most often)

        for i in range(9):
            L[i] = float(L[i]) #Every element of the list is cast into a float
    return L

if __name__ == "__main__":

    JSON_list_1Thread = []
    DISETList_1Thread = []
    threadList = []
    processList = []
    basicList = []

    #This list is our abscissa axis
    L = range(1,10,1) #We adjust the list acording to the number of measure we made

    #We get our lists of measures from the files, and comment the ones we do not need
    JSON_list_1Thread = getListFromFile("valuesLists/JSON_smallDicoFib30_1thread.txt")
    DISETList_1Thread = getListFromFile("valuesLists/DISETSmallDicoFib30_1Thread.txt")
    basicList = getListFromFile("valuesLists/basicServerSmallDicoFib30.txt")
    threadList = getListFromFile("valuesLists/threadServerSmallDicoFib30.txt")
    processList = getListFromFile("valuesLists/processServerSmallDicoFib30.txt")

    print "All graphs acquired..."

    #We build the plot, with the options we want (style, color...)
    line1 = plt.plot (L, basicList, linestyle = 'solid', marker = "o", color = "k", label = "xmlrpc basic server")
    line2 = plt.plot (L, threadList, linestyle = 'solid', marker = "s", color = "k", label = "xmlrpc thread server")
    line3 = plt.plot (L, processList, linestyle = 'solid', marker = "^", color = "k", label = "xmlrpc process server")
    line4 = plt.plot (L, DISETList_1Thread, linestyle = 'solid', marker = "s", color = "r", label = "DISET w/ DEncode(1 thread)")
    line5 = plt.plot (L, JSON_list_1Thread, linestyle = 'solid', marker = "o", color = "b", label = "DISET w/ JSON(1 thread)")

    print "All lines created"

#    line6 = plt.plot (L, DISETList_5Threads, linestyle = 'solid', marker = "s", color = "g", label = "DISET ( no SSL, 5 threads)")
#    line5 = plt.plot (L, DISETList_15Thread, linestyle = 'solid', marker = "o", color = "k", label = "DISET ( no SSL, 15 threads)")
    plt.xlabel('Number of client threads')
    plt.ylabel('Time taken to process all the requests (sec)')
    myLegend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.tight_layout()

    #We store the plot in a file
    pylab.savefig('plots/noSSL/smallDicoFib30/xmlrpc_vs_DEncode_vs_JSON_smallDicoFib30.png', bbox_extra_artists=(myLegend,), bbox_inches='tight')
    print "graph stored"
