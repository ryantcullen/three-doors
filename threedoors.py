import numpy as np
import math

numCorrect = 0
trials = 10000

for i in range(trials):

    doorz = [0, 0, 0]

    choiceIndex = np.random.randint(0,3)
    carIndex = np.random.randint(0,3)

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
        numCorrect += 1

precentCorrect = numCorrect/trials

print(precentCorrect)
    
    
    

