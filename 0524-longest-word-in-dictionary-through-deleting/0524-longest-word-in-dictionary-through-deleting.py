class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        lmax = 0
        string = "z"*10; 
        bl = len(s)
        for w in dictionary:
            #print(w)
            i = 0
            l = len(w)
            flag = True 
            for c in w:
                if i == bl:
                    flag = False
                    break
                while s[i]!= c:
                    i+=1
                    if i == bl:
                        flag = False
                        break
                    if s[i] == c:
                        i+=1
                        break
            #print(flag,i,len(w),lmax)
            if flag:
                if len(w)>lmax:
                    string = w
                    lmax = len(w)
                elif len(w) == lmax:
                    string = min(w,string)
            #print('-----------------------')
        return string if string!="z"*10 else ""