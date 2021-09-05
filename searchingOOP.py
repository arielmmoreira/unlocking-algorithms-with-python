import random, time

class Array():
    
    def __init__(self, array):
        self.array = array[:]
        self.length = len(self.array)

    def shuffle(self):
        random.shuffle(self.array)
        print("Array shuffled: ", self.array)

    def linearSearch(self, x):
        startTime = time.time()
        answer = "Number not found!"

        for i in range(self.length):
            if self.array[i] == x:
                answer = f"Number found at position: {i}"

        clock = "Time of linear search: {:.10f}".format(time.time() - startTime) 
        print(clock)
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
        return array.recursiveLinearSearch(x, i + 1)    

    def __repr__(self):
        output = ""
        for element in self.array:
            output += str(element) + " "
        return output