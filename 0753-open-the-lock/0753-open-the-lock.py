class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited=set(deadends)
        if "0000" in visited:
            return -1
        q=deque(["0000"])
        visited.add("0000")
        #slot simulation
        nextSlot={str(i):str(i+1) for i in range(9)}
        nextSlot["9"]="0"
        #print(nextSlot)
        prevSlot={str(i):str(i-1) for i in range(1,10)}
        prevSlot["0"]="9"
        #print(prevSlot)
        count=0
        while q:
            l=len(q)
            for i in range(l):
                s=q.popleft()
                if s==target:
                    return count
                for i in range(4):
                    #simulating previous wheel for index i
                    prev_combination=list(s)
                    prev_combination[i]=prevSlot[prev_combination[i]]
                    prev_combination=''.join(prev_combination)
                    if prev_combination not in visited:
                        q.append(prev_combination)
                        visited.add(prev_combination)
                    #simulating next wheel for index i
                    next_combination=list(s)
                    next_combination[i]=nextSlot[next_combination[i]]
                    next_combination=''.join(next_combination)
                    if next_combination not in visited:
                        q.append(next_combination)
                        visited.add(next_combination)
            count+=1
        return -1


                
        

