# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkChild(self, root, low, high):
        sum = 0
        if root == None:
            #print('No root')
            return sum
        if root.val >= low and root.val <= high:
            sum = (root.val + self.checkChild(root.left, low, high) + self.checkChild(root.right, low, high))
            #print(root.val, 'in range', sum)
            
        elif root.val > high:
            #print(root.val, 'too high')
            sum = self.checkChild(root.left, low, high)
        else:
            #print(root.val, 'too low')
            sum = self.checkChild(root.right, low, high)
        
        return sum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        if null return
        if im in the range, add my value and check both my children
        elif im higher, check my left child
        else check my right child
        """
        
        sum = self.checkChild(root, low, high)
        return sum

    
        