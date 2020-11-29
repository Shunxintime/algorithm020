#Directly
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        final = list()

        def preorder(root: TreeNode):
            if not root:
                return
            final.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return final