class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ele=max(nums)
        index=float('inf')
        for i,ele in enumerate(nums):
            if max_ele==ele:
                index=i
            elif max_ele<ele*2:
                #print(ele)
                return -1
            
                
        return index