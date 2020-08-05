# Write your solution here
def sumarray(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(sumarray([6,9,5,6,9]))