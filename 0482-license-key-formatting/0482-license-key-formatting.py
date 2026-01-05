class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ns = ''.join(s.split('-')).upper()
        print(ns)
        news = ""
        count = 0
        for i in range(len(ns)-1,-1,-1):
            if count == k:
                news = "-" + news
                count = 0
            news = ns[i]+news
            count+=1
            # print(i,count,news,s[i])
        return news