class Solution:
    def gcdOfNumbers(self, a,b):
        if a<b:
            a,b=b,a
        if b==0:
            return a
        return self.gcdOfNumbers(b,a%b)
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ''
        gcdLengths=self.gcdOfNumbers(len(str1),len(str2))
        return str1[:gcdLengths]