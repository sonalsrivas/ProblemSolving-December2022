class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        n=len(s)
        indexToDelete=set()
        for i in range(n):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if not stack:
                    indexToDelete.add(i)
                else:
                    stack.pop()
        for remainingOpens in stack:
            indexToDelete.add(remainingOpens)
        result=''
        for i in range(n):
            if i in indexToDelete:
                continue
            result+=s[i]
        return result
        
'''
0123456789 10 11 12
le(e(t(c)o d   e  )
       ^
   (6
   (4
   (2
   if char == ')' and stack is empty ---- then delete char index
   
'''