#!/usr/local/bin/python
# -*-coding:utf-8 -*

###############################################################################
#                            plotBuilder.py                                   #
###############################################################################
"""This script builds the plots and saves them in files. Here, many lines can
   be commented or uncommented, depending on the plots we need."""

 #importing the libraries
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import pylab
#from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})

def getListFromFile(fileName):
    """This function reads a list of values stored in a file, and makes
    a list of floats out of it. Then, we will be able to use this list
    of floats to build plots."""
    with open(fileName, "r") as myFile:
        L = []
        myLine = myFile.read() #We read the list stored in the file
        L = myLine.split(";") #We parse the list
        del L[-1] #We get rid of the last element (which is a carriage return most often)

        for i in range(10):
            L[i] = float(L[i]) #Every element of the list is cast into a float
    return L

if __name__ == "__main__":

    #This list is our abscissa axis.
    #We adjust the list acording to the number of measure we made
    L = range(1,11,1)

    #We get our lists of measures from the files
    JSON = getListFromFile("/home/florent/Desktop/desktop/JSON_BigDicoFib1_1thread.txt")
    DEncode = getListFromFile("/home/florent/Desktop/desktop/DEncode_bigDicoFib1_1thread.txt")

    print "All graphs acquired..."

    #We build the plot, with the options we want (style, color, ...)
    line1 = plt.plot (L, DEncode, linestyle = 'solid', marker = "o", color = "k", label = "DISET w/ DEncode(1 thread)")
    line2 = plt.plot (L, JSON, linestyle = 'solid', marker = "o", color = "r", label = "DISET w/ JSON(1 thread)")
    #line3 = plt.plot (L, processList, linestyle = 'solid', marker = "^", color = "k", label = "xmlrpc process server")
    #line4 = plt.plot (L, DISETList_1Thread, linestyle = 'solid', marker = "s", color = "r", label = "DISET w/ DEncode(1 thread)")
    #line5 = plt.plot (L, JSON_list_1Thread, linestyle = 'solid', marker = "o", color = "b", label = "DISET w/ JSON(1 thread)")
    #line6 = plt.plot (L, DISETList_5Threads, linestyle = 'solid', marker = "s", color = "g", label = "DISET ( no SSL, 5 threads)")
    #line5 = plt.plot (L, DISETList_15Thread, linestyle = 'solid', marker = "o", color = "k", label = "DISET ( no SSL, 15 threads)")

    print "All lines created"

    #We draw the axis and the legend
    plt.xlabel('Number of client threads')
    plt.ylabel('Time taken to process all the requests (sec)')
    myLegend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.tight_layout()

    #We store the plot in a file
    pylab.savefig('/home/florent/Desktop/desktop/DEncode_vs_JSON_bigDicoFib1.png', bbox_extra_artists=(myLegend,), bbox_inches='tight')
    print "graph stored"
