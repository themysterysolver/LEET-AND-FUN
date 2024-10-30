class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        if arr[0]<arr[1]:
            isIncreasing=True
        elif arr[0]>arr[1]:
            return False
        else:
            return False
        if isIncreasing:
            peak=False
            for i in range(len(arr)-1):
                if arr[i]==arr[i+1]:
                    return False
                elif arr[i]>arr[i+1]:
                    peak=True
                if peak:
                    if arr[i]>arr[i+1]:
                        continue
                    else:
                        return False  
        if not peak:
            return False
        else:
            return True
                

           
