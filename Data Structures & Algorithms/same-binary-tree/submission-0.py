# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        q, p = deque([p]), deque([q])
        while q and p:
            for _ in range(len(q)): 
                nodeq = q.popleft()
                nodep = p.popleft()
                if nodep is None and nodeq is None: 
                    continue 
                if nodep and nodeq and nodep.val == nodeq.val:
                    q.append(nodeq.right)
                    q.append(nodeq.left)
                    p.append(nodep.right)
                    p.append(nodep.left)
                    continue 
                return False

        return True 