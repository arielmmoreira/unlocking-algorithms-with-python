class Array():

    def __init__(self, arr):
        self.array = arr[:]
        self.length = len(self.array)

    def shuffle(self):
        import random
        random.shuffle(self.array)
        print("Array shuffled: ", self.array)

    def __repr__(self):
        output = ""
        for element in self.array:
            output += str(element) + " "
        return output

    