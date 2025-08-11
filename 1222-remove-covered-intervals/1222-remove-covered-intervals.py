class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        for a,b in intervals:
            if not stack:
                stack.append((a,b))
            elif a>=stack[-1][0] and b<=stack[-1][1]:
                continue
            else:
                stack.append((a,b))
        print(stack)
        ns = []
        for a,b in stack:
            if not ns:
                ns.append((a,b))
            #print(stack,a<=ns[-1][0],b>=ns[-1][1])
            elif a<=ns[-1][0] and b>=ns[-1][1]:
                c,d = ns.pop()
                ns.append((a,b))
            else:
                ns.append((a,b))
        print(ns)
        return len(ns)