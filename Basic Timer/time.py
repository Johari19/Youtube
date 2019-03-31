from timefunc import *
from pause import pause
options = int(input("Choose a time function: 1. Time 2. Stopwatch 3. Timer (1/2/3) "))
if options == 1:
    realtime()
if options == 2:
    stopwatch()
    print("Time is UP! \n")
    pause()
if options == 3:
    seconds = 10
    timerfunc(10)
