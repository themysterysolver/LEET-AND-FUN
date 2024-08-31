class Solution(object):
    def merge_sort(self,intervals):
        if len(intervals)<=1:
            return intervals
        #print intervals
        mid=len(intervals)//2
        #print mid
        left=self.merge_sort(intervals[:mid])
        right=self.merge_sort(intervals[mid:])
        return self.mergeh(left,right)

    def mergeh(self,left,right):
        new=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i][0]<=right[j][0]:
                new.append(left[i])
                i+=1
            elif left[i][0]>right[j][0]:
                new.append(right[j])
                j+=1
        while i<len(left):
            new.append(left[i])
            i+=1
        while j<len(right):
            new.append(right[j])
            j+=1
        return new


    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start=0
        index=0
        print intervals
        intervals=self.merge_sort(intervals)
        print intervals
        for i in range(len(intervals)-1):
                if intervals[i][len(intervals[i])-1]>=intervals[i+1][0] :
                    intervals[i][len(intervals[i])-1]=max(intervals[i+1][len(intervals[i+1])-1],intervals[i][len(intervals[i])-1])
                    intervals[i+1]=intervals[i]
        unique_t=set(tuple(i) for i in intervals)
        unique=[list(t) for t in unique_t] 
        print unique
        return unique
            
            
        