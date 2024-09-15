#What I have doen is to do a binary search for rows then coumn,we can optimise this code!
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start,end=0,len(matrix)-1
        if len(matrix)>1:
            while start<=end:
                mid=(start+end)//2
                if matrix[mid][-1]==target:
                    return True
                elif matrix[mid][-1]<target:
                    start=mid+1
                else:
                    end=mid-1
        if start>=len(matrix) or target<matrix[start][0]:
            return False
        index=start 
        print(index)
        start,end=0,len(matrix[index])-1
        while start<=end:
            mid=(start+end)//2
            if matrix[index][mid]==target:
                return True
            elif matrix[index][mid]<target:
                start=mid+1
            else:
                end=mid-1
        return False

            

        
