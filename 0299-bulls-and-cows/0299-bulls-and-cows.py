class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        c1=Counter(secret)
        c2=Counter(guess)
        #print('BEFORE:\nCounter 1:{}\nCounter 2:{}\n-----'.format(c1,c2))
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                c1[secret[i]]-=1
                c2[secret[i]]-=1
                bull+=1
        #print('BULL:{}'.format(bull))
        #print('AFTER:\nCounter 1:{}\nCounter 2:{}\n-----'.format(c1,c2))
        cow=0
        for key,val in c2.items():
            if key in c1:
                cow+=min(val,c1[key])
        #print('COW:{}'.format(cow))
        return str(bull)+"A"+str(cow)+"B"

