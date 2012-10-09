'''
Created on Oct 9, 2012

@author: Administrator
'''
import random

#def NetflixAccTests():
    
outFile = open('AcceptanceTests.txt', 'w')
lineCount = 0
#movieID = 1
while(lineCount < 1000):  
    numRatings = random.randint(1, 40)
    #write movie number + :
    movieID = random.randint(1, 17770)
    outFile.write(str(movieID) + ':\n')
    for i in range(numRatings):
        #write user number
        user = random.randint(1, 2649429)
        outFile.write(str(user) + '\n')
        #print 'meow'
    lineCount += numRatings + 1
    #movieID += 1
outFile.close()
    
        