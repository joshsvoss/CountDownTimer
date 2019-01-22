#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

# TimeLeft Object

import datetime
import time

class TimeLeft:
    """This object implements the time between now and some datetime in the
        future, for example: a test date, flight, or birthday."""
    #TODO: do fields not go here to be declared, before they're initialized
    # in the constructor?

    # Constructor method:
    def __init__(self):
        self.futureDateTime = datetime.datetime(2019, 3, 17, 9)
        self.currentDateTime = datetime.datetime.today()
        self.timeLeft = self.futureDateTime - self.currentDateTime
        

    def updateTimeLeft(self):
        self.currentDateTime = datetime.datetime.today()
        self.timeLeft = self.futureDateTime - self.currentDateTime

    def printTimeDelta(self):
        print self.timeLeft
        





# "main" method
instance = TimeLeft()
instance.printTimeDelta()
# for loop:
for i in range(10):
    instance.updateTimeLeft()
    instance.printTimeDelta()
    time.sleep(1)
    
