import time
import sys
import datetime
from pause import pause

if __name__ == "__main__":
    print("DO NOT RUN THIS SCRIPT! IT DOES NOTHING")
    pause()
else:

    def realtime():
        while True:
            rtime = time.strftime("%H:%M:%S")
            print("The time is: {0} PM EST".format(rtime), end="\r")
            time.sleep(1)



    def stopwatch():
        start = time.time()
        time.clock()
        elapsed = 0
        while True:
            elapsed = time.time() - start
            print ("Time elapsed: ", round(elapsed), end="\r")
            time.sleep(0.1)

    def timerfunc(seconds):
            start = time.time()
            time.clock()
            elapsed = seconds
            while elapsed > 0:
                elapsed = start - time.time()
                print ("Time elapsed: ", round(elapsed), end="\r")
                time.sleep(0.1)
