class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        cput = [0]*n
        prev = 0
        #note the interval is e-s+1
        for log in logs:
            id,T,time = log.split(":")
            id,time = int(id),int(time)
            if T == "start":
                if stack:
                    cput[stack[-1]]+=time-prev
                stack.append(id)
                prev = time
            else:
                cput[stack.pop()]+=time-prev+1
                prev = time+1
        return cput


