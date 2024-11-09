class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        hash=dict()
        for i in range(numRows):
            hash[i+1]=""
        print(hash)
        counter=1
        direction="DOWN"
        for i in range(len(s)):
            if direction=="DOWN":
                hash[counter]=hash[counter]+s[i]
                counter+=1
                if counter>numRows:
                    direction="UP"
                    counter-=2
            elif direction=="UP":
                hash[counter]=hash[counter]+s[i]
                counter-=1
                if counter<1:
                    direction="DOWN"
                    counter+=2
        answer=''.join(hash.values())
        print(hash)
        return answer