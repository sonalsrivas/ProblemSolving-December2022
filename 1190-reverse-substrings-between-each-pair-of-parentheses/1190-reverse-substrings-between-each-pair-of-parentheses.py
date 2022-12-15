class Solution:
    def reverseString(self, s):
        return s[::-1]
    
    def reverseParentheses(self, s: str) -> str:
        stack=['']
        i, n = 0, len(s)   # ((et)er)              ((
                             #    ^
        while i<n:
            # store the parenthesis openings first if any
            while i<n and s[i]=='(':
                if stack and stack[-1]=='(':
                    stack.append('')
                stack.append(s[i])
                i+=1
                
            # have the substring
            substring=''
            while i<n and s[i] not in '()':
                substring+=s[i]
                i+=1
            stack.append(substring)
            
            if i>=n or s[i]=='(':
                continue
            else:
                while i<n and s[i]==')':
                    #print(stack)
                    substring=stack.pop()
                    revSubstring = self.reverseString(substring)
                    stack.pop()
                    stack[-1] = stack[-1]+revSubstring
                    i+=1
                    while i<n and s[i] not in '()':
                        stack[-1]+=s[i]
                        i+=1
                    #if stack[-1] 
            print(stack,i)
        return stack[-1]
            
'''
((et)er)
    ^

et XX  -> te
(  XX
(
       
     
     R(R(et)+er)
     (
et  X
R('' + R(et) + er)

tu(we(oi))(kl)
        ^
oi
(
we 
(
tu
'''