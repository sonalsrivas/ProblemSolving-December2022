class Solution:
    def mergeArrays(self, n1: List[List[int]], n2: List[List[int]]) -> List[List[int]]:
        p1, p2, l1,l2 = 0,0,len(n1),len(n2)
        res=[]
        while p1< l1 and p2<l2:
            if n1[p1][0] == n2[p2][0]:
                res.append([n1[p1][0], n1[p1][1]+n2[p2][1]])
                p1+=1
                p2+=1
            elif n1[p1][0]<n2[p2][0]:
                res.append(n1[p1])
                p1+=1
            elif n1[p1][0]>n2[p2][0]:
                res.append(n2[p2])
                p2+=1
        while p1< l1:
            res.append(n1[p1])
            p1+=1
        
        while p2<l2:
            res.append(n2[p2])
            p2+=1
        return res