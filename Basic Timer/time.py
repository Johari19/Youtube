from timefunc import *
from pause import pause
options = int(input("Choose a time function: 1. Time 2. Stopwatch(1/2) "))
if options == 1:
    realtime()
if options == 2:
    stopwatch(10)
    print("Time is UP! \n")
    pause()
