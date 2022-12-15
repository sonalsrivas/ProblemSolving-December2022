class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[]
        self.k=k
        self.occupied=0

    def insertFront(self, value: int) -> bool:
        if self.occupied>=self.k:
            return False
        self.deque.insert(0,value)
        self.occupied+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.occupied>=self.k:
            return False
        self.deque.append(value)
        self.occupied+=1
        return True

    def deleteFront(self) -> bool:
        if self.occupied<=0:
            return False
        self.deque.pop(0)
        self.occupied-=1
        return True

    def deleteLast(self) -> bool:
        if self.occupied<=0:
            return False
        self.deque.pop()
        self.occupied-=1
        return True

    def getFront(self) -> int:
        return self.deque[0] if self.deque else -1

    def getRear(self) -> int:
        return self.deque[-1] if self.deque else -1

    def isEmpty(self) -> bool:
        return self.occupied<=0

    def isFull(self) -> bool:
        return self.occupied>=self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()