class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # make a mote of the no of incoming edges to each node. 
        # and if that number is zero then it is part of the smallest set.
        smallestSet={node for node in range(n)}
        for u,v in edges:    
            smallestSet.discard(v)
        
        return smallestSet