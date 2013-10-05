import itertools
import random
import sys
import math


# n choose r function
def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

#Set = set(itertools.permutations(range(6), 4))
NUM_PLACES = int(raw_input("Enter number of places: \n"))
NUM_COLORS = int(raw_input("Enter number of numbers: \n"))

guess = list()
i = 0
while i < int(NUM_PLACES):
    new = random.randint(0, NUM_COLORS)
    if new not in guess:
        guess.append(new)
        i += 1
print "Try: "
print guess

CORRECT_VAL = int(raw_input("Enter number of correct values, wrong place: \n"))
CORRECT_BOTH = int(raw_input("Enter number of correct values in the correct place: \n"))

Set = (itertools.permutations(range(NUM_COLORS), NUM_PLACES))
size = nCr(NUM_COLORS, NUM_PLACES)
print size
range = range(NUM_COLORS)
    
while CORRECT_BOTH != NUM_PLACES:
    # Set generation
    range = (x for x in range and guess)    
    guessSet = set(itertools.permutations(range, CORRECT_VAL))
    solutionSpace = list()
    
    for i in xrange(size):
        setCompare = set(Set.next())
        if len([a for a in guessSet if set(a).issubset(setCompare)]) != 0:
            solutionSpace.append(setCompare)
        if i%1000 == 0:
            print i    
     
    print len(solutionSpace)  
    print solutionSpace             
    CORRECT_VAL = int(raw_input("Enter number of correct values, wrong place: \n"))
    CORRECT_BOTH = int(raw_input("Enter number of correct values in the correct place: \n"))
sys.exit()