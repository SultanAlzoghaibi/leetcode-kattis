class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0

    
        def dfs(treeNode):
            if not treeNode:
                return 0
            
            left = dfs(treeNode.left)
            right = dfs(treeNode.right)

            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        dfs(root)

        return self.ans