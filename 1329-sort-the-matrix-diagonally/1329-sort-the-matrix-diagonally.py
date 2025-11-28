class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hash = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hash[i-j].append(mat[i][j])
        
        for val in hash.values():
            val.sort()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = hash[i-j].pop(0)
        
        return mat