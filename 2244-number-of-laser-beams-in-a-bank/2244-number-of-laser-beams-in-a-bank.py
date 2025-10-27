class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        count = 0
        for row in bank:
            curr = row.count('1')
            count+=curr*prev
            if curr!=0:
                prev = curr
        return count