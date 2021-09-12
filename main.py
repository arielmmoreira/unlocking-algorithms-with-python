from Search import Search
from Sort import Sort
import time, random


def main():
    arr = generateArray(10000)

    selectionSort = selection(arr)
    insertionSort = insertion(arr)
    mergeSort = merge(arr)
    quickSort = quick(arr)
    pythonSort = python(arr)
    print("TOTAL TIME:")
    print("Selection sort:", selectionSort)
    print("Insertion sort:", insertionSort)
    print("Merge sort:", mergeSort)
    print("Quicksort:", quickSort)
    print("Python built-in sort:", pythonSort)

    
def generateArray(size):
    return [random.randrange(size) for _ in range(size)]

def insertion(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.insertionSort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    return totalTime

def selection(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.selectionSort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    return totalTime

def merge(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.mergeSort(0, len(arr) - 1)
    finalTime = time.time()
    totalTime = finalTime - startTime
    return totalTime

def quick(arr):
    sortArray = Sort(arr)
    startTime = time.time()
    sortArray.quickSort(0, len(arr) - 1)
    finalTime = time.time()
    totalTime = finalTime - startTime
    return totalTime

def python(arr):
    startTime = time.time()
    arr.sort()
    finalTime = time.time()
    totalTime = finalTime - startTime
    return totalTime

main()