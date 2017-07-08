import os
import time
import sys

DRIVE = "/dev/cdrom" #setting the target drive

def ejectDisk():
        startTime = int(round(time.time() * 1000)) #gets the initial time

        print("Checking " + DRIVE)

        os.system("/usr/bin/eject " + DRIVE) #open the tray
        endTime = int(round(time.time() * 1000)) #gets the final time
        if (endTime - startTime) <= 500: #opening the drive will take less that 500ms
                os.system("/usr/bin/eject -t " + DRIVE) #close the tray
                print("Closed CD Tray")
                return False
        else:
                print("Opened CD Tray")
                return True
ejectDisk()
#DEBUGING INFO
#print("Start time was " + str(startTime))
#print("End time was   " + str(endTime))
