import random
import string
import re
from pause import *
import secrets
import time

print("THIS SCRIPT MAKES A STRING OF ANY LENGTH THAT YOU WANT!\n")

print("Note: the amount of characters that is outputted will not exactly be the amount you plugged in. \nThis is because the script removes spaces... ")



def generate(textfile, chars):
    a = open(textfile, 'w')
    a
    p = ''.join(secrets.SystemRandom().choice(string.printable) for _ in range(chars))
    p = re.sub(r"\s+", "", p, flags=re.UNICODE)
    a.write(p)
    print("Randomize", "#" + str(count), "Successful")
    a.close()



textfile = "text.txt"  #str(input("Textfile: "))
chars = int(input("Amount of characters: "))
ref = int(input("How many times to randomize? (More is better): "))
count = 0
start_time = time.time()

while count < ref:
    generate(textfile, chars)
    count = count + 1
    
 
time_took = (time.time() - start_time)
if time_took >= 3600:
    time_took = (time_took)/60/60
    print("It took", time_took, "hours(s) to run")
    print("Randomized text", round(count/time_took), " times per minute")
    
if time_took >= 60:
    time_took = (time_took)/60
    print("It took", time_took, "minute(s) to run")
    print("Randomized text", round(count/time_took), "times per minute")
    
else:
    print("It took", (time_took), "second(s) to run")
    print("Randomized text", round(count/time_took), " times per minute")
pause()
