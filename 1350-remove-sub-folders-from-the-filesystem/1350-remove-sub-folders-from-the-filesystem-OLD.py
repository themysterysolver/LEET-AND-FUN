class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        print(folder)
        result=[]
        for f in folder:
            doesnt_exist=True
            for c in result:
                if c in f:
                    if (len(c)==len(f) or f[len(c)]=='/') and f.index(c)==0:
                        doesnt_exist=False
                        break
            if doesnt_exist:
                result.append(f)
            #print(f,result)
        return result
        
