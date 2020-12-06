class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])
        indx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:indx+1],inorder[:indx])
        root.right = self.buildTree(preorder[indx+1:],inorder[indx+1:])
        return root
    #仿写于精选