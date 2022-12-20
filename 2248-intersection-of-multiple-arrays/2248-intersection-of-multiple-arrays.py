class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        eliminateBubble=[0]*1001
        
        for lst in nums:
            for i in lst:
                eliminateBubble[i]+=1
        #print(eliminateBubble)
        return [g for g in range(1001) if eliminateBubble[g]==len(nums) ]