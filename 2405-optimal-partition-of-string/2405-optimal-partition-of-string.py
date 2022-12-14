class Solution:
    def partitionString(self, s: str) -> int:
        n=len(s); i=0
        minNoOfSubstrings=0
        while i<n:
            substring=set()
            while i<n and s[i] not in substring:
                substring.add(s[i])
                i+=1
    
            minNoOfSubstrings+=1
            
            #i+=1
        return minNoOfSubstrings