class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
 
class Solution:
    def searchBST(self, root: 'TreeNode', val: int) -> 'TreeNode':
        simdiki = root
 
        while simdiki is not None:
            if val == simdiki.val:
                return simdiki
            elif val < simdiki.val:
                simdiki = simdiki.left
            else:
                simdiki = simdiki.right
 
        return None
 
