#idea is montonic stack
#mostly we do it by index but since here everything is unique qe can use hash map for easy mapping
#idea is that once we see a larger element than stack we mean that we have seen a greater el than prev,
#thus we assign next greater el of prev as curr
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash = dict()
        for num in nums2:
            while stack and num>stack[-1]:
                prev = stack.pop()
                hash[prev] = num
            stack.append(num)
        for el in stack:
            hash[el] = -1
        return [hash[i] for i in nums1]