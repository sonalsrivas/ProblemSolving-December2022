# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left==root.right==None:
            return root.val
        leftVal=self.evaluateTree(root.left)
        rightVal=self.evaluateTree(root.right)
        return leftVal | rightVal if root.val==2 else leftVal & rightVal 