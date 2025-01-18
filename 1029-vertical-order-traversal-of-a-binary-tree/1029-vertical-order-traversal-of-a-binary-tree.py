# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash=dict()
        hash[(0,0)]=[root.val]
        #print(hash)
        q=deque([(root,(0,0))])
        lvl=0
        while q:
            l=len(q)
            for i in range(l):
                r,(y,x)=q.popleft()
                if r.left:
                    q.append((r.left,(lvl+1,x-1)))
                    if (lvl+1,x-1) in hash:
                        hash[(lvl+1,x-1)].append(r.left.val)
                    else:
                        hash[(lvl+1,x-1)]=[r.left.val]
                if r.right:
                    q.append((r.right,(lvl+1,x+1)))
                    if (lvl+1,x+1) in hash:
                        hash[(lvl+1,x+1)].append(r.right.val)
                    else:
                        hash[(lvl+1,x+1)]=[r.right.val]
            lvl+=1
        #print(hash)
        hash_tags=list(hash.items())
        #print(hash_tags)
        for key,val in hash_tags:
            val.sort()
        #print(hash_tags)
        hash_tags.sort(key=lambda x:x[0][-1])
        #print(hash_tags)
        nhash=dict()
        for (key1,key2),val in hash.items():
            if key2 in nhash:
                nhash[key2].extend(val)
            else:
                nhash[key2]=val
        #print(nhash)
        nhash_tag=list(nhash.items())
        nhash_tag.sort(key=lambda x:x[0])
        #print(nhash_tag)
        result=[]
        for key,val in nhash_tag:
            result.append(val)
        return result
         
        



        
