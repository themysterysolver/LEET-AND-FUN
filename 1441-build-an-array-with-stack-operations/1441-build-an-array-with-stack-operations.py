class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        stack = []
        maxi = max(target)
        for i in range(1,n+1):
            if i>maxi:
                break
            if i in target:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")
        return stack