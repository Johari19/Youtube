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



    def stopwatch(seconds):
        start = time.time()
        time.clock()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start
            print ("Time elapsed: ", round(elapsed), end="\r")
            time.sleep(0.1)
