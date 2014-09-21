import itertools
import random
import sys
import time
import math

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
                        FileTransferSpeed, FormatLabel, Percentage, \
                        ProgressBar, ReverseBar, RotatingMarker, \
                        SimpleProgress, Timer


# Memory contstraints for large problem sets. Brute forcing not realistic.

# n choose r ordered function
def lenPerm(n,r):
    f = math.factorial
    return f(n) / (f(n-r))

###############################################################################
## Generate initial sets
#		- Retrieve scope of game (range of places/numbers)
#		- Create universal set generator from input values
#		- Randomly generate initial guess
#		- Receive feedback from initial guess, create solutionSpace 
#		- Enter loop that continues while game is not complete 
#
###############################################################################
NUM_PLACES = int(raw_input("Enter number of places: \n"))
NUM_COLORS = int(raw_input("Enter number of numbers: \n"))

############################################## 
## Set generation
##############################################
Set = (itertools.permutations(range(NUM_COLORS), NUM_PLACES))
size = lenPerm(NUM_COLORS, NUM_PLACES)
print "Size of set: " + str(size)

guess = set()
i = 0

##############################################
## Generate initial guess
##############################################

while i < NUM_PLACES:
    new = random.randint(0, NUM_COLORS)
    if new not in guess:
        guess.add(new)
        i += 1
print "Try: "
print guess

CORRECT_VAL = int(raw_input("Enter number of correct values, wrong place: \n"))
CORRECT_BOTH = int(raw_input("Enter number of correct values in the correct place: \n"))

##############################################
## Generate set of values based on the guess
#		and user feedback on number correct.
#		- Will use this set later to clear
#		values from the solutionSpace that 
#		cannot be the answer.
#
##############################################

rangeNaught = range(NUM_COLORS)
range_ = set(x for x in rangeNaught and guess)    
potentialGuessSet = set(itertools.permutations(range_, CORRECT_VAL))
solutionSpace = list()

widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
            ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=int(size)).start()

i=0
while i < size:
	setCompare = Set.next()
	if len([a for a in potentialGuessSet if set(a).issubset(setCompare)]) != 0:
		solutionSpace.append(setCompare)
	i += 1
	pbar.update(i)
pbar.finish()
print solutionSpace	
print "Size of solution space: " + str(len(solutionSpace)) 


while CORRECT_VAL != NUM_PLACES:
	# determine best guess
	guess = random.sample(solutionSpace, 1)
	print "Try: " 
	print guess
	
	CORRECT_VAL = int(raw_input("Enter number of correct values, wrong place: \n"))
	CORRECT_BOTH = int(raw_input("Enter number of correct values in the correct place: \n"))
	
	range_ = set(x for x in range_ and guess)
	potentialGuessSet = set(itertools.permutations(range_, CORRECT_VAL))
	
	i = 0
	
	while i < len(solutionSpace):
		setCompare = solutionSpace[i]
		if len([a for a in potentialGuessSet if set(a).issubset(setCompare)]) == 0:
			solutionSpace.remove(setCompare)
		i += 1
		#if i%1000 == 0:
			#print i  
        	
	print solutionSpace
	print "New solution space size: \n"
	print len(solutionSpace)

sys.exit()
