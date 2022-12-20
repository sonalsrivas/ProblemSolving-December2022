class StringIterator:

    def __init__(self, compressedString: str):
        self.string=compressedString
        self.len=len(compressedString)
        self.pointer=0
        self.character=''
        self.frequency=0
        self.processForPointer()

    def processForPointer(self):
        if self.pointer >= self.len:
            self.character=' '
            return 
        self.character=self.string[self.pointer]
        self.pointer+=1
        self.frequency=0
        while self.pointer < self.len and self.string[self.pointer].isdigit():
            self.frequency*=10
            self.frequency+=int(self.string[self.pointer])
            self.pointer+=1
        print(self.pointer)
        
    def next(self) -> str:
        nextCharToReturn = self.character
        self.frequency -= 1
        if self.frequency==0:
            #self.pointer+=1
            self.processForPointer()
        return nextCharToReturn

    def hasNext(self) -> bool:
        return self.pointer < self.len or self.character!=' '


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()