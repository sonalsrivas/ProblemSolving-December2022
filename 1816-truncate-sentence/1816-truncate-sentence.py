class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=""
        for char in s:
            if char==" ":
                k-=1
                if k==0:
                    return res
            res+=char
            
                
        return res