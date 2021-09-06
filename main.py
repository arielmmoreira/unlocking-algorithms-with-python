from Search import Search
from Sort import Sort
import time, random

def main():
    arr = generateArray(1000)
    searchArray = Search(arr)
    sortArray = Sort(arr)
    
    startTime = time.time()

    sortArray.insertionSort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    print("Total time:", totalTime)





def generateArray(size):
    return [random.randrange(size) for _ in range(size)]


main()