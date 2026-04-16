class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        enum = defaultdict(list)
        for idx,num in enumerate(nums):
            enum[num].append(idx)
        print(enum)
        ans = []
        big_l = len(nums)
        def find(l,le,j):
            left,right = 0,le-1
            while left<=right:
                mid = (left+right)//2
                if l[mid] == j:
                    return mid
                elif l[mid]<j:
                    left = mid+1
                else:
                    right = mid-1
            return left
        for q in queries:
            j = q
            num_j = nums[j]
            l = enum[num_j]
            # print(l)
            le = len(l)
            # idx = l.index(j)
            idx = find(l,le,j)
            #print(j,num_j,l,idx)
            if le>1:
                left = abs(l[idx]-l[(idx-1)%le])
                right = abs(l[idx]-l[(idx+1)%le])
                wrap = -l[idx]+big_l+l[(idx-1)%le]
                wrap_2 = -l[idx]+big_l+l[(idx+1)%le]
                wrap_3 = l[idx]+big_l-l[(idx-1)%le]
                wrap_4 = l[idx]+big_l-l[(idx+1)%le]
                ans.append(min(left,right,wrap,wrap_2,wrap_3,wrap_4))
                #print('LR:',left,right,wrap,wrap_2)
                # if left<right:
                #     ans.append(left)
                # else:
                #     ans.append(right)
            else:
                ans.append(-1)
            
        return ans