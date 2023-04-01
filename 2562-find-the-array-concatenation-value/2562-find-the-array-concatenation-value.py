class Solution:
    def findTheArrayConcVal(self, n: List[int]) -> int:
        l,r,cv =0,len(n)-1,0
        while l<r:
            cv+=self.add(n[l], n[r])
            l+=1
            r-=1
        if l==r:
            cv+=n[l]
        return cv
    def add(self, x,y):
        return int(str(x)+str(y))