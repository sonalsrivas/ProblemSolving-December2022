class Solution:
    def fractionAddition(self, expression: str) -> str:
        def segregateFraction(s):
            N,D=[],[]
            n=len(s)
            i=0
            while i<n:
                numerator=''
                while i<n and s[i]!='/':
                    numerator+=s[i]
                    i+=1
                N.append(int(numerator))
                i+=1
                denominator=''
                while i<n and s[i] not in '+-':
                    denominator+=s[i]
                    i+=1
                D.append(int(denominator))
            
            return N,D
                    
        def gcd(a,b):
            #if a<b:
            #    a,b=b,a
            if b==0:
                return a
            return gcd(b,a%b)
        
        n,d= segregateFraction(expression)
        finaln, finald=0,1
        for i in d:
            finald*=i
            
        dproductExceptSelf=d
        for i,y in enumerate(d):
            dproductExceptSelf[i]=finald//y
            n[i]*=dproductExceptSelf[i]
        
        for x in n:
            finaln+=x
        
        gcdnd=gcd(finaln, finald)
        finaln, finald = finaln//gcdnd, finald//gcdnd
        
        return str(finaln)+'/'+str(finald)