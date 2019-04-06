import random
import string
#These are modules, basically other scripts that this script is dependant on!

#Next is functions. Functions can run multiple things when called upon!


def randomLetter():
    print(random.choice(string.ascii_letters))
    print(20 + 20)
    x = 5
    print(x*2)
    
randomLetter() #This calls the function making it run everything in it!
