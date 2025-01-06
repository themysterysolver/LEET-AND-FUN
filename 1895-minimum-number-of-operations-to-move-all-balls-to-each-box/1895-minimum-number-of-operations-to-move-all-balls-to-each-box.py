class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        b=list(boxes)
        answer=[0]*len(boxes)
        for i in range(len(boxes)):
            ans=0
            for j in range(len(boxes)):
                if i==j:
                    continue
                else:
                    if boxes[j]=='1':
                        ans+=abs(i-j)
            answer[i]=ans
        return answer