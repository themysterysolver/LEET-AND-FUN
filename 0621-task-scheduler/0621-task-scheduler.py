# cooldown deque is used to store time req to cooldown and pus it into heap
# heap is used to do with most freq element
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        cooldown=deque()
        heap=[(-f,val) for val,f in freq.items()]
        heapq.heapify(heap)
        time=0

        while cooldown or heap:
            time+=1
            if cooldown and time==cooldown[0][0]:
                _,f,val=cooldown.popleft()
                heapq.heappush(heap,(f,val))
            if heap:
                f,val=heapq.heappop(heap)
                if -f>1:
                    cooldown.append((time+1+n,f+1,val))
        return time
