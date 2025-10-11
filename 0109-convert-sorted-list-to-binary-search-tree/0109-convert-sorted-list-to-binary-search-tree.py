# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def middle(root):
            prev = None
            slow,fast = root,root
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return (slow,prev)
        
        def display(root):
            while root:
                print(root.val,end='->')
                root = root.next
            print('-------------------')
        def build(node):
            if not node:
                return node
            if node.next is None:
                return TreeNode(node.val)
            mid,prev = middle(node)
            # print(mid.val)
            # if prev:
            #     print(prev.val)
            #display(node)
            t = TreeNode(mid.val)
            if prev:
                prev.next = None
            t.left = build(node)
            t.right = build(mid.next)
            return t
        return build(head)

