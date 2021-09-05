import random

class Array():
    
    def __init__(self, array):
        self.array = array[:]

    def shuffle(self):
        random.shuffle(self.array)

    def __repr__(self):
        output = ""
        for element in self.array:
            output += str(element) + " "
        return output


array = Array([1, 2, 3, 4, 5, 6])

print(array)