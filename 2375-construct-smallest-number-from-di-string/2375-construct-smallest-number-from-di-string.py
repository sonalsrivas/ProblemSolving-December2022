class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern+=pattern[-1]
        n=len(pattern)
        numList=[0]*n
        digit=1
        i=0
        while i<n:
            while pattern[i]!='I':
                i+=1
                if i==n:
                    break
            else:
                # now i must be 'I'
                numList[i]=digit
                digit+=1
            # now fill all if had any 'D's before
            j=i-1
            while j>-1 and pattern[j]=='D':
                numList[j]=digit
                digit+=1
                j-=1
            i+=1
        
            
        return ''.join(map(str,numList))
'''
"III D I DDD"

"123 5 4 987 6"


II D II DD I
12 4 35 87 6 9

12 6 34 87 5 9
'''