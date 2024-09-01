class Solution:
    def mjoin(self,arr,l,mid,h):
        left=arr[l:mid+1]
        right=arr[mid+1:h+1]
        i,j=0,0
        k=l
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1
    def merge_sort(self,nums,l,h):
        if l<h:
            mid=(l+h)//2
            self.merge_sort(nums,l,mid)
            self.merge_sort(nums,mid+1,h)
            self.mjoin(nums,l,mid,h)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums,0,len(nums)-1)
        return nums

        