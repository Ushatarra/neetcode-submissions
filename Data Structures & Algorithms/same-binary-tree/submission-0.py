# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_equal(p1,q1):

            if q1 is None and p1 is None:
                return True
            
            if q1 is None:
                return False
            
            if p1 is None:
                return False
            
            if p1.val != q1.val:
                return False

            return (is_equal(p1.left,q1.left) and is_equal(p1.right,q1.right))
            
        return is_equal(p,q)
            


            

            
            

        