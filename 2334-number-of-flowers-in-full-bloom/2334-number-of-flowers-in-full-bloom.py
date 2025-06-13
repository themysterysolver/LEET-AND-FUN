## very good logic DIFF ARRAY+BIN SEARCH
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        hash=SortedDict({0:0})
        for start,end in flowers:
            hash[start]=hash.get(start,0)+1
            hash[end+1]=hash.get(end+1,0)-1
        prefix=[]
        curr=0
        flower_positions=[]
        for key,val in hash.items():
            curr+=val
            flower_positions.append(key)
            prefix.append(curr)
        #print(flower_positions)
        #print(prefix)
        ans=[]
        for p in people:
            idx=bisect_right(flower_positions,p)-1
            ans.append(prefix[idx])
        return ans


'''
Here this out we will use difference array and binary search to solve this problem
If we use PURE DIFF array concept we get a MLE coz array size can go a large size
Thus we smart this with help of hahsmap,so similary we use hashmap to construct diff array and then calculate prefix array considering 0 coz in future when binary serach we don't flowers which is nto bloomed ata ll.
Then with prefix array we insert the person viisting day 's prefix array quickly with help of binary search.
'''