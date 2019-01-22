#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

# TimeLeft Object

import datetime

class TimeLeft:
    """This object implements the time between now and some datetime in the
        future, for example: a test date, flight, or birthday."""


    # Constructor method:
    def __init__(self):
        self.futureDateTime = datetime.datetime(2019, 3, 17, 9)
        self.currentDateTime = datetime.datetime.today()
        self.timeLeft = self.futureDateTime - self.currentDateTime
        
        

    def printSomething(self):
        print "something"

    def printTimeDelta(self):
        print self.timeLeft
        





# "main" method
instance = TimeLeft()
instance.printSomething()
instance.printTimeDelta()
    
