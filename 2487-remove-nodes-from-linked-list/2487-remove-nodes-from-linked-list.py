# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def putNodeInStack(self, stackNodes, node):
        while stackNodes and stackNodes[-1].val<node.val:
            stackNodes.pop()
        stackNodes.append(node)
        
    def deleteNode(self,node, prev) : 
        if prev:
            prev.next=node.next
        
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stackNodes = [] 
        node=head
        while node:
            self.putNodeInStack(stackNodes, node)
            node=node.next
        
        stackPointer=0
        stacklen=len(stackNodes)
        
        newHead=None
        node=head 
        prev=None
        while node:
            if stackNodes[stackPointer]==node:
                stackPointer+=1
                if not newHead:
                    newHead=node
                prev=node
            else:
                self.deleteNode(node, prev) 
            node=node.next
        return newHead
'''
5 2 2 3 8
2
2
5
[5,2,13,3,8]
          ^

2 X 13>2      3 X 8>3 ... 8
5 X 13>5.... 13           13
'''