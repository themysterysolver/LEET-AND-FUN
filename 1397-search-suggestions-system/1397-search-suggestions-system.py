class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        #result.sort()
        s=""
        for idx,c in enumerate(searchWord):
            s+=c
            r = []
            for p in products:
                if s==p[:idx+1]:
                    r.append(p)
            r.sort()
            result.append(r[:3])
        return result