import os
import time
if __name__ == "__main__":
    print("DO NOT RUN THIS SCRIPT! IT DOES NOTHING")
    time.sleep(10)
else:

    # Functions
    def add(x,y):
        print(x + y)
        os.system('pause')
    def subtract(x,y):
        print(x - y)
        os.system('pause')
    def multiply(x,y):
        print(x * y)
        os.system('pause')
    def divide(x, y):
        print(x/y)
        os.system('pause')
    def printStuff(text):
        print(text)
    # Variables
    option = int(input("What operation would you like to do? 1. Add 2. Subrtract 3. Multiply 4. Divide (1/2/3/4): "))
    array = [1, 2, 3, 4]
    error = "There is an error!"
    errorType = "Choice out of range!"

