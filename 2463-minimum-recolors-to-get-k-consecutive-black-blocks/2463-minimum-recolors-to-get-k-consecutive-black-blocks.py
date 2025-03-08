class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start=0
        wf=0
        mini=float('inf')
        for i in range(len(blocks)):
            if blocks[i]=="W":
                wf+=1
            if i-start+1==k:
                mini=min(wf,mini)
                if blocks[start]=="W":
                    wf-=1
                start+=1
        return mini 


            
