class DynamicArray:
    arr = []
    size = 0
    capacity = 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        if i >= 0 and i < self.size:
            return self.arr[i]
        return -1

    def set(self, i: int, n: int) -> None:
        if i >= 0:
            if i < self.size:
                self.arr[i] = n
            elif i == self.size:
                if i == self.capacity:
                    self.resize()
                self.arr[i] = n
                self.size += 1

    def pushback(self, n: int) -> None:
        self.set(self.size, n)

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        newCapacity = self.size * 2
        tempArray = [0] * newCapacity
        
        tempArray[:self.size] = self.arr
        self.arr = tempArray
        self.capacity = newCapacity


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity