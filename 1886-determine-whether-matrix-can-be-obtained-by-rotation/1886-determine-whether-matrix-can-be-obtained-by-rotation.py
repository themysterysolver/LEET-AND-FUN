class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def dis(mat):
            for r in mat:
                print(r)
            print('-----------')
        for _ in range(4):
            r = []
            for row in mat:
                r.insert(0,row)
            for i in range(n):
                for j in range(i):
                    r[i][j],r[j][i] = r[j][i],r[i][j]
            mat = r[:][:]
            #dis(mat)
            flag = True
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        flag = False
                        break
            if flag:
                return True
        return False
