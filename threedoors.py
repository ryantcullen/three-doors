import numpy as np
import math

# tracks how many times switching was the correct move to make
numCorrect = 0

# the number of trials to run the experiment
trials = 10000

for i in range(trials):

    # list of doors
    doorz = [0, 0, 0]
    
    # randomize the user's initial choice
    choiceIndex = np.random.randint(0,3)
    # random index to represent the door with the car behind it
    carIndex = np.random.randint(0,3)

    # set list element with the car to 1
    doorz[carIndex] = 1

    #handle elimination of one of the doors and then switching
    for i in range(len(doorz)):
        if doorz[i] == 0:
            if i != choiceIndex:
                doorz.pop(i)

                if doorz[0] == 1:
                    carIndex = 0
                else:
                    carIndex = 1


                if choiceIndex == 2:
                    choiceIndex = 0
                elif choiceIndex == 1:
                    if i == 2:
                        choiceIndex = 0
                    elif i == 0:
                        choiceIndex = 1
                else:
                    choiceIndex = 1
                break
        

    if choiceIndex == carIndex:
        # if switching was successful, increment numCorrect
        numCorrect += 1

# calculate the precentage of successful switches to total trials
precentCorrect = numCorrect/trials

# display result
print(precentCorrect)
    
    
    

