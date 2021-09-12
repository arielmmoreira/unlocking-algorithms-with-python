from Search import Search
from Sort import Sort
import time, random


def main():
    arr = generateArray(1000)

    selection(arr)
    insertion(arr)
    merge(arr)
    quick(arr)
    pythonSort(arr)

    
def generateArray(size):
    return [random.randrange(size) for _ in range(size)]

def insertion(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.insertionSort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    print("Total time for insertion:", totalTime)

def selection(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.selectionSort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    print("Total time for selection sort:", totalTime)

def merge(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.mergeSort(0, len(arr) - 1)
    finalTime = time.time()
    totalTime = finalTime - startTime
    print("Total time for merge sort:", totalTime)

def quick(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.quickSort(0, len(arr) - 1)
    finalTime = time.time()
    totalTime = finalTime - startTime
    print("Total time for quick sort:", totalTime)

def pythonSort(arr):

    startTime = time.time()
    arr.sort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    print("Total time for python builti-in sort:", totalTime)

main()