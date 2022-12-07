class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        integerPart, remainder = divmod(abs(numerator), abs(denominator))
        resultFraction = [('-' if  numerator*denominator<0 else '' )+str(integerPart), '.']
        mapRemainderIndex = dict()
        
        lenResultFraction = 2
        while remainder>0 and remainder not in mapRemainderIndex:
            mapRemainderIndex[remainder]=lenResultFraction
            quotient, remainder = divmod(remainder*10, abs(denominator))
            resultFraction.append(str(quotient))
            lenResultFraction+=1
        
        if remainder in mapRemainderIndex:
            indexOfOcc = mapRemainderIndex[remainder]
            resultFraction.insert(indexOfOcc, '(')
            resultFraction.append(')')
        
        return ''.join(resultFraction).rstrip('.')