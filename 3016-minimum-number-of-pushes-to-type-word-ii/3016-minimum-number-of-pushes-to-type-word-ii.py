class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        d = sorted(c.items(),key=lambda x:-x[1])
        nw = ''.join([x*y for x,y in d])
        # print(nw)
        hash = defaultdict(int)
        count = 0
        press = 0
        for w in nw:
            if w in hash:
                press+=hash[w]
            else:
                count+=1
                hash[w] = count//8+1 if count%8!=0 else count//8
                press+=hash[w]
            #print(w,count,press,hash[w])
        return press
