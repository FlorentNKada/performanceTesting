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

        for i in range(10):
            L[i] = float(L[i]) #Every element of the list is cast into a float
    return L

if __name__ == "__main__":

    DISETList_1Thread = []
#    DISETList_2Threads = []
#    DISETList_5Threads = []
#    DISETList_15Thread = []
    threadList = []
    processList = []
    basicList = []

    #This list is our abscissa axis
    L = range(1,11,1) #We adjust the list acording to the number of measure we made

    #We get our lists of measures from the files, and comment the ones we do not need
    DISETList_1Thread = getListFromFile("valuesLists/DISETBigDicoFib12_1Thread.txt")
    print DISETList_1Thread
#    DISETList_2Threads = getListFromFile("valuesLists/DISETSmallDicoFib30_2Threads.txt")
#    print DISETList_2Threads
#    DISETList_5Threads = getListFromFile("valuesLists/DISETBigDicoFib1_5threads.txt")
#    print DISETList_5Threads
#    DISETList_15Threads = getListFromFile("valuesLists/DISETBigDicoFib1_15threads.txt")
#    print DISETList_15Threads
    basicList = getListFromFile("valuesLists/basicServerBigDicoFib12.txt")
    print basicList
    threadList = getListFromFile("valuesLists/threadServerBigDicoFib12.txt")
    print threadList
    processList = getListFromFile("valuesLists/processServerBigDicoFib12.txt")
    print processList

    #We build the plot, with the options we want (style, color...)
    line1 = plt.plot (L, basicList, linestyle = 'solid', marker = "o", color = "r", label = "basic server")
    line2 = plt.plot (L, threadList, linestyle = 'solid', marker = "o", color = "b", label = "thread server")
    line3 = plt.plot (L, processList, linestyle = 'solid', marker = "o", color = "c", label = "process server")
    line4 = plt.plot (L, DISETList_1Thread, linestyle = 'solid', marker = "o", color = "g", label = "DISET (no SSL, 1 thread)")
#    line5 = plt.plot (L, DISETList_15Threads, linestyle = 'solid', marker = "^", color = "g", label = "DISET ( no SSL, 15 threads)")
#    line6 = plt.plot (L, DISETList_5Threads, linestyle = 'solid', marker = "s", color = "g", label = "DISET ( no SSL, 5 threads)")
#    line5 = plt.plot (L, DISETList_15Thread, linestyle = 'solid', marker = "o", color = "k", label = "DISET ( no SSL, 15 threads)")
    plt.xlabel('Number of client threads')
    plt.ylabel('Time taken to process all the requests (sec)')
    myLegend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.tight_layout()

    #We store the plot in a file
    pylab.savefig('plots/bigDicoFib12.png', bbox_extra_artists=(myLegend,), bbox_inches='tight')
