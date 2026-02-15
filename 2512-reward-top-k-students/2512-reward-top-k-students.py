class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        hash = {i:0 for i in student_id}
        p = set(positive_feedback)
        n = set(negative_feedback)
        for i,val in zip(student_id,report):
            print(val)
            for w in val.split():
                if w in p:
                    hash[i]+=3
                if w in n:
                    hash[i]-=1
            #print()
        heap = []
        for key,val in hash.items():
            heapq.heappush(heap,(-val,key))
        print('heap:',heap)
        ans = []
        for i in range(k):
            if heap:
                _,id = heapq.heappop(heap)
                ans.append(id)
            else:
                break
        return ans
