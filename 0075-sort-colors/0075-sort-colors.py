class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zc=arr.count(0)
        zo=arr.count(1)
        zt=arr.count(2)
        i=0
        
        for j in range(zc):
            arr[i]=0
            i=i+1
        
        for j in range(zo):
            arr[i]=1
            i=i+1
        
        for j in range(zt):
            arr[i]=2
            i=i+1

        
        
        