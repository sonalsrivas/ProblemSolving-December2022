from bisect import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ln=len(nums)
        kwindow, result = nums[:k], []
        
        def calculateMedian(odd):
            return (kwindow[k//2]+kwindow[k//2-1])/2. if not odd else kwindow[(k-1)//2]*1.0
        
        kwindow.sort()
        odd = k%2
        for i in range(k,ln):
            result.append(calculateMedian(odd))
            kwindow.remove(nums[i-k])#pop(bisect(kwindow, nums[i-k])-1)  # <<< bisect is faster than .remove()
            insort(kwindow, nums[i])
            
        result.append(calculateMedian(odd))
        return result