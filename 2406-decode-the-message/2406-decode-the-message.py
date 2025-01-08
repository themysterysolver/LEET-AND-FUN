class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s=set()
        hash=dict()
        idx=0
        for k in key:
            if k!=' ' and k not in s:
                hash[k]=chr(ord('a')+idx)
                idx+=1
                s.add(k)
        '''for k,v in hash.items():
            print(k,v)'''
        result=""
        for m in message:
            print(m)
            if m==' ':
                result+=' '
            else:
                result+=hash[m]
        return result
