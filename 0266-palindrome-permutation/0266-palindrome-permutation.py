class Solution:
    def canPermutePalindrome(self, string: str) -> bool:
        n=len(string)
        
        mapCharParity=defaultdict(int)
        for char in string:
            mapCharParity[char]^=1
        
        noEvens=0
        noOdds=0
        
        for char,parity in mapCharParity.items():
            if parity==0:
                noEvens+=1
            else:
                noOdds+=1
        print(noOdds, noEvens,n//2)
        if n%2==0:
            return noOdds==0# and noEvens==n//2
        
        return noOdds==1 #and noEvens==n//2