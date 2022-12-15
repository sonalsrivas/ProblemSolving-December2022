class FrontMiddleBackQueue:

    def __init__(self):
        self.q=[]
        self.size=0

    def pushFront(self, val: int) -> None:
        self.q.insert(0,val)
        self.size+=1

    def pushMiddle(self, val: int) -> None:
        self.q.insert(self.size//2, val)
        self.size+=1

    def pushBack(self, val: int) -> None:
        self.q.append(val)
        self.size+=1

    def popFront(self) -> int:
        if self.size<=0:
            return -1
        self.size-=1
        return self.q.pop(0)

    def popMiddle(self) -> int:
        if self.size<=0:
            return -1
        self.size-=1
        return self.q.pop(self.size//2)

    def popBack(self) -> int:
        if self.size<=0:
            return -1
        self.size-=1
        return self.q.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()