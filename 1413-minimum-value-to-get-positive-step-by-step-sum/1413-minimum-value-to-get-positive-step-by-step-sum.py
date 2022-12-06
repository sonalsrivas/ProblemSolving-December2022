class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minPositive=1
        currentSum=1
        for num in nums:
            newNum=currentSum+num
            if newNum<1:
                diff=1-newNum
                minPositive+=diff
                currentSum=1
            else:
                currentSum=newNum
        return minPositive
'''
sV=0
[-3,2,-3,4,2]
 0+-3 =-3 if sV+current<=0 then sV=max(sV,-(sV+current)) +1
sV=4
  1 3 0
sV=5
       
       
 -3, 2,-3,4,2
  1. 3. 1 5 7 
1 4     5


1 2
1 3
1

'''