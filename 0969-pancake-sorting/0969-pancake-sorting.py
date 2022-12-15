class Solution:
    def shiftBackMax(self, arr, mapIndex, maxInt, maxIndex, desiredPosition, resultArr):
        arr, mapIndex=self.flipFirstK(arr, mapIndex, maxIndex+1)
        arr, mapIndex=self.flipFirstK(arr, mapIndex, desiredPosition+1)
        resultArr.append(maxIndex+1)
        resultArr.append(desiredPosition+1)
        
        return arr, resultArr, mapIndex
        
    def flipFirstK(self, arr, mapIndex, k):
        for i in range(k//2):
            arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
            mapIndex[arr[i]]=i
            mapIndex[arr[k-i-1]]=k-i-1
            
        return arr, mapIndex
    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        resultArr=[]
        mapIndex={arr[i]:i for i in range(n)}
        for num in range(n, 0, -1):
            arr, resultArr, mapIndex=self.shiftBackMax(arr, mapIndex, num, mapIndex[num], num-1, resultArr)
        return resultArr
        
'''

arr = 
[3, 2, 4, 1]
 4 2 3 1     3
 1 3 2 4    4
 2 3 1 4    3
 3 2 1 4    2
 1 2 3 4    3
 
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4]

'''