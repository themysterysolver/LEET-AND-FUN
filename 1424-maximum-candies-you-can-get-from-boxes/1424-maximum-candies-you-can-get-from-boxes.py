class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        count = 0
        q = deque(initialBoxes) #contains boxes
        # for i in range(len(status)):
        #     if status[i] == 1:
        #         q.append(i)
        #         #visited.add(i)
        #keys = set()
        visited = set()
        while q:
            flag = False
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                if node in visited:
                    continue
                if status[node] == 1:
                    flag = True
                    count+=candies[node]
                    visited.add(node)
                    for k in keys[node]:
                        status[k] = 1
                    for el in containedBoxes[node]:
                        q.append(el)
                else:
                    q.append(node)
                
            if not flag:
                break
            print('BOXES',q)
            print('status',status)
            print('candies',count)
        return count
        