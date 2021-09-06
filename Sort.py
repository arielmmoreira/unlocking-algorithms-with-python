from Array import Array

class Sort(Array):

    def selectionSort(self, ascending=True):
        if ascending:
            for i in range(self.length - 1):
                smallest = i
                for j in range(i + 1, self.length):
                    if self.array[j] < self.array[smallest]:
                        smallest = j
                tmp = self.array[i]
                self.array[i] = self.array[smallest]
                self.array[smallest] = tmp           
        else:
            for i in range(self.length - 1, -1, -1):
                smallest = i
                for j in range(i - 1, -1, -1):
                    if self.array[j] < self.array[smallest]:
                        smallest = j
                tmp = self.array[i]
                self.array[i] = self.array[smallest]
                self.array[smallest] = tmp

    def insertionSort(self):
        for i in range(1, self.length):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key


    def mergeSort(self, p, r):
        """
        p: index of first element
        r: index of last element
        """
        if p >= r:
            return
        else:
            q = (p + r) // 2
            self.mergeSort(p, q)
            self.mergeSort(q + 1, r)
            self.merge(p, q, r)


    def merge(self, p, q, r):
        """
        p: index of the first element of the array
        q: index of half of the array
        r: index of the last element of the array
        """
        import math
        copy1 = self.array[p:q + 1]
        copy2 = self.array[q + 1:r + 1]  
        copy1.append(math.inf)
        copy2.append(math.inf)

        i = 0
        j = 0
        for k in range(p, r + 1):
            if copy1[i] <= copy2[j]:
                self.array[k] = copy1[i]
                i += 1
            else:
                self.array[k] = copy2[j]
                j += 1

    def quickSort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self.quickSort(p, q - 1)
            self.quickSort(q + 1, r)
        

    def partition(self, p, r):
        q = p
        for u in range(p, r):
            if self.array[u] <= self.array[r]:
                tmp = self.array[q]
                self.array[q] = self.array[u]
                self.array[u] = tmp
                q += 1
        tmp = self.array[q]
        self.array[q] = self.array[r]
        self.array[r] = tmp
        return q
            

    def __repr__(self):
        output = ""
        for element in self.array:
            output += str(element) + " "
        return output