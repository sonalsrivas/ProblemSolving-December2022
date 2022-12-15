class Solution:
    def findxorFromXtoY(self,xorList, x,y):
        return xorList[x-1]^xorList[y] if x>0 else xorList[y]
        
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        xorList=arr[::]
        for i in range(1,n):
            xorList[i]^=xorList[i-1]
        noOfTriplets=0
        for i in range(n-1):
            for j in range(i+1, n):
                a=self.findxorFromXtoY(xorList, i,j-1)
                for k in range(j,n):
                    b=self.findxorFromXtoY(xorList, j,k)
                    if a==b:
                        noOfTriplets+=1
        return noOfTriplets
                    
'''
[2,3,1,6,7]
 
'''