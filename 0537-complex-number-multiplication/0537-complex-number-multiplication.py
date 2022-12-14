class Solution:
    def findNums(self, num):
        real, imaginary ='',''
        i, n = 0, len(num)
        while num[i]!='+':
            real+=num[i]
            i+=1
        i+=1
        while num[i]!='i':
            imaginary+=num[i]
            i+=1
        return int(real), int(imaginary)
        
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = self.findNums(num1)
        c,d = self.findNums(num2)
        return str(a*c-b*d)+'+'+str(a*d+b*c)+'i'
'''
a+bi
c+di
(a+bi)*(c)+(di)*(a+bi)
ca+bci + adi+bdii
=> ac-bd +i(ad+bc)

"1+1i"
"1+-2i"
(1+i)(1) +(1+i)(-2i)
1+i+-2i-2ii
1+i(1-2)+-2(-1)
1+-i+2
3+-i

3+-1i
'''