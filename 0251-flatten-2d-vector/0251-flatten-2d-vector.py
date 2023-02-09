class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.inner=0
        self.outer=0
        self.veclength=len(self.vec)

    def neutralize(self):
        while self.outer< self.veclength and self.inner == len(self.vec[self.outer]):   # if currently pointed element is a list type then dig in.
            self.outer+=1
            self.inner=0
        
    def next(self) -> int:
        # The assumption here would be that the pointer always points to the fresh number (after neutralization)
        self.neutralize()
        nextElement=self.vec[self.outer][self.inner]
        self.inner+=1
        return nextElement

    def hasNext(self) -> bool:
        self.neutralize()
        return self.outer < len(self.vec)
        


'''
[
    [ - 0
        [ - 0 
            1, 2
        ], [3], [4]
    ]
]

[ 
    1, 3, [5,2] 
]


'''