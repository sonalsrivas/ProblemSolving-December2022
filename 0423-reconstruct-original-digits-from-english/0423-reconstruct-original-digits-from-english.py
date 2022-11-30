class Solution:
    def originalDigits(self, s: str) -> str:
        mapDigString={'0':['zero','z'], '1':['one','o'],'2':['two','w'],'3':['three','t'],'4':['four','u'],'5':['five','f'],'6':['six','x'],'7':['seven','s'],'8':['eight','g'],'9':['nine','i']}
        d=Counter(s)
        r=[]
        for dig in '0246813579':
            string, unique = mapDigString[dig]
            freqOfuniqueInS=d[unique]
            print(freqOfuniqueInS,d)
            r.append(dig*freqOfuniqueInS)
            for c in string:
                d[c]-=freqOfuniqueInS
            
        return ''.join(sorted(r))