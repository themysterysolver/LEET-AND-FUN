# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        inorderA=[]
        preorderA=[]
        def inorder(root):
            if root:
                inorder(root.left)
                inorderA.append(root.val)
                inorder(root.right)
        def preorder(root):
            if root:
                preorderA.append(root.val)
                preorder(root.left)
                preorder(root.right)
        inorder(root)
        preorder(root)
        encode=""
        print(inorderA,preorderA)
        str1='.'.join(map(str,inorderA))
        str2='.'.join(map(str,preorderA))
        encode=str1+'-'+str2
        return encode
        
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        print(data)
        if data=='-':
            return []
        #print(data)
        idx=data.index('-')
        inorder=list(map(int,data[:idx].split('.')))
        preorder=list(map(int,data[idx+1:].split('.')))
        print('at derserialize:',inorder,preorder)
        mapi={val:idx for idx,val in enumerate(inorder)}
        preorderIdx=[0]
        def helper(left,right):
            if left>right:
                return
            value=preorder[preorderIdx[0]]
            preorderIdx[0]+=1
            newNode=TreeNode(value)
            idx=mapi[value]
            newNode.left=helper(left,idx-1)
            newNode.right=helper(idx+1,right)
            return newNode
        return helper(0,len(inorder)-1)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans