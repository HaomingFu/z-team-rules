class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
        startIn, startPost = 0, 0
        inEnd = postEnd = len(inorder)-1
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        return buildBinaryTree(inorder, postorder, startIn, inEnd, startPost, postEnd, dic)

def buildBinaryTree(inorder, postorder, inStart, inEnd, postStart, postEnd, dic):
    print("inStart, inEnd", inStart, inEnd)
    print("postStart, postEnd", postStart, postEnd)
    if inStart > inEnd or postStart > postEnd:
        return None
    rootVal = postorder[postEnd]
    root = TreeNode(rootVal)
    k = dic[rootVal]
    root.left = buildBinaryTree(inorder, postorder, inStart, k-1, postStart, postStart+k-1-inStart, dic)
    root.right = buildBinaryTree(inorder, postorder, k+1, inEnd, postEnd-inEnd+k, postEnd-1, dic)
    return root

print(buildTree([1,3,2], [3,2,1]))
