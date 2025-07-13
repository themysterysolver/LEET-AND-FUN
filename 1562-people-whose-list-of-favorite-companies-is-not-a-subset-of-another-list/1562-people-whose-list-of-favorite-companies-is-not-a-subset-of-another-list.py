class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(f) for f in favoriteCompanies]
        
        result  = []

        for i in range(len(sets)):
            flag = True
            for j in range(len(sets)):
                if i!=j and sets[i].issubset(sets[j]):
                    flag = False
                    break
            if flag:
                result.append(i)
        return result