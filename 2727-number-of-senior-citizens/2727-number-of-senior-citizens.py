class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in range(len(details)):
            details[i]=int(details[i][11:13])
            if details[i]>60:
                count+=1  
        print(details)     
        return count