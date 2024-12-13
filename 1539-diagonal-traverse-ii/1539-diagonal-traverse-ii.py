class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sorter=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                sorter.append((i+j,-i,nums[i][j]))
        print(sorter)
        sorter.sort(key=lambda x:(x[0],x[1]))
        print(sorter)
        result=[i for _,_,i in sorter]
        print(result)
        return result