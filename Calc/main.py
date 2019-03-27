from calc import *
import os

# Actual script
if option in array:
    x = float(input("Set the first number: "))
    y = float(input("Set the second number: "))
    print("The answer is:")
    if option == array[0]:
        add(x,y)
    if option == array[1]:
        subtract(x,y)
    if option == array[2]:
        multiply(x,y)
    if option == array[3]:
        divide(x,y)
else:
    print(error + " " + errorType)
    os.system('pause')
