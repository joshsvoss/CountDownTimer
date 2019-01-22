#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

# TimeLeft Object

import datetime

class TimeLeft:
    """This object implements the time between now and some datetime in the
        future, for example: a test date, flight, or birthday."""
    innerTimeDate = datetime.datetime(2019, 3, 17, 9)


    # Constructor method:
    def __init__(self):
        print
        

    def printSomething(self):
        print "something"





# This is the "main" method:
instance = TimeLeft()
instance.printSomething()
    
