class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # make a mote of the no of incoming edges to each node. 
        # and if that number is zero then it is part of the smallest set.
        mapNodeIncomingedges={node:0 for node in range(n)}
        for u,v in edges:    
            mapNodeIncomingedges[v]+=1
        smallestSet=set()
        for node,noIncomingedges in mapNodeIncomingedges.items():
            if noIncomingedges == 0:
                smallestSet.add(node)
        return smallestSet