class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=len(nums)
        cur_len=1
        max_len=1
        for i in range(1,n):
            if nums[i-1] < nums[i]:
                cur_len+=1
            else:
                cur_len=1
            max_len=max(max_len, cur_len)
        return max_len