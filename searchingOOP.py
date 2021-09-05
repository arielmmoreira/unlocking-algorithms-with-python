import random

class Array():
    
    def __init__(self, array):
        self.array = array[:]
        self.length = len(self.array)

    def shuffle(self):
        random.shuffle(self.array)
        print("Array shuffled: ", self.array)

    def linearSearch(self, x):
        answer = "Number not found!"

        for i in range(self.length):
            if self.array[i] == x:
                answer = f"Number found at position: {i}"

        print("Iterations:", self.length)
        return answer

    def betterLinearSearch(self, x):
        iterations = 0
        for i in range(self.length):
            if self.array[i] == x:
                iterations += 1
                print(f"Iterations: {iterations}")
                return "Number at found at position: " + str(i)
        return "Number not found"

    def sentinelLinearSearch(self, x):
        self.array.append(x)
        i = 0
        while self.array[i] != x:
            i += 1

        self.array.pop()
        if i < self.length or self.array[self.length - 1] == x:
            print(f"Iterations: {i + 1}")
            return f"Number found at position: {i}"
        return "Number not found!"

    def recursiveLinearSearch(self, x, i=0):
        if i > self.length:
            return "Number not found"
        if self.array[i] == x:
            print(f"Iterations: {i + 1}")
            return f"Number found at position: {i}"
        return self.recursiveLinearSearch(x, i + 1)

    def binarySearch(self, x):
        self.array.sort()
        print("Array sorted:", self.array)
        p = 0
        r = self.length - 1
        iterations = 1
        while p <= r:
            q = (p + r) // 2
            if self.array[q] == x:
                print(f"Iterations: {iterations}")
                return f"Number found at position {q}"
            if self.array[q] > x:
                r = q - 1
            elif self.array[q] < x:
                p = q + 1
            iterations += 1
        return "Number not found!"
        

    def __repr__(self):
        output = ""
        for element in self.array:
            output += str(element) + " "
        return output
