class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        nb=0
        for i in b:
            nb*=10
            nb+=i
        b=nb
        
        def _pow(number, power, mod):
            if power==0:
                return 1
            halfPow=pow(number, int(power/2),mod)
            if power%2==0:
                return (halfPow*halfPow)%mod
            if power>0:
                return ((halfPow*halfPow)%mod)*number
            return ((halfPow*halfPow)%mod)/number
        return pow(a,b,1337)
        
        return 0