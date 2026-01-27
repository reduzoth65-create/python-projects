import random
import time

def getRandomDate(startDtae,endDate):
    print("Printing random date between",startDtae,"and",endDate)
    randomGenerator= random.random()
    dateFormat='%m/%d/%Y'
    startTime= time.mktime(time.strptime(startDtae,dateFormat))
    endTime= time.mktime(time.strptime(endDate,dateFormat))

    randomTime=startTime+randomGenerator*(endTime-startTime)
    randomDate=time.strptime(dateFormat,time.localtime(randomTime))
    return randomDate

print("Random Date=",getRandomDate("1/1/2026","12/12/2027"))