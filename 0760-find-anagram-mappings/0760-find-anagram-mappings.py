class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        mapNums2Ind={nums2[i]:i for i in range(n)}
        mapping=[0]*n
        for i in range(n):
            mapping[i]=mapNums2Ind[nums1[i]]
        return mapping
'''


[12,28,46,32,50]

[50,12,32,46,28]


0:

'''